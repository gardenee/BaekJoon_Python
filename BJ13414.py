from sys import stdin

K, L = map(int, input().split())
answer = []
clicked = dict()

for i in range(L):
    _id = stdin.readline().rstrip()
    if _id in clicked:
        answer[clicked[_id]] = 0
    answer.append(_id)
    clicked[_id] = i

cnt = 0
for _id in answer:
    if _id != 0:
        print(_id)
        cnt += 1
    if cnt == K:
        break
