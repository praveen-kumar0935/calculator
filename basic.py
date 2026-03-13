n=int(input('enter a number:'))
temp=n
while temp>9:
    s=0
    while temp>0:
        s+=temp%10
        temp=temp//10
    temp=s
if temp==1:
    print('magic')
else:
    print('no')

'''
n = int(input())

temp = n

# Repeated digit sum
while temp > 9:
    s = 0
    while temp > 0:
        s += temp % 10
        temp //= 10
    temp = s

if temp == 1:
    print("Magic Number")
else:
    print("Not a Magic Number")'''

