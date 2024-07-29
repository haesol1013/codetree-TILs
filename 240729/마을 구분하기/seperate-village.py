# 입력 및 초기화
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]


# 범위 체크
def in_range(x, y):
    global n
    return 0 <= x < n and 0 <= y < n


def bfs(x, y):
    global cnt
    pairs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in pairs:
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny]:
            cnt += 1
            visited[nx][ny] = True
            bfs(nx, ny)


result = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j]:
            cnt = 1
            visited[i][j] = True
            bfs(i, j)
            result.append(cnt)

print(len(result))
for i in sorted(result):
    print(i)