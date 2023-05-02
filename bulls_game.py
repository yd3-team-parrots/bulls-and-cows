import random
import ranimport random

def bullsAndCows():
    value = ''
    while True:
        if len(value) == 4:
            break
        ck = str(random.randint(1, 9))
        if ck not in value:
            value+=ck

    n=0
    while True:
        bulls = 0
        cows = 0
        num=input("숫자를 입력:")
        n += 1
        if len(num) != 4 or num.isdigit() is False:
            print("error")
            n = n - 1
        else:
            if num==value:
                print("정답입니다. 총 입력한 횟수:%d"%n)
                bb=1
                break
            for i in range(4):
                if num[i] == value[i]:
                    bulls += 1
            for j in range(4):
                for k in range(4):
                    if num[j]==value[k]:
                        cows+=1
                        if num[j]==value[j]:
                            cows-=1

            print("%dB %dC 입력한 횟수 %d"%(bulls,cows,n))
        if n==10:
            print("기회를 다 사용했습니다")
            print(value)
            bb=1
            break


def main():
    bullsAndCows()
    while True:
        con=input("계속 하시겠습니까?:y/n")
        if con =='y':
            bullsAndCows()
        elif con=='n':
            break
        else:
            print("error")
main()
