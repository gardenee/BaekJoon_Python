def ball_count(answer, guess):
    strike, ball = 0, 0
    for i in range(3):
        if answer[i] == guess[i]:
            strike += 1
        elif guess[i] in answer:
            ball += 1

    return strike, ball


possible_nums = set()

for a in range(1, 10):
    for b in range(1, 10):
        if a == b:
            continue
        for c in range(1, 10):
            if a == c or b == c:
                continue
            possible_nums.add(str(a)+str(b)+str(c))

for _ in range(int(input())):
    guess, strike, ball = map(int, input().split())
    temp = set()

    for num in possible_nums:
        result = ball_count(num, str(guess))
        if result[0] == strike and result[1] == ball:
            temp.add(num)

    possible_nums = temp

print(len(possible_nums))
