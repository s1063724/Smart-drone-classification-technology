from pathlib import Path

import torch


class Config:
    # network arch
    num_classes = 2

    # optimization
    learning_rate = 0.001
    momentum = 0.9  #當遇到山坡時加速

    # data loading
    batch_size = 10
    num_workers = 4
    pin_memory = True

    root: Path = Path('data')

    # training related
    device = 'cuda' if torch.cuda.is_available() else 'cpu'#有gpu就用否則使用cpu
    epochs = 10

