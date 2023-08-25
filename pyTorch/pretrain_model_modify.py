import torchvision
from torch import nn
vgg16_1 = torchvision.models.vgg16(pretrained = False)
vgg16_2 = torchvision.models.vgg16(pretrained = False)
vgg_origin = vgg16_1
vgg16_1.classifier.add_module("7", nn.Linear(1000, 10))
vgg16_2.classifier[6] = nn.Linear(4096, 10)

print(vgg16_1)
print("----------------------------------------")
print(vgg16_2)