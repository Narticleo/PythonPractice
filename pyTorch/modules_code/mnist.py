from torch import nn

class mnist_module(nn.Module):
    def __init__(self):
        super(mnist_module, self).__init__()
        self.seq = nn.Sequential(
            nn.Conv2d(1, 9, 3, 1, 1), #1*28*28 -> 9*28*28
            nn.MaxPool2d(2), #9*28*28 -> 9*14*14
            nn.Conv2d(9, 9, 3, 1, 1), #still 9*14*14
            nn.MaxPool2d(2), #9*14*14 -> 9*7*7
            nn.Flatten(),
            nn.Linear(9*7*7, 10)
        )
    def forward(self, x):
        return self.seq(x)
    
    