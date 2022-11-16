idx, ipt = input().split()

word = ""
for i in range(len(ipt)):
    if ipt[i] == "_" or ipt[i] == " ":
        continue
    elif i == 0:
        word += ipt[i].lower()
    elif ipt[i-1] == " " or ipt[i-1] == "_" or "A" <= ipt[i] <= "Z":
        word += " " + ipt[i].lower()
    else:
        word += ipt[i]

temp = ""
## 카멜 표기법
for i in range(len(word)):
    if word[i] == " ":
        continue
    if i != 0 and word[i-1] == " ":
        temp += word[i].upper()
    else:
        temp += word[i]

print(temp)
temp = ""

## 스네이크 표기법
for i in range(len(word)):
    if word[i] == " ":
        temp += "_"
    else:
        temp += word[i]

print(temp)
temp = ""

## 파스칼 표기법
for i in range(len(word)):
    if i == 0:
        temp += word[i].upper()
    elif word[i-1] == " ":
        temp += word[i].upper()
    elif word[i] != " ":
        temp += word[i]

print(temp)
