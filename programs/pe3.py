# largest prime factor of 600851475143
num = 600851475143
lar = 2
while num%2 == 0:
    num = int(num/2)
x = 3
while num != 1:
    while num%x == 0:
        num = int(num/x)
        lar = x
    x += 2
print(lar)