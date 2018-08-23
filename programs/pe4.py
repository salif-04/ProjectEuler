# largest palindrome made from product of two 3-digit numbers
max_num=0
for i in range(990,99,-11):
    for j in range(999,99,-1):
        num = i*j
        if(str(num)==str(num)[::-1] and num>max_num):
            max_num = num
            break
print(max_num)