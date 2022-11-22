import random

gbb_list = ['가위', '바위', '보']

while True:
    gbb_in = input("가위(1)/바위(2)/보(3) 해당 번호를 선택하십시오.\n종료하려면 엔터키.:")
    try:

        input_num = int(gbb_in)

        print('')
        print('%s :' % gbb_list[input_num - 1], end = ' ')

        pc_num = random.randint(-3, -1)
        print('%s(PC)' % gbb_list[pc_num*(-1) - 1])


        rslt = input_num + pc_num
        if abs(rslt) > 1:
            rslt *= (-1)


        if rslt > 0:
            print('이기셨습니다.\n')
        elif rslt < 0:
            print('지셨습니다.\n')
        else:
            print('비기셨네요, 다시 입력하세요.\n')
    except:
        break
