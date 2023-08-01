import torch
from torch.autograd import Variable
tensor = torch.FloatTensor([[1,2],[3,4]])
variable = Variable(tensor, requires_grad=True)
print(variable.data)
v_out = (variable*variable).mean()
# v_out.backward()
v1_out = (variable*variable*variable).median()
v1_out.backward()

print(variable.grad)
print(variable.data)
print(variable.data.numpy().astype(int))

# print((tensor*tensor).mean())
# print((variable*variable).mean())