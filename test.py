class A():
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def addsub(self,a,b,c):
        return self.sub(self.add(a,b),c) 
a = A()
a.name = "abc"
print(a.name)
print(a.add(1,8))
print(a.addsub(2,3,2))