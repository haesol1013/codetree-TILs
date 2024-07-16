import sys

input = sys.stdin.readline

# 입력
n, t = map(int, input().split())
l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))


# 회전
def rotate(arr1, arr2, arr3):
    length = len(arr1)
    target = arr1 + arr2 + arr3

    tmp = target[-1]
    for i in range(len(target)-1, 0, -1):
        target[i] = target[i-1]
    target[0] = tmp

    return target[:length], target[length:length*2], target[length*2:]


for _ in range(t):
    l, r, d = rotate(l, r, d)


# 출력
print(*l)
print(*r)
print(*d)