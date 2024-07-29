# 입력
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]


# 초기 설정
def initialize():
    dp[0][0] = grid[0][0]

    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + grid[0][i]

    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]


initialize()
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + grid[i][j]

print(dp[-1][-1])