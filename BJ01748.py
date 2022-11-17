N = str(input())

num = list(N)
num[0] = str(int(num[0])-1)
answer = ""
for n in num:
    answer += n
answer = (int(answer)+1) * len(num)

for i in range(1, len(num)):
    answer += 9 * 10 ** (i-1) * i

print(answer)
