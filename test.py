datas = ["0017","1299","1123"]
age = [""*4 for row in range(3)]
for i in range(0,len(datas)):
    age[i] = datas[i][2:4]
    print(int(age[i]))
print(int(datas[0][0:2]))