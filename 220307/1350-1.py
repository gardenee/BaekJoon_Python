N = int(input())
files = list(map(int, input().split()))
memory = int(input())
num = 0

for f in files:
    if f > 0:
        if f % memory == 0:
            num += f//memory
        else:
            num += f//memory + 1

print(num * memory)
