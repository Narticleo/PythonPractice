import torch
import torch.nn.functional as nnf
import torch.nn as nn
import matplotlib.pyplot as plt

n_data = torch.ones(100, 2)
x0 = torch.normal(2*n_data, 1)
y0 = torch.zeros(100)

x1 = torch.normal(-2*n_data, 1)
y1 = torch.ones(100)

x = torch.cat((x0, x1), 0)
y = torch.cat((y0, y1), )
# y = nnf.one_hot(y.to(torch.int64))
# print(y)
# plt.scatter(x.data.numpy()[:, 0], x.data.numpy()[:, 1],c = y.data.numpy(), s = 100, lw = 0)
# plt.show()

class NET(nn.Module):
    def __init__(self, n_feature, output):
        super(NET, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(n_feature, 10),
            nn.ReLU(),
            nn.Linear(10, 5),
            nn.ReLU(),
            nn.Linear(5, output)
        )
    def forward(self, x):
        return self.net(x)
net = NET(2, 2)
opt = torch.optim.Adam(net.parameters(), lr = 0.001)
loss_func = nn.CrossEntropyLoss()
prediction = net(x)
print(prediction.shape, y.shape)

loss = nn.CrossEntropyLoss(prediction, y)
# print(loss)
# iter = 2000

# for i in range(iter):
#     prediction = net(x)
#     loss = loss_func(prediction, y)
#     opt.zero_grad()
#     loss.backward()
#     opt.step()