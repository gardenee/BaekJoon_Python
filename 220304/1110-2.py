m = int(input())
n = -1
answer = 0

while m != n:
    if n == -1:
        n = m
    n = (n%10)*10 + (n//10 + n%10)%10
    answer += 1

print(answer)