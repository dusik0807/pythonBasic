list=[1,5,3,6]
print(list[3])

list=[1,5,3,6]
print(list[1:3])
print(list[2:])
print(list[:2])

과목=['국어','수학','영어','과학']
print(과목)

rainbow=['빨강','주황','노랑','초록','파랑','남색','보라']
first_color=rainbow[0]
print('무지개의 첫번째 색은 {}이다'.format(first_color))
first_color=rainbow[6]
print('무지개의 마지막 색은 {}이다'.format(first_color))

list=[1,5,3,6]
list.append(8)
print(list)

list=[1,5,4,3,6]
list.insert(4,7)
print(list)

my_variable=[]


list1=[1,2,3]
list.append(4)
print(list)

list=[1,2,3,5]
list.insert(3,4)
print(list)

list1=[1,2,3]
list2=[4,5,6]
list3=list1+list2
print(list3)

list1=[1,2,3]
del list[1]
print(list)

list1=[1,2,3]
list1.remove(2)
print(list1)

list1=[1,2,3]
list[1]=10
print(list)

movie_rank=['아바타','어벤져스','타이타닉','명량','겨울왕국']
print(movie_rank)

t1=(1,2,'a','b')
#t1[0]='c'

음식=('떡볶이','햄버거','피자','김밥')
print(음식)


rainbow=('빨강','주황','노랑','초록','파랑','남색','보라')
first_color=rainbow[0]
print('무지개의 첫번째 색은 {}이다'.format(first_color))
first_color=rainbow[6]
print('무지개의 마지막 색은 {}이다'.format(first_color))

t=(1,2,3,4,5,6,7,8,9,10)
print(t*10)

t=(1,2,3,4,5,6,7,8,9,10,)
t2=t*10
print(t2)
print(len(t2))


number=2
while number < 6:
    number=number+1
    print(number)
    print("-------")

for number in range(1,10):
    string='{}*{}={}'.format(3,number,3*number)
    print(string)


점수=int(input('몇 점인가요?'))
print(점수)
if 점수 <=60:
    print("합격입니다.")
else:
    print("불합격입니다.")

number=2
while number < 6:
    number=number+1
    print(number)
