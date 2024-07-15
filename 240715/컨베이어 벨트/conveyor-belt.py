import sys

# 입력
n, t = map(int, sys.stdin.readline().split())
arr1 = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))


# 회전
def rotate(arr, n):
    tmp = arr[-1]

    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]

    arr[0] = tmp

    return arr


# t초 만큼 회전
merged_arr = arr1 + arr2
for _ in range(t):
    merged_arr = rotate(merged_arr, 2*n)
arr1, arr2 = merged_arr[:n], merged_arr[n:]

print(*arr1)
print(*arr2)