import torch as tc
import numpy as np
array = np.arange(10).reshape((2,5))
torch = tc.from_numpy(array)
arr1 = torch.numpy()

print(array, torch , arr1 , sep = "\n")