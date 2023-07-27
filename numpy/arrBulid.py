import numpy as np

a = np.zeros((5,10,11))
print(a.shape)

arange = np.arange(7,0,-1)
print("arange",arange)

lins = np.linspace(0,100,5,dtype = np.int8)
print("linspace",lins)

rand = np.random.rand(2,4)
rand = rand.astype(np.int32)
print("rand",rand)