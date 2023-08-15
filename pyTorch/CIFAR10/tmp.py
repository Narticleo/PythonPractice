import math
import numpy as np

arr = np.array([2.3610, 0.4933])
print(arr.mean(), arr.std())
arr = (arr - arr.mean()) / arr.std()
print(arr)