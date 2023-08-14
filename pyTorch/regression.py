import torch
from torch.autograd import Variable
import torch.nn.functional as nnf
import matplotlib.pyplot as plt

x = torch.unsqueeze(torch.linspace(-10,10,100), dim = 1)
y = x.sin() + 0.3*x.pow(3) + 0.8*(x**2)+ 150*torch.rand(x.size())
# y = 100*x.sin()
# plt.scatter(x, y)
# plt.show()

class NET(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(NET, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden, bias = True)
        self.predict = torch.nn.Linear(n_hidden, n_output)

    def forward(self, x):
        x = nnf.relu(self.hidden(x))
        x = self.predict(x)
        return x
    
net = NET(1, 5, 1)
# print(net)
optimizer = torch.optim.Adam(net.parameters(), lr = 0.05)
loss_func = torch.nn.MSELoss()
#列印出參數的數量
# p_num = sum(p.numel() for p in net.parameters())
# print(p_num)

for i in range(1000):
    prediction = net(x)
    loss = loss_func(prediction, y)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    plt.cla()
    plt.scatter(x.data.numpy(), y.data.numpy())
    plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-')
    plt.pause(0.05)