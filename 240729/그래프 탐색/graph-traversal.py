# 입력
n, m = map(int, input().split())
start_end = [tuple(map(int, input().split())) for _ in range(m)]

# 초기화
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]


def dfs(vertex):
    global cnt
    visited[vertex] = True
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            cnt += 1
            dfs(curr_v)


for start, end in start_end:
    graph[start].append(end)
    graph[end].append(start)


cnt = 0
dfs(1)
print(cnt)