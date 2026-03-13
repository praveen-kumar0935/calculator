'''1question
import sys
n=int(input('enter the no of values:'))
count=0
m=-sys.maxsize

while n!=0:
    a=int(input('enter the each value:'))
    n-=1
    if a>m:
        m=a
        count+=1
print(count)
'''
#2 question
'''n=int(input('enter a value:'))
temp=n
mul=1
while temp>0:
    d=temp%10
    mul=mul*d
    temp=temp//10
print(mul)'''
'''   
n=input()
pk=1
for i in n:
    pk*=int(i)
print(pk)
'''
# 3 question
'''
str=input()
n=int(input('enter the number'))
max_value=0
count=0

for i in range(len(str)):
    if i % n==0:
        max_value=max(count,max_value)
        count=0
    if str[i]=='c':
        count+=1
if count>max_value:
    max_value=count
print('no of times appear:',max_value)'''
#hens and goats
'''legs=int(input())
heads=int(input())

for i in range(1,heads):
    g_count=i
    h_count=heads-i
    l_count=g_count*4 + h_count*2
    if (legs == l_count):
        print(g_count,h_count)
        break
'''
n=int(input('enter the value:'))
pk=[]
for i in range(n):
    pk.append(int(input()))
for i in sorted(pk):
    print(i,end="")



 
 
