#sum 0f multiples of 3 or 5
s=0
for x in [i for i in range(3,1000) if(i%3==0 or i%5==0)]:
    s = s + x
print(s)