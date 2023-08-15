import torch
from torch import nn
import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10("dataset", train = False, transform = torchvision.transforms.ToTensor(), download = True)
loader = DataLoader(dataset, batch_size = 64, shuffle = False)


class MaxPool(nn.Module):
    def __init__(self):
        super(MaxPool, self).__init__()
        self.net = nn.Sequential(
            nn.MaxPool2d(kernel_size = 2, ceil_mode = True)
        )
    def forward(self, x):
        return self.net(x)
    

maxpool = MaxPool()
writer = SummaryWriter("maxpool")
step = 0
for data in loader:
    imgs, label = data
    writer.add_images("origin", imgs, step)
    results = maxpool(imgs)
    writer.add_images("pool", results, step)
    step += 1


writer.close()




