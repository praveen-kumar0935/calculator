n=int(input())
sum=1
while n!=0:
    sum=sum*n%10
    n=n//10
print(sum)
