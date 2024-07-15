import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_sum = 0
for i in range(n-2):
    for j in range(n-2):
        sum_ = sum(arr[i][j:j+3]
                   + arr[i+1][j:j+3]
                   + arr[i+2][j:j+3])
        max_sum = max(max_sum, sum_)
print(max_sum)