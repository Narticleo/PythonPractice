import torch, torchvision
from torch import nn
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
vgg16_ori = torch.load("./modules/vgg16_origin.pth")
vgg16_mod = torch.load("./modules/vgg16_modify.pth")
module = myModule()
module.load_state_dict(torch.load("./modules/myModule.pth"))
# print(vgg16_ori)
# print(vgg16_mod)
print(module)

