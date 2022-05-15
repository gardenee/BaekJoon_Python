Line = list(input().rstrip())
answer = 0
temp = 0
curr = ""
T = 0

for l in Line:
    if l == "+":
        if T == 1:
            temp += int(curr)
        else:
            answer += int(curr)
        curr = ""
    elif l == "-":
        if T == 1:
            temp += int(curr)
            answer -= temp
            temp = 0
        else:
            T = 1
            answer += int(curr)
        curr = ""
    else:
        curr += l

if T == 1:
    temp += int(curr)
    answer -= temp
else:
    answer += int(curr)

print(answer)
