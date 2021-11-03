from typing import MutableMapping


print("{}".format(2))

#data=input("입력값: ")
hit=0
while hit<10:
    hit=hit+1
    print("나무를 {}번 찍었습니다.".format(hit))

hit=0
while hit<10:
    hit=hit+1
    print("나무를 {}번 찍었습니다.".format(hit))
    if hit == 10:
        print("나무가 넘어졌습니다.")
	

hit=0
while hit<10:
    hit=hit+1
    print("나무를 {}번 찍었습니다.".format(hit))
    if hit == 10:
        print("나무가 넘어졌습니다.")
    elif hit ==8:
        print("나무가 곧 넘어갈것 같습니다.")
    elif hit ==1:
        print("나무가 꿈쩍도 하지 않습니다.")

prompt="""
100을 임력하면 종료가 되는 프로그램입니다.
100.종료
Enter number:"""



#number=0
#while number != 100:
   # print(prompt)
    #number = int(input())


number=0
while number <100:
    number=number+1
    print(number)

number=1
while number <=100:
    print(number)
    number=number+1

number=0
max=int(input())
while number < max:
    number = number+1
    print(number)

#while 3<5:
#    print("3은 5보다 작다.")

if 3<5:
    print("3은 5보다 작다.")

print("숫자 두 개 작은수부터 입력해주세요.")
min = int(input())
max = int(input())
while min <= max:
    print(min)
    min =min+1

number=3
while number <=6:
    print(number)
    number=number+1

for number in range(1,21):
    print(number)

for number in range(10,101):
    print(number)

for number in range(1,10):
    string= '{}*{}={}'.format(2,number,2*number)
    print(string)

for number in range(1,10):
    string= '{}*{}={}'.format(9,number,9*number)
    print(string)

단= int(input('구구단을 출력합니다. 몇 단인지 입력해주세요'))
for number in range(1,10):
    string= '{}*{}={}'.format(단,number,단*number)
    print(string)
