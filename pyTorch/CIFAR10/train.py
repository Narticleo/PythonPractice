import torchvision
from torch.utils.tensorboard import SummaryWriter
transforms = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor()
])

train_set = torchvision.datasets.CIFAR10(root = "./dataset", train = True, download = True, transform = transforms)
test_set = torchvision.datasets.CIFAR10(root = "./dataset", train = False, download = True, transform = transforms)

# print(train_set[0])
writer = SummaryWriter("tensorboard")

for i in range(20):
    img, label = train_set[i]
    writer.add_image("test", img, i)

writer.close()
