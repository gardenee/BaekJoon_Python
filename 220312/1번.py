def solution(money, costs):
    ref = [1, 5, 10, 50, 100, 500]
    dic = {}
    for i in range(len(ref)):
        dic.setdefault(ref[i], costs[i] / ref[i])

    answer = 0
    while money != 0:
        for k, v in dic.items():
            if v == min(dic.values()):
                answer += (money // k) * costs[ref.index(k)]
                money = money % k
                dic[k] = 100000
                break

    return answer
