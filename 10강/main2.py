import random
com = random.randint(0,100)
print (com)

import random
com = random.randint(0,100)
count = 0
print(com)
print('0~100까지의 숫자를 입력하세요.')
while True:
    count = count + 1
    print("{0} 번째 도전!!".format(count))
    user = input('당신의 선택은?')
    user = int(user)
    print(user)
    if  user < 0:
        break
    elif user > com:
        print('정답보다 크네요')
    elif user < com:
        print('정답보다 작네요')
    elif  user < 0:

        break
    else:
        print('정답입니다.')
        break
