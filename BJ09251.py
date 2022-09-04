X = input()
Y = input()
dp = [0] * (len(X))

for i in range(len(Y)):
    n = 0
    for j in range(len(X)):
        if n < dp[j]:
            n = dp[j]
        elif X[j] == Y[i]:
            dp[j] = n+1

print(max(dp))
