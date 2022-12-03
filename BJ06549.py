while True:
    ipt = list(map(int, input().split()))
    if ipt == [0]:
        break

    stack = []
    answer = 0

    for h in ipt[1:]:
        answer, cnt = max(answer, h), 0
        curr = [h, 1]

        while stack:
            if stack[-1][0] >= h:
                prev = stack.pop()
                cnt += prev[1]
                answer = max(answer, cnt * prev[0])
            else:
                break

        curr[1] += cnt
        answer = max(answer, h * curr[1])
        stack.append(curr)

    cnt = 0
    for i in range(len(stack) - 1, -1, -1):
        cnt += stack[i][1]
        answer = max(answer, cnt * stack[i][0])

    print(answer)
