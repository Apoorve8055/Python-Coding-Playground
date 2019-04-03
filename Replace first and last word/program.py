data = input()
data1 = data.split(' ')
print(data1)
data1[0]= "xxxx"
data1[-1]= "zzzz"
data = " ".join(data1)
print(data)