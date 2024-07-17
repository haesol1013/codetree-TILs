# 입력
n, m, t = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
pos_list = [
    list(map(lambda x: x - 1, map(int, input().split())))
    for _ in range(m)
]


# 범위 체크
def can_go(x, y):
    global n
    return 0 <= x < n and 0 <= y < n


# 이동
def move(pos):
    global grid
    curr_x, curr_y = pos
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    max_val = 0
    max_pos = [0, 0]

    for dx, dy in zip(dxs, dys):
        next_x, next_y = curr_x + dx, curr_y + dy
        if can_go(next_x, next_y) and grid[next_x][next_y] > max_val:
            max_val = grid[next_x][next_y]
            max_pos = next_x, next_y

    return max_pos


# 반복
for _ in range(t):
    exist_pos = set()
    del_pos = set()
    
    # 구슬 하나씩 이동
    for i, pos in enumerate(pos_list):
        pos_list[i] = move(pos)
    
    # 중복 체크
    for i, pos in enumerate(pos_list):
        if pos not in exist_pos:
            exist_pos.add(pos)
        else:
            del_pos.add(pos)
    
    # 중복되지 않은 것만 체크
    pos_list = [pos for pos in pos_list if not pos in del_pos]

# 출력
print(len(pos_list))