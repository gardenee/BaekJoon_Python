N = int(input())
budgets = list(map(int, input().split()))
M = int(input())

total, answer = 0, 0
start, end = 0, 100001

while start < end:
    mid = (start+end)//2
    sum_budget, max_budget = 0, 0
    for budget in budgets:
        if budget <= mid:
            sum_budget += budget
            max_budget = max(max_budget, budget)
        else:
            sum_budget += mid
            max_budget = mid

    if sum_budget > M:
        end = mid
    else:
        if total < sum_budget:
            total = sum_budget
            answer = max_budget
        start = mid+1

print(answer)
