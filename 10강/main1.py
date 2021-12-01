#import random
#print('임의의 두 숫자가 주어집니다.더하기 빼기 값을 구하세요.')

#num1= random.randint(0,100)
#num2= random.randint(0,100)

#print('숫자 1 : {0},숫자 2 :{1}'.format(num1,num2))
#com = num1+num2
#count = 0
#while True:
 #   count = count + 1
 #   print("두 수의 더하기 값은?({} 번째 도전)".format(count))
  #  user = input('당신의 답은?')
   # user = int(user)
  #  print(user)
 #   
 #   if user > com:
 #      print('정답보다 크네요')
  #  elif user < com:
  #      print('정답보다 작네요')
   # else:
    #    print('정답입니다.')
     #   break
while True:
    user=int(input())

    if  user < 0:
        break
    elif 81<= user <=100:
        print("A등급")
    elif 61<= user <=80:
        print("B등급")
    elif 41<= user <=60:
        print("C등급")
    elif 21<= user <=40:
        print ("D등급")
    else: 
        0<= user <=20
        print("E등급")

movie_rank=("아바타,어벤져스,타이타닉,명량,겨울왕국")
