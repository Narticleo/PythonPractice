import torch
from torch import nn
import torchvision
from torch.utils.tensorboard import SummaryWriter
from torch.utils.data import DataLoader
dataset = torchvision.datasets.CIFAR10("dataset", train = False, 
                                       transform = torchvision.transforms.ToTensor())

loader = DataLoader(dataset, batch_size = 8, shuffle = False)

class CIFAR10(nn.Module):
    def __init__(self):
        super(CIFAR10, self).__init__()
        self.net = nn.Sequential(
            nn.Conv2d(3, 32, 5, padding = 2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 32, 5, padding = 2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 5, padding = 2),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(1024, 64),
            nn.Linear(64, 10)
        )

    def forward(self, x):
        return self.net(x)
    

module = CIFAR10()
writer = SummaryWriter("optimizer")

optimizer = torch.optim.Adam(module.parameters(), lr = 0.01) 
loss_func= nn.CrossEntropyLoss()


for epoch in range(20):
    loss_result = 0
    for data in loader:
        imgs, labels = data
        prediction = module(imgs)
        loss = loss_func(prediction, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        loss_result = loss

    print(f"loss after epoch{epoch}:{loss_result}")


