import torchvision
import cv2
import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset
from torch.utils.tensorboard import SummaryWriter

#preparing data
train_data = torchvision.datasets.MNIST('../Dataset/MNIST', train = True, 
                                        transform = torchvision.transforms.ToTensor(), download = True)
test_data = torchvision.datasets.MNIST('../Dataset/MNIST', train = False, 
                                        transform = torchvision.transforms.ToTensor(), download = True)

train_loader = DataLoader(train_data, batch_size = 32)
test_loader = DataLoader(test_data, batch_size = 32)



# neural network
class mnist_module(nn.Module):
    def __init__(self):
        super(mnist_module, self).__init__()
        self.seq = nn.Sequential(
            nn.Conv2d(1, 9, 3, 1, 1), #1*28*28 -> 9*28*28
            nn.MaxPool2d(2), #9*28*28 -> 9*14*14
            nn.ReLU(),
            nn.Conv2d(9, 9, 3, 1, 1), #still 9*14*14
            nn.MaxPool2d(2), #9*14*14 -> 9*7*7
            nn.ReLU(),
            nn.Conv2d(9, 32, 3, 1, 1), #9*7*7 -> 32*7*7
            nn.Flatten(),
            nn.Linear(32*7*7, 10)
        )
    def forward(self, x):
        return self.seq(x)
    

#settings
lr = 1e-3
epoch = 10
device = 'cuda' if torch.cuda.is_available() else 'cpu'
module = mnist_module()
loss_func = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(module.parameters(), lr)
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, 10, 0.99)
writer = SummaryWriter('../tensorboard/mnist')
test_size = len(test_data)


module.to(device)
loss_func.to(device)

#traing and testing
train_step = 0
for i in range(epoch):
    print(f'epcoh:{i}','training','----------------------------------------------', sep = '\n')
    module.train()
    for img, labels in train_loader:
        img, labels = img.to(device), labels.to(device)
        prediction = module(img)
        loss = loss_func(prediction, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        scheduler.step()
        if (train_step % 100) == 0 :
            writer.add_scalar('training loss', loss.item(), train_step, new_style = True)
            print(f'step:{train_step:5d}, loss:{loss.item():.6f}')
        train_step += 1
    print('testing')
    print('---------------------------------------------')
    module.eval()
    test_step = 0
    total_acc = 0
    total_loss = 0
    with torch.no_grad():
       for img, labels in test_loader:
            img, labels = img.to(device), labels.to(device)
            prediction = module(img)
            loss = loss_func(prediction, labels)
            accuracy = (prediction.argmax(1) == labels).sum()
            total_acc += accuracy.item()
            total_loss += loss.item()
            test_step += 1
    writer.add_scalar('testing loss', total_loss, test_step, new_style = True)
    writer.add_scalar('accuracy', total_acc/test_size, i, new_style = True)
    print(f'accuracy:{(total_acc/test_size)*100:.3f}%')
writer.close()


