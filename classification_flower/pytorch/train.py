import argparse
import os
from math import inf

import PIL
import torch
import matplotlib.pyplot as plt
from torch import optim
from torch.optim.optimizer import Optimizer
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader
from torchvision import transforms

from classification_flower.config import Config
from classification_flower.model import get_model

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'


def main():
    # args = get_arg_parser().parse_args()
    model: torch.nn.Module = get_model(2)
    print(model)
    loss_func = torch.nn.CrossEntropyLoss()
    config = Config()

    # 資料前處裡
    transform = transforms.Compose([
        transforms.Resize(size=(150, 150), interpolation=PIL.Image.BILINEAR),  # interpolation用來處理照片放大的模糊區域
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))  # (rgb average,rgb 標準差)
    ])

    train_set = ImageFolder('./data/train', transform=transform)
    valid_set = ImageFolder('./data/valid', transform=transform)

    train_loader = DataLoader(train_set, batch_size=5, shuffle=True, num_workers=4, pin_memory=True)
    valid_loader = DataLoader(valid_set, batch_size=5, num_workers=4, pin_memory=True)

    # 載入需優化的方法
    optimizer = optim.SGD(model.parameters(), lr=config.learning_rate,momentum=config.momentum)
    train_losses, train_accuracies, test_losses, test_accuracies = \
        fit(train_loader, valid_loader, model, optimizer, loss_func, config)

    plt.figure()
    plt.title('loss')
    plt.plot(train_losses, label='train')
    plt.plot(test_losses, label='test', linestyle='dashed')
    plt.legend()
    plt.show()

    plt.figure()
    plt.title('accuracy')
    plt.plot(train_accuracies, label='train')
    plt.plot(test_accuracies, label='test', linestyle='dashed')
    plt.legend()
    plt.show()


def fit(
        train_loader: DataLoader,
        valid_loader: DataLoader,
        model: torch.nn.Module,
        optimizer: Optimizer,
        loss_func,
        config: Config
):
    train_accuracies = []
    train_losses = []
    test_accuracies = []
    test_losses = []

    model.to(config.device).train()  # 使用gpu計算
    n_batch = len(train_loader)

    best_model_indicate = inf
    best_model = None
    for epoch in range(config.epochs):
        train_loss = 0
        correct = 0
        n_pred = 0  #預測幾個
        for batch_idx, (batch, targets) in enumerate(train_loader):  # batch_idx=當批序號
            batch = batch.to(config.device)
            targets = targets.to(config.device)

            pred: torch.Tensor = model(batch)
            loss = loss_func(pred, targets)
            loss.backward()  # 梯度

            optimizer.step()  # 更新權重
            optimizer.zero_grad()  # 將優化度歸零
            train_loss += loss.item()
            correct += (pred.cpu().argmax(dim=1) == targets.cpu()).sum().item()
            n_pred += batch.size(0)
            print('\repoch: %d/%d , batch: %d/%d , loss: %.6f , accuracy: %.6f' % (
                epoch + 1, config.epochs, batch_idx + 1, n_batch, loss.item(), correct / n_pred
            ), end='')
        train_loss, train_acc = train_loss / n_pred, correct / n_pred
        test_loss, test_acc = valid(valid_loader, model, loss_func, config)
        print('\repoch: %d/%d , train_loss: %.6f , train_accuracy: %.6f , val_loss: %.6f , val_acc: %.6f' % (
            epoch + 1, config.epochs, train_loss, train_acc, test_loss, test_acc
        ))

        model_indicate = (train_loss * test_loss) / (train_acc * test_acc)
        if model_indicate < best_model_indicate:
            best_model = model.state_dict()
            best_model_indicate = model_indicate

        train_accuracies.append(train_acc)
        train_losses.append(train_loss)
        test_accuracies.append(test_acc)
        test_losses.append(test_loss)

    torch.save(
        {
            'model': model.state_dict(),
            'optimizer': optimizer.state_dict()
        }, 'checkpoint.pt'
    )

    torch.save(
        {
            'model': best_model,
        }, 'best.pt'
    )
    return train_losses, train_accuracies, test_losses, test_accuracies


@torch.no_grad()
def valid(
        valid_loader,
        model,
        loss_func,
        config
):
    model.to(config.device).eval()
    test_loss = 0
    correct = 0
    n_pred = 0
    for batch_idx, (batch, targets) in enumerate(valid_loader):  # batch_idx=當批序號
        batch = batch.to(config.device)
        targets = targets.to(config.device)

        pred: torch.Tensor = model(batch)
        loss = loss_func(pred, targets)
        test_loss += loss.item()
        correct += (pred.cpu().argmax(dim=1) == targets.cpu()).sum().item()
        n_pred += batch.size(0)

    test_loss /= n_pred
    test_acc = correct / n_pred
    return test_loss, test_acc


# def get_arg_parser():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-e', '--epochs', type=int, default=10)
#     return parser


if __name__ == '__main__':
    main()
