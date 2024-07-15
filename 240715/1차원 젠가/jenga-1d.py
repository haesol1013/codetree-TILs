import sys

# 입력
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())


def delete(arr, s, e):
    # s부터 e범위 까지 False로
    arr[s-1:e] = [False]*(e-s+1)

    # tmp arr initialize
    tmp = [False]*len(arr)

    # tmp arr 채우기
    tmp_idx = len(arr) - 1
    for val in arr:
        if val:
            tmp[tmp_idx] = val
            tmp_idx -= 1

    return [val for val in tmp if val]


arr = delete(arr, s1, e1)
arr = delete(arr, s2, e2)

print(len(arr))
for i in arr:
    print(i)