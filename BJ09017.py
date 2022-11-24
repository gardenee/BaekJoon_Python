import heapq

for _ in range(int(input())):
    N = int(input())
    record = dict()
    result = list(map(int, input().split()))
    for i in range(N):
        team = result[i]
        temp = record.get(team, 0)
        record[team] = temp + 1

    for key in record.keys():
        if record[key] < 6:
            while key in result:
                result.remove(key)

    record = dict()
    for i in range(len(result)):
        team = result[i]
        temp = record.get(team, [])
        temp.append(i+1)
        record[team] = temp

    ranking = []
    for key in record.keys():
        team = record[key]
        if len(team) >= 6:
            heapq.heappush(ranking, [sum(team[:4]), team[4], key])

    print(heapq.heappop(ranking)[2])
