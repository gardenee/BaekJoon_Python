N, K = map(int, input().split())
table = input()

answer = 0
for i in range(len(table)):
    if table[i] == 'H' or table[i] == '!':
        continue
    for j in range(max(0, i-K), min(N, i+K+1)):
        if table[j] == 'H':
            answer += 1
            table = table[:j] + '!' + table[j+1:]
            break

print(answer)
