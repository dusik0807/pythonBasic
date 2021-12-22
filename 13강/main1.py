class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        self.name
        print('{}가 먹는다'.format(self.name))
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

dog= Dog('코코',2,'홍길동')
print(dog)
dog.eat()

#print('''내 이름은 남도일 탐정이죠!무엇이든 도와드리겠습니다.반갑숩니다.내 이름은 코코 탐정이죠.''')
#a= input("오늘 당신이 먹을 음식은?")
#print (a)

#while True:
 #   퀴즈=6
  #  print("3+3= 무엇일까요?")
   # user = input('당신의 선택은?')
    #user = int(user)
 #   print(user)
#    if user < 6:
#        print("정답 보다 작네요")
 #   elif user > 6:
 #       print('정답보다 크네요')
 #   else:
 #       #user == 6:
#      print('정답입니다.')
 #       break

class Animal:
    def __init__(self,age):
        self.age=age
    def eat(self):
        print(' 먹는다')
    def move(self):
        print('움직인다')

class Dog(Animal):
    def __init__ (self,name,age):
        super().__init__(age)
        self.name=name
    def bark(self):
        print('멍멍')
    def shake(self):
        print('꼬리를 흔든다')
    def __str__(self):
        sentence ='이름:{},나이:{}'.format(self.name,self.age)
        return sentence
class Bird(Animal):
    def __init__(self,age):
        self.age=age

    def eat(self):
        print('새가 모이를 먹는다')

    def move(self):
        print('새가 몸을 움직인다')

animal=Animal(1)
animal.eat()
animal.move()

dog=Dog('코코',3)
dog.eat()
dog.move()

bird=Bird(1)
bird.eat()
bird.move()



dog= Dog('코코',2)
print(dog)
dog.bark()

dog2=Dog('두리',5)
print(dog2)

dog3=Dog('먼지',7)
print(dog3)
from main1 import *

dog=Dog('코코',2)
print(dog)

 
