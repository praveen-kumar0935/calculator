'''class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfunt(self):
        print('my name is '+ self.name)

p1=person('praveen',35)    
p1.myfunt()

class praveen:
    def __init__(self):
        pass

p1=praveen()
p1.name='pk'
p1.age=23
print('my name is '+p1.name)
print(p1.name)
print(p1.age)
        '''
#single parameter
'''
class person:
    def __init__(self,name,age=18):
        self.name=name
        self.age=age

p1=person('praveen')
p2=person('kumar',24)
print(p1.name,p1.age)
print(p2.name,p2.age)
print('hello my name is' + p1.name)
print('hello my age is ', p1.age)
        
        '''

"""class praveen:
    pass

p1=praveen()
p1.name='pk'
p1.age=19
p1.name='kumar'
p1.city='vizag'
p1.name='lavada'
print(p1.name)"""

'''class person:
    def __init__(self,name,age,city,state):
        self.name=name
        self.age=age
        self.city=city
        self.state=state
p1=person('praveen',13,'vsp','ap')
print('hello my name is ' + p1.city)

class vehicle:
    def __init__(self,company,model,version):
        self.company=company
        self.model=model
        self.version=version
    def myveh(self):
        print(f"my car name is,{self.company} and model is{self.model} the version is {self.version}")

car=vehicle('audi','corollel',118)
car.myveh()

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def mypk(abc):
        print('hello my name is '+ abc.name)
p1=person('satya ',33)
p2=person('sai',23)
p1.age=99
print(p1.age)'''

'''def greet(name,age):
    return f"hello my name is {name} and age is {age}"
msg=greet('pravven',33)
print(msg)
msg1=greet('kumar',34)
print(msg1)

def myfun(fruits):
    for fruit in fruits:
        print(fruit)
my_fruits=['apple','banana','orange']
#my_Fun={'a':'pk','b'':'rk','c':'dk'}
my_fun1=('pk','rk','sk')
myfun(my_fun1)
myfun(my_fruits)'''
def myfun(person ,name,age):
    print('name:',person["name"])
    print('age:',person['age'])
    return f"my name is {name},and age is{age}"

myfun1={"name":"praveen","age":78}
print(myfun1)
myfun('kumar',78,'kp')
print(myfun)