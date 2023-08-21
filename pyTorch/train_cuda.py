from numpy import mean
import torchvision, torch
from torch.utils.data import DataLoader
from torch import nn
from numpy import mean
import time
from torch.utils.tensorboard import SummaryWriter
train_data = torchvision.datasets.CIFAR10("./Dataset/CIFAR10", train = True, 
                                          transform = torchvision.transforms.ToTensor(), download = True) 
test_data = torchvision.datasets.CIFAR10("./Dataset/CIFAR10", train = False, 
                                          transform = torchvision.transforms.ToTensor(), download = True)
test_size = len(test_data)
train_loader = DataLoader(train_data, 64)
test_loader = DataLoader(test_data, 64, drop_last = True)
device = "cuda" if torch.cuda.is_available() else "cpu"
class myModule(nn.Module):
    def __init__(self):
        super(myModule, self).__init__()
        self.net = nn.Sequential(
            nn.Conv2d(3, 32, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 32, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(64*4*4, 10)
        )
    def forward(self, x):
        return self.net(x)
    
writer = SummaryWriter('tensorboard/train_cuda')
module = myModule()
module.to(device)
learning_rate = 1e-2
epoch = 15
optimizer = torch.optim.Adam(module.parameters(), lr = learning_rate)
# scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode = 'min', factor = 0.1, patience = 20, verbose = True)
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size = 10, gamma = 0.99)
loss_func = nn.CrossEntropyLoss()
loss_func.to(device)
train_step = 0
for turn in range(epoch):
    start_time = time.time()
    #training
    print(f'epoch:{turn+1}')
    module.train() #effect when dropout is in neural network
    # losses = []
    for data in train_loader:
        imgs, labels = data
        imgs, labels = imgs.to(device), labels.to(device)
        prediction = module(imgs)
        loss = loss_func(prediction, labels)
        # losses.append(loss.item())
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        scheduler.step()
        if train_step % 100 == 0:
            print(f'step : {train_step:4d},    loss : {loss.item():6f}')
            writer.add_scalar('training_loss', loss.item(), train_step)
        train_step += 1
    writer.add_scalar('learning rate', scheduler.get_last_lr()[0], turn+1)
    #testing
    test_loss = 0
    accuracy_total = 0
    module.eval()
    with torch.no_grad():
        for data in test_loader:
            imgs, labels = data
            imgs, labels = imgs.to(device), labels.to(device)
            prediction = module(imgs)
            loss = loss_func(prediction, labels)
            test_loss += loss.item()
            accuracy = (prediction.argmax(1) == labels).sum()
            accuracy_total += accuracy
    accuracy_rate = accuracy_total/test_size
    writer.add_scalar('testing_accuracy', accuracy_rate, turn+1)
    writer.add_scalar('testing_loss', test_loss, turn+1)
    print(f'accuracy : {accuracy_rate}')
    print(f'learning rate : {scheduler.get_last_lr()[0]}')
    print(time.time() - start_time)
torch.save(module, 'modules/train_py.pth')
writer.close()
