import argparse

import PIL
import torch
import numpy as np
from torch import optim
from torch.optim.optimizer import Optimizer
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader
from torchvision import transforms

from classification_flower.config import Config
from classification_flower.model import get_model



def main():
    # args = get_arg_parser().parse_args()
    model: torch.nn.Module = get_model(2)
    loss_func = torch.nn.CrossEntropyLoss()
    config = Config()
    # print(vars(config))
    #資料前處裡
    transform = transforms.Compose([
        transforms.Resize(size=256, interpolation=PIL.Image.BILINEAR)  # interpolation用來處理照片放大的模糊區域
        , transforms.ToTensor()
        , transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])  # (rgb average,rgb 標準差)
    ])

    train_set = ImageFolder('./data/train', transform=transform)
    valid_set = ImageFolder('./data/valid', transform=transform)

    train_loader = DataLoader(train_set, batch_size=5, shuffle=True, num_workers=4, pin_memory=True)
    valid_loader = DataLoader(valid_set, batch_size=5, num_workers=4, pin_memory=True)

    # 載入需優化的方法
    optimizer = optim.SGD(model.parameters(), lr=config.learning_rate, momentum=config.momentum)
    fit(train_loader, valid_loader, model, optimizer, loss_func, config)

    # valid(valid_loader, model, criterion, config)


def fit(
    train_loader: DataLoader,
    valid_loader: DataLoader,
    model: torch.nn.Module,
    optimizer: Optimizer,
    loss_func,
    config: Config):
    model.to(config.device).train() #使用gpu計算

    for epoch in range(config.epochs):
        print('\nepoch:%d' % epoch)
        train_loss = 0
        correct = 0
        n_pred = 0
        for batch_idx, (batch, targets) in enumerate(train_loader):#batch_idx=當批序號
            batch = batch.to(config.device)
            targets = targets.to(config.device)

            pred: torch.Tensor = model(batch)
            loss = loss_func(pred, targets)
            loss.backward()     #梯度

            optimizer.step()    #更新權重
            optimizer.zero_grad()   #將優化度歸零
            train_loss += loss.item()
            correct += (pred.cpu().argmax(dim=1) == targets.cpu()).sum().item()
            n_pred += batch.size(0)
            print('\rloss: %.6f , accuracy: %.6f' % (loss.item(), correct / n_pred), end='')

    torch.save(model.state_dict(), './classification_flower/model.pth')
    torch.save(optimizer.state_dict(), './classification_flower/optimizer.pth')
    torch.save(train_loss, './classification_flower/train_loss.pth')


# def valid(valid_loader,
#           model,
#           criterion,
#           config):
#     model.to(config.device).eval()
#     test_loss=0
#     correct=0
#     total=0
#     for batch_idx, (data, target) in enumerate(valid_loader):
#         data = data.to(config.device)
#         output = model(data)
#         loss = criterion(output, target)
#         test_loss = test_loss + ((1 / (batch_idx + 1)) * (loss.data - test_loss))
#         pred = output.data.max(1, keepdim=True)[1]
#         correct += np.sum(np.squeeze(pred.eq(target.data.view_as(pred))).cpu().numpy())
#         total += data.size(0)
#
#     print('Test Loss: {:.6f}'.format(test_loss))
#
#     print('Test Accuracy: %2d%% (%2d/%2d)' % (100. * correct / total, correct, total))
#     # Log the images and metrics
#     wandb.log({
#         "Examples": example_images,
#         "Test Accuracy": 100. * correct / len(valid_loader.dataset),
#         "Test Loss": test_loss})


# def get_arg_parser():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-e', '--epochs', type=int, default=10)
#     return parser



if __name__ == '__main__':
    main()
