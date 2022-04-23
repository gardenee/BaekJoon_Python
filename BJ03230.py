N, M = map(int, input().split())
ranking = []
n = 0

for i in range(1, N+1):
    ranking.insert(int(input())-1, i)

final_list = ranking[:M+1]
final_rank = []

for i in range(M-1, -1, -1):
    final_rank.insert(int(input())-1, final_list[i])

print(final_rank[0])
print(final_rank[1])
print(final_rank[2])
