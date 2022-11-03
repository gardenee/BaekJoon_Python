n = int(input())

dp = [0] * (n+2)
dp[1] = 1
dp[2] = 3

for i in range(3, n+2):
    dp[i] = (dp[i-2]*2)%10007 + dp[i-1]%10007
    dp[i] %= 10007

print(dp[n])
