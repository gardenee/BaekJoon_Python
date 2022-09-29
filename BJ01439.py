word = input()
cnt, ref = 0, -1

for w in word:
    if w != ref:
        cnt += 1
        ref = w

print(cnt//2)
