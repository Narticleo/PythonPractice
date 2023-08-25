import torch as tc
import numpy as np

a = tc.tensor([[1,2,3],[4,5,6]])
b = tc.tensor([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

# print((a@b).numpy())

x = tc.tensor([1,2,3,4])
y = tc.tensor([4,5,6])

x = tc.reshape(x , (2, 2))
# print(x.argmax())
# print(x.T)


x = tc.tensor([[1, 2, 3, 4],
              [2, 3, 4, 5],
              [3, 4, 5, 6], 
              [4, 5, 6 ,7]])

y = x.view(2, 8)
y[0] = tc.tensor([0]*8)
# print(x)

z = tc.randint(low = 10, high = 20, size = (2, 3, 4))
# print(z)
# print(z.permute((1 ,2, 0)))
# print(z.reshape((3, 4, 2)))

x1 = tc.tensor([1, 2, 3])
x2 = tc.tensor([4, 5, 6])
x1 = tc.stack((x1, x2), dim = 0)
# print(x1)


x = tc.randint(1, 5, (3, 4, 5))
x_rev = x.flip(2)
print(x)
print(x_rev)


# device choosing
device = "cuda" if tc.cuda.is_available() else "cpu"
tensor1 = tc.tensor([1, 2, 3]).to(device)
# print(tensor1.device)

#pratical list skill
all_member = dir(tc.nn.Module)
all_member = [ member for member in all_member if "parameter" in member]
# print(all_member)