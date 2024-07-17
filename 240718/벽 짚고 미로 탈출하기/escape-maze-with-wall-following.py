# 입력
n = int(input())
start_pos = tuple(map(lambda x: x-1, map(int, input().split())))
grid = [
    list(input())
    for _ in range(n)
]

# 변수 설정
# 1. 시작 방향
start_direct = "r"
# 2. 방향에 따른 앞
front = {"r": (0, 1), "d": (1, 0), "l": (0, -1), "u": (-1, 0)}
# 3. 방향에 따른 대각선
diagonal = {"r": (1, 1), "d": (1, -1), "l": (-1, -1), "u": (-1, 1)}


# 탈출 가능성 체크
def is_out(pos: tuple) -> bool:
    global grid, n
    x, y = pos
    return x < 0 or x >= n or y < 0 or y >= n


# 시작과 같은 상태인지 확인
def is_same_state():
    global start_pos, curr_pos, start_direct, curr_direct
    return curr_pos == start_pos and curr_direct == start_direct


# 벽 유뮤 확인
def is_wall(pos: tuple) -> bool:
    global grid
    x, y = pos
    return grid[x][y] == "#"


# 회전 -> 시계 | 반시계
def rotate(direction: str, clockwise=False) -> str:
    directions = ["r", "d", "l", "u"]
    curr_idx = directions.index(direction)
    if clockwise:
        return directions[curr_idx+1] if curr_idx < 3 else directions[0]
    else:
        return directions[curr_idx-1] if curr_idx > 0 else directions[3]


#초기 설정
curr_pos = start_pos
curr_direct = start_direct
cnt = 0

# 이동
while True:
    # 현 위치에서 방향을 고려했을 때 앞 위치
    front_pos = tuple(map(sum, zip(curr_pos, front[curr_direct])))
    # 현 위치에서 방향을 고래했을 때 대각선 위치
    diagonal_pos = tuple(map(sum, zip(curr_pos, diagonal[curr_direct])))

    # 격자 앞 -> 탈출
    if is_out(front_pos):
        cnt += 1
        print(cnt)
        break

    # 벽 앞 -> 반시계 회전
    if is_wall(front_pos):
        curr_direct = rotate(curr_direct)

        if is_same_state():
            print(-1)
            break

        continue

    # 벽 이어짐 -> 방향 그대로 전진
    if is_wall(diagonal_pos):
        cnt += 1
        curr_pos = front_pos
        # 다시 돌아왔는지 확인

    # 벽 안 이어짐 -> 벽의 오른쪽 90도로 이동
    else:
        cnt += 2
        curr_pos = diagonal_pos
        curr_direct = rotate(curr_direct, clockwise=True)

    # 이동 후, 현 위치와 시작 위치 and 현 방향과 시작 방향 모두 같다면 종료

    if is_same_state():
        print(-1)
        break