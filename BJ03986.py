answer = 0

for _ in range(int(input())):
    stack = []
    ipt = input()

    for word in ipt:
        if not stack:
            stack.append(word)
            continue

        if stack[-1] != word:
            stack.append(word)
        else:
            stack.pop()

    if not stack:
        answer += 1

print(answer)
