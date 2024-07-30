# 입력
n = int(input())
visited = [0, 0, 1, 1] + [0]*(n-3)

for i in range(4, n+1):
    if visited[i-2]:
        visited[i] += visited[i-2]
    if visited[i-3]:
        visited[i] += visited[i-2]

print(visited[n])