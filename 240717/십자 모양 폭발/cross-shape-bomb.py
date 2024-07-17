# 입력
n = int(input().strip())
matrix = [list(map(int, input().strip().split())) for _ in range(n)]
r, c = map(int, input().strip().split())
r -= 1
c -= 1


# 폭발
def explode(matrix, n, r, c):
    bomb_value = matrix[r][c]
    matrix[r][c] = 0
    for i in range(1, bomb_value):
        # up
        if r - i >= 0:
            matrix[r - i][c] = 0
        # down
        if r + i < n:
            matrix[r + i][c] = 0
        # right
        if c + i < n:
            matrix[r][c + i] = 0
        # left
        if c - i >= 0:
            matrix[r][c - i] = 0


# 중력 적용
def apply_gravity(matrix, n):
    for col in range(n):
        tmp = [matrix[row][col] for row in range(n) if matrix[row][col] != 0]
        for row in range(n-1, -1, -1):
            if tmp:
                matrix[row][col] = tmp.pop()
            else:
                matrix[row][col] = 0


explode(matrix, n, r, c)

apply_gravity(matrix, n)


for row in matrix:
    print(*row)