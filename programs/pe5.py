t=20
a=[i for i in range(1,21)]
while(1):
    status=1
    for i in a:
        if (not(t%i==0)):
            status=0
            break
    if status:
        break
    t+=1
print(t)