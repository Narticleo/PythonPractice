import torchvision
from torch import nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
import torch
dataset = torchvision.datasets.CIFAR10("./dataset", train = False, transform = torchvision.transforms.ToTensor())
loader =  DataLoader(dataset, batch_size = 8, shuffle = False)
class myConv2d(nn.Module):
    def __init__(self):
        super(myConv2d, self).__init__()
        self.net = nn.Sequential(
            nn.Conv2d(in_channels = 3, out_channels = 3, kernel_size = 3, stride = 2, padding = 1)
        )
    def forward(self, x):
        return self.net(x)
    
writer = SummaryWriter("./conv2d-1")
net = myConv2d()
step = 0
for data in loader:
    imgs ,labels = data
    writer.add_images("origin data", imgs, step)
    results = net(imgs).reshape((-1, 3, 16, 16))
    writer.add_images("after conv2d", results, step)
    step += 1

writer.close()

    

