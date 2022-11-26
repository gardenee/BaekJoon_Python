min_dp = ["", "", "1", "7", "4", "2", "6", "8", "10", "18", "22", "20"]

for i in range(len(min_dp), 101):
    min_dp.append(min_dp[-7] + "8")
    if i % 7 == 3:
        min_dp[i] = "200" + "8" * ((i-17)//7)

for _ in range(int(input())):
    num = int(input())

    if num % 2 == 0:
        max_answer = "1" * (num//2)
    else:
        max_answer = "7" + "1" * ((num-3)//2)

    print(int(min_dp[num]), int(max_answer))
