# 입력
n, m, k = map(int, input().split())
matrix = [
    list(map(int, input().split()))
    for _ in range(n)
]
k -= 1
start, end = k, k+m
curr_row = 0


# 다음 행 확인
def is_empty(arr):
    return sum(arr) == 0


for _ in range(n-1):
    if is_empty(matrix[curr_row+1][start:end]):
        curr_row += 1
    else:
        break

# 채우기
for i in range(start, end):
    matrix[curr_row][i] = 1

# 출력
for row in matrix:
    print(*row)