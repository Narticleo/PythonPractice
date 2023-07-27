import numpy as np

a = np.random.randint(1, 21, size = (2,2))
b = np.random.randint(11, 31, size = (2,2))
print("a:\n",a,"\nb:\n",b)
print("a+b:\n",a+b)
print("a-b:\n",a-b)
print("a*b:\n",a*b)
print("a/b:\n",a/b)
print("a[0]*b[0]:\n",np.dot(a[0],b[0]))
print("a@b:\n",a@b)
print("sqrt(a):\n",np.sqrt(a))
print("cos(a):\n",np.cos(a))
print("sin(a):\n",np.sin(a))
print("pow(a,3):\n",np.power(a,3))
print("log(a):\n",np.log(a))
print("a.min a.max a.sum:\n",a.min(axis = 0),a.max(axis = 1),a.sum(axis = 0))
print("a.argmin:\n",a.argmax())
print("a.mean a.median a.std a.var:\n",a.mean(), np.median(a), a.std(), a.var())





