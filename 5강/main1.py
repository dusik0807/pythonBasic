print('''안녕하세요!반갑습니다.''')
def a():
    print("안녕하세요")
a()
print('''꽈베기 마이쪄요우''')

def message():
    print("A")
    print("B")

message()
print("C")
message()

print("")

def say1(name):
    string='안녕하세요?'+name+'님?'
    return string

def say2(name):
    string='안녕하세요?'+name+'님?'
    print(string) 

name="뽀로로"
say1(name)
say2(name)

name=input("당신의 이름은?")
print(name)

age=input('당신의 나이는?')
print(age)

print('당신은{}이고{}살입니다.'.format(name,age))

print('당신은'+name+'이고'+str(age)+'살입니다.')

mine=input('가위 바위 보 중 하나를 내주세요>')
print('mine:',mine)

date=input('오늘 날짜:')
print('오늘의 날짜는',date,'입니다.')

date='2021/10/20'
year=date[0:4]
month=date[5:7]
day=date[8:10]
print('년:',year)
print('월:',month)
print('일:',day)
