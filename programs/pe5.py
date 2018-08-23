# smallest number divisible by all numbers less than 21
num = 2
div = 2
while div!=21:
    if num%div == 0:
        div += 1
        temp = num
    else: num += temp
print(num)