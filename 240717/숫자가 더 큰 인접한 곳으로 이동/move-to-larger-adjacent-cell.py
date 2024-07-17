# 입력
n, r, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
pos_list = []
r -= 1
c -= 1


# 범위 체크
def in_range(x, y):
    global n
    return 0 <= x <= n - 1 and 0 <= y <= n-1


while True:
    # 상하 좌우
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    curr_val = matrix[r][c]
    exist_bigger = False
    pos_list.append(curr_val)

    for dx, dy in zip(dxs, dys):
        curr_x, curr_y = r + dx, c + dy
        if in_range(curr_x, curr_y) and matrix[curr_x][curr_y] > curr_val:
            r, c = curr_x, curr_y
            exist_bigger = True
            break

    if not exist_bigger:
        break

print(*pos_list)