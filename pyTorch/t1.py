import torch
import torch.nn.functional as nnf

x = torch.tensor([1, 2 ,3, 1, 2, 3, 4, 1, 2, 1, 4])
x = nnf.one_hot(x)
print(x)