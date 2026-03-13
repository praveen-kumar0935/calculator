'''n=5
total=0
for i in range(1,n+1):
    total +=i
    print(total)'''
'''
n=10
for i in range(1,11):
    res={n*i}
    print(f"{n}*{i}={res}")
    print('{}*{}={}'.format(n,i,n*i))'''
'''
for i in range(1,51):
    if i%2 == 1:
        print(i)

n=input('enter a string')
vowels='aeiouAEIOU'
count=0
for i in n:
    if i in vowels:
        count+=1
        print(i)
'''
#factorial of a number
'''
n=5
fact=1
for i in range(1,10):
    fact*=i
    print(fact)
'''
#count digits in a number
'''
n=12345
count=0
while n>0:
    n//=10
    count+=1
    print(count)
    '''
#print each letter
'''text='praveen'
for char in text:
    print(char)'''
#printing square pattern
'''
n=5
for i in range (n):
    print('*'*i)'''
'''
n=6
for i in range(1,n+1):
    print('*'*i)'''

#print index of list
'''a=["apple","banana","cherry"]
for i in range(len(a)):
    print(f"{i}:{a[i]}")

fruits = ["apple", "banana", "cherry"]
for index in range(len(fruits)):
    print(f"{index}: {fruits[index]}")'''

#reverse a string 
'''
text="kumar"
reversed_text=""
for char in text:
    reversed_text=char+reversed_text
    print(reversed_text)'''

'''text = "python"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(reversed_text)'''
#count vowels in string
'''text='PRAVEEN BONDA sai'
vowels='aeiouAEIOU'
sum=0
for char in text:
    if char in vowels:
        sum+=1
        print(char)'''
#prime number
'''num = 17
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

print("Prime" if is_prime else "Not Prime")'''
#fizzbuzz program
'''for i in range(1,100):
    if i%3==0 and i%5==0:
        print('fizzbuzz')
    if i%3==0:
        print('fizz')
    if i%5==0:
        print('buzz')'''
'''for i in range(1, 15):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)'''
#fibonacci series
'''
n=int(input('enter user value:'))
a,b=0,1
for i in range(n):
    print(a)
    a,b=b,a+b'''
    
#find max number in list
'''numbers=[29,34,8,1,7]
max_num=numbers[0]
for i in numbers:
    if i>max_num:
        print("maximum:",i)'''

# sum of digits in a  number

'''n=1234
total=0
for digits in str(n):
    total+=int(digits)
    print('sum of digits:',total
#palindrome
def is_palindrome_number(num):
    original = num
    reversed_num = 0

    while num > 0:
        digit = num % 10                  # Get the last digit
        reversed_num = reversed_num * 10 + digit  # Build the reversed number
        num //= 10                        # Remove the last digit

    return original == reversed_num
number = int(input("Enter a number: "))

if is_palindrome_number(number):
    print("It's a palindrome number!")
else:
    print("Not a palindrome number.")'''



''''n=int(input())
sum=1
while n!=0:
    r=n%10
    sum=sum*r
    n=n//10
print(sum)

def myfun(*names):
    print("my first name is "+names[1])

myfun('praveeen','bonda','kumar')

def myfun(*args):
    total=0
    for num in args:
        total+=num
    return total
print(myfun(5,6,7))
f1=myfun(1,2,3)
print(f1)'''














      





