# 입력
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 초기화
visited = [[False]*m for _ in range(n)]


# 범위 체크
def in_range(x, y):
    global n, m
    return 0 <= x < n and 0 <= y < m


# 이동 가능 여부 체크
def can_go(x, y):
    if not in_range(x, y):
        return False

    if visited[x][y] or not grid[x][y]:
        return False

    return True


# dfs
def dfs(x, y):
    pairs = [(1, 0), (0, 1)]
    for dx, dy in pairs:
        next_x, next_y = x + dx, y + dy
        if can_go(next_x, next_y):
            visited[next_x][next_y] = True
            dfs(next_x, next_y)


visited[0][0] = True
dfs(0, 0)

result = 1 if visited[n-1][m-1] else 0
print(result)