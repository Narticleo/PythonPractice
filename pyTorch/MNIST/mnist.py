import torchvision
import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset

train_data = torchvision.datasets.MNIST('../Dataset/MNIST', train = True, 
                                        transform = torchvision.transforms.ToTensor(), download = True)
test_data = torchvision.datasets.MNIST('../Dataset/MNIST', train = False, 
                                        transform = torchvision.transforms.ToTensor(), download = True)

print(len(train_data), len(test_data))
img, labels = train_data[0]
print(img.shape)