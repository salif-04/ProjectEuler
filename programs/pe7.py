x = [2]
c = 1
num = 3
while(c!=10001):
    status = 1
    for i in x:
        if num%i == 0:
            status = 0
            break
    if status:
        x.insert(c,num)
        c = c+1
    num = num+1
print(x[10000])