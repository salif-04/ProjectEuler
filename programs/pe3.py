import math
a=[2]
c=1
num = 600851475143
limit=int(math.sqrt(num))
for i in range(3,limit):
    status=1
    for j in a:
        if(i%j==0):
            status = 0
            break
    if(status):
        a.insert(c,i)
        c=c+1
a.reverse()
for i in a:
    if(num%i==0):
        print(i)
        break