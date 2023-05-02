from random import randint


def generate_numbers():

    numbers = []
    while len(numbers) < 4:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)

    print("\n0과 9 사이의 서로 다른 숫자 4개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    print("\n숫자 4개를 하나씩 차례대로 입력하세요.")

    guess = []
    while len(guess) < 4:
        new_num = int(input("{}번째 숫자를 입력하세요: ".format(len(guess) + 1)))

        if new_num < 0 or new_num > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")

        elif new_num in guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")

        else:
            guess.append(new_num)

    return guess


def get_score(guess, solution):
    bull_count = 0
    cow_count = 0
    
    i = 0
    while i < 4:
        if guess[i] == solution[i]:
            bull_count += 1

        elif guess[i] in solution:
            cow_count += 1

        i += 1

    return bull_count, cow_count


ANSWER = generate_numbers()
tries = 0
print(ANSWER)

while True:
    user_guess = take_guess()
    tries += 1

    b, c = get_score(user_guess, ANSWER)
    print(f"Bull: {b}, Cow: {c}")

    if b == 4:
        break


print("축하합니다. {}번 만에 숫자 4개의 값과 위치를 모두 맞추셨습니다.".format(tries))
