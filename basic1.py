'''n = int(input())
s = 0
for i in range(1, n):
    if n % i == 0:
        s += i

if s == n:
    print("Perfect Number")
else:
    print("Not Perfect")'''
#prime number
'''num=11
praveen=False
if num<2:
    praveen=False
else:
    for i in range(2,num):

        if num%i==0:
            praveen=True
            break

if praveen==True:
    print('non prime')
else:
    print('prime')

n=int(input('enter size'))
j=0
l=[0 for i in range(n)]
for i in range(n):
    a=int(input('enter each value'))
    if a!=0:
        l[j]=a
        j+=1

for i in l:
    print(i,end='')
'''

'''n=int(input())
b=bin(n)[2:]
toggeled=""
for i in (b):
    if i =='0':
        toggeled+='1'
    else:
        toggeled+='0'

result=int(toggeled,2)
print(result)
'''

n=int(input('enter size'))
arr=[]
for i in range(n):
    arr.append(int(input()))
for i in sorted (arr):
    print(i,end='')





