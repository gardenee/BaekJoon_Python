def star(n):
    if n == 1:
        return ["*"]

    rtn = ["*" * (4*n-3), "*"]

    prev = star(n-1)
    for i in range(len(prev)):
        if i == 0:
            rtn.append("* " + prev[0] + "**")
        elif i == 1:
            rtn.append("* " + prev[1] + " " * (4*n-7) + "*")
        else:
            rtn.append("* " + prev[i] + " *")

    if n == 2:
        for _ in range(2):
            rtn.append("")
            for i in range(4*n-3):
                if i % 2 == 0:
                    rtn[-1] += "*"
                else:
                    rtn[-1] += " "

    rtn += ["*" + " " * (4*n-5) + "*", "*" * (4*n-3)]

    return rtn


answer = star(int(input()))
for i in range(len(answer)):
    print(answer[i])
