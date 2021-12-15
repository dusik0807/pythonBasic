class Dog:
    name = "두식"
    age = 2

    def bark(self):
        print('멍멍')

    def sit(self):
        print('앉는다.')

dog1 = Dog()

dog1.bark()


dog1.sit()
print(type(dog1))
print('''오늘은 날씨가 굉장히 좋고 기분이 좋습니다!!''')


class Dog:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
    
    def bark(self):
        print('멍멍')

    def sit(self):
        print('앉는다.')

dog1=Dog("두식",2)
dog2=Dog("다은",12)
print(dog1.name,dog1.age,)
print(dog2.name,dog2.age,)           

class Dog:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
    
    def bark(self):
        print('멍멍')

    def sit(self):
        print('앉는다.')

    def __str__(self):
        sentence ='이름:{},나이:{}'.format(self.name,self.age)
        return sentence

dog1=Dog("두식",2)
dog2=Dog("다은",12)
print(dog1)
print(dog2)     

result =0
def add(num):
    global result
    result+= num
    return result

print(add(3))
print(add(4))

class Calculator:
    def __init__(self):
        self.result =0
    def add(self,num):
        self.result += num
        return self.result
        
cal1=Calculator()
print(cal1.add(3))
print(cal1.add(4))

class Animal:
    def eat(self):
        print('먹는다')
    def move(self):
        print('움직인다')


class Dog(Animal):
    def bark(self):
        print('멍멍')
    def shake(self):
        print('꼬리를 흔든다')
dog=Dog()
dog.eat()
dog.move()
dog.bark()
dog.shake()
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print('먹는다')
    def move(self):
        print('움직인다')

class Dog(Animal):
    def __init__ (self,name,age,owner):
        super().__init__(name,age)
        self.owner=owner
    def bark(self):
        print('멍멍')
    def shake(self):
        print('꼬리를 흔든다')
    def __str__(self):
        sentence ='이름:{},나이:{},주인:{}'.format(self.name,self.age,self.owner)
        return sentence

dog= Dog('두식',2,'김다은')
print(dog)

