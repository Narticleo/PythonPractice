from torch.utils.data import DataLoader
import torchvision
from torch.utils.tensorboard import SummaryWriter

test_set = torchvision.datasets.CIFAR10("./dataset", train = False, transform = torchvision.transforms.ToTensor())

test_loader = DataLoader(test_set, batch_size = 20, shuffle = False, drop_last = False)

writer = SummaryWriter("dataloader")
for epoch in range(2):
    step = 0
    for data in test_loader:
        imgs, labels = data
        writer.add_images("epoch:{}".format(epoch), imgs, step)
        step += 1


writer.close()