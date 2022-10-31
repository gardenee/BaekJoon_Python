import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = dict()
words = []
idx = 0

for _ in range(N):
    word = input().rstrip()
    n = len(word)
    if n < M: continue

    if word in dic:
        words[dic[word]][0] -= 1
    else:
        dic[word] = idx
        idx += 1
        words.append([-1, -n, word])

words.sort()
for word in words:
    print(word[2])
