import random
# 컴퓨터가 뽑는다.
def computer_select_4number():
  num_list = []
  while len(num_list)<4 :
    temp = random.randint(1,9)
    if temp not in num_list:
      num_list.append(temp)
  return num_list

def user_select_4number():
  num_list = list(map(int,input("4자리 숫자를 입력해주세요 : ").split(" ")))
  return num_list

def find_bulls_cows(computer_ ,user_):
  cows= 0
  bulls = 0
  for i, j in zip(computer_ , user_):
    if i == j:
      bulls += 1
    else:
      if j in computer_number:
        cows += 1
  return bulls, cows

if __name__ == "__main__":
  computer_number = computer_select_4number()
  print(computer_number)
  while True:
    user_number = user_select_4number()
    bulls , cows = find_bulls_cows(computer_number, user_number)
    if bulls == 4:
      print(f"정답입니다. : {computer_number}")
      break
    else:
      print(f"Bulls:{bulls} , cows:{cows}")

