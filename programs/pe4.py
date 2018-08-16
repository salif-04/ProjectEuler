def palindrome(num):
    x=num
    s=0
    while(x>0):
        s=s*10+(x%10)
        x=int(x/10)
    if s == num:
        return True
    else:
        return False
max_num = 0
for i in range(990,99,-11):
    for j in range(999,99,-1):
        if(palindrome(i*j) and i*j>max_num):
            max_num = i*j
            break
print(max_num)