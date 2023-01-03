def star(n):
    if n == 1:
        return ["*"]

    answer = ["*" * (4 * (n-1) + 1), "*" + " " * (4 * (n-1) - 1) + "*"]

    prev = star(n-1)
    for line in prev:
        answer.append("* " + line + " *")

    answer += ["*" + " " * (4 * (n-1) - 1) + "*", "*" * (4 * (n-1) + 1)]

    return answer


answer = star(int(input()))
for line in answer:
    print(line)
