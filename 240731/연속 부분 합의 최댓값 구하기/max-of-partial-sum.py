# 입력
n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n

# 초기화
dp[0] = arr[0]

# dp
for i in range(1, n):
    dp[i] = max(dp[i-1] + arr[i], arr[i])

print(max(dp))