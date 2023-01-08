name = input()

cnt_alphabet = [0] * 26
for alphabet in name:
    cnt_alphabet[ord(alphabet)-65] += 1


answer, center = "", ""

for i in range(26):
    cnt = cnt_alphabet[i]

    if cnt % 2 == 1:
        if len(name) % 2 == 0 or center:
            answer = "I'm Sorry Hansoo"
            break
        else:
            center = chr(65+i)

    answer += chr(65+i) * (cnt//2)

if answer != "I'm Sorry Hansoo":
    answer = answer + center + answer[::-1]

print(answer)
