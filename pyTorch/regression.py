import torch
from torch.autograd import Variable
import torch.nn.functional as nnf
import matplotlib.pyplot as plt

x = torch.unsqueeze(torch.linspace(-10,10,100), dim = 1)
y = x.pow(2) + 20*torch.rand(x.size())

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
optimizer = torch.optim.Adam(net.parameters(), lr = 0.5)
loss_func = torch.nn.MSELoss()

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