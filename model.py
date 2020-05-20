from torchvision import models


def get_model(num_classes: int):
    return models.resnet18(num_classes=num_classes)#RestNet模型