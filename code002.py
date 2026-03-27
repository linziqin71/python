#coding:utf-8
#程序设计第二课


a = 1
b = 2
if(a<b):
    print("第一个数小")


def jioushu(a):
    if(a%2==1):
        return "奇数"
    else:
        return "偶数"   
print(jioushu(a))



count = 1
while count <= 99:
    print(count)
    count += 1


for j in range(0,100):
    print(j)
    print(jioushu(j))


list = [0,1,21,"xiaoming",'a']
for i in list:
    print(i)

def panduan(k):
    if k % 3 == 0 and k % 7 == 0:
        return k
    else:
        return None 

for k in range(1, 1001):
    result = panduan(k)
    if result is not None:
        print(result)


    


