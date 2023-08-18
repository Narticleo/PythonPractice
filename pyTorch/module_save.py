import torchvision, torch
from torch import nn

vgg16_origin = torchvision.models.vgg16(pretrained = False)
vgg16_modify = torchvision.models.vgg16(pretrained = False)

vgg16_modify.classifier.add_module("7", nn.Linear(1000, 10))

torch.save(vgg16_origin, "./modules/vgg16_origin.pth")
torch.save(vgg16_modify, "./modules/vgg16_modify.pth")

class myModule(nn.Module):
    def __init__(self):
        super(myModule, self).__init__()
        self.net = nn.Sequential(
            nn.Conv2d(3, 5, 2),
            nn.MaxPool2d(2),
            nn.ReLU(),
            nn.Flatten()
        )
    def forward(self, x):
        return self.net(x)
modules = myModule()
torch.save(modules.state_dict(), "./modules/myModule.pth")

def hello():
    print("hello")