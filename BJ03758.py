from sys import stdin
import heapq

for _ in range(int(input())):
    n, k, t, m = map(int, input().split())
    score_log = dict()

    for i in range(m):
        team_id, problem_no, score = map(int, stdin.readline().split())
        score_log.setdefault(team_id, [[0]*k, 0, 0])
        score_log[team_id][0][problem_no-1] = max(score_log[team_id][0][problem_no-1], score)
        score_log[team_id][1] += 1
        score_log[team_id][2] = i

    ranking = []
    for team in score_log.keys():
        problems, try_cnt, submit_no = score_log[team]
        heapq.heappush(ranking, [-sum(problems), try_cnt, submit_no, team])

    for i in range(n):
        check = heapq.heappop(ranking)
        if check[3] == t:
            print(i+1)
