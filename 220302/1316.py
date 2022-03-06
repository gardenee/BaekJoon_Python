ans = 0

for _ in range(int(input())):
    change = []
    word = input()
    change.append(word[0])
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            change.append(word[i+1])

    if len(change) == len(set(change)):
        ans += 1

print(ans)
