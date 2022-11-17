import heapq

N, M = map(int, input().split())

INF = 101
bacon_nums = [[INF] * N for _ in range(N)]

for i in range(N):
    bacon_nums[i][i] = 0

friend = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    friend[A-1].append(B-1)
    friend[B-1].append(A-1)

heap = [[0, 0, 0]]
while heap:
    n, A, B = heapq.heappop(heap)
    if bacon_nums[A][B] < n:
        continue

    friend_friend = friend[B]
    for acquaintance in friend_friend:
        if bacon_nums[A][acquaintance] > n+1:
            bacon_nums[A][acquaintance] = n+1
            bacon_nums[acquaintance][A] = n+1
            heap.append([n+1, A, acquaintance])
            heap.append([n+1, acquaintance, A])
        if bacon_nums[B][acquaintance] > 1:
            bacon_nums[B][acquaintance] = 1
            bacon_nums[acquaintance][B] = 1
            heap.append([1, B, acquaintance])
            heap.append([1, acquaintance, B])

answer, name = 101, 0
for i in range(N):
    bacon_num = sum(bacon_nums[i])
    if answer > bacon_num:
        answer = bacon_num
        name = i+1

print(name)
