import torch
from torch.autograd import Variable
import torch.nn.functional as nnf
import matplotlib.pyplot as plt

#一維轉二維(1,100)
x = torch.unsqueeze(torch.linspace(-10,10,100), dim = 1)
y = x.pow(3) + 10*torch.rand(x.size())

# plt.scatter(x, y)
# plt.show()

class NET(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(NET, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden, bias = True)
        self.h1 = torch.nn.Linear(n_hidden, 5)
        self.predict = torch.nn.Linear(5, n_output)
    def forward(self, x):
        x = nnf.relu(self.hidden(x))
        x = nnf.relu(self.h1(x))
        x = self.predict(x)
        return x
    
net = NET(1, 10, 1)
# print(net)
optimizer = torch.optim.Adam(net.parameters(), lr = 0.5)
loss_func = torch.nn.MSELoss()
#列印出參數的數量
# p_num = sum(p.numel() for p in net.parameters())
# print(p_num)
for i in range(100):
    prediction = net(x)
    loss = loss_func(prediction, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    plt.cla()
    plt.scatter(x.data.numpy(), y.data.numpy())
    plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-')
    plt.pause(0.05)

