a,b=1,2
s = 2
while(a+b < 4000000):
    c=a+b
    if (c%2 == 0):
        s = s+c
    a=b
    b=c
else:
    print(s)