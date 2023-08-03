import torch
import torch.nn.functional as nnf
import torch.nn as nn
import matplotlib.pyplot as plt
from torch.autograd import Variable

n_data = torch.ones(100, 2)
x0 = torch.normal(2*n_data, 1)
y0 = torch.zeros(100)

x1 = torch.normal(-2*n_data, 1)
y1 = torch.ones(100)

x = torch.cat((x0, x1), 0).type(torch.FloatTensor)
y = torch.cat((y0, y1), ).type(torch.FloatTensor)

x, y = Variable(x), Variable(y)

plt.scatter(x.data.numpy()[:, 0], x.data.numpy()[:, 1],c = y.data.numpy(), s = 100, lw = 0)
plt.show()