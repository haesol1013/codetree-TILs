# 입력
n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


# 현재 숫자의 위치
def get_curr_num_pos(num):
    global grid
    curr_pos = [0, 0]

    for idx, row in enumerate(grid):
        if num in row:
            curr_pos = [idx, row.index(num)]

    return curr_pos


def can_go(x, y):
    global n
    return 0 <= x < n and 0 <= y < n


# 인접 칸 중 가장 큰 수가 있는 위치
def get_max_num_pos(x, y):
    global grid
    dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
    dys = [0, 1, 1, 1, 0, -1, -1, -1]
    max_val = 0
    max_pos = [0, 0]

    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx, y + dy
        if can_go(next_x, next_y) and grid[next_x][next_y] > max_val:
            max_val = grid[next_x][next_y]
            max_pos = next_x, next_y

    return max_pos[0], max_pos[1], max_val


for _ in range(m):
    for i in range(1, n**2+1):
        curr_x, curr_y = get_curr_num_pos(i)
        max_x, max_y, max_val = get_max_num_pos(curr_x, curr_y)
        grid[curr_x][curr_y], grid[max_x][max_y] = max_val, i

for row in grid:
    print(*row)