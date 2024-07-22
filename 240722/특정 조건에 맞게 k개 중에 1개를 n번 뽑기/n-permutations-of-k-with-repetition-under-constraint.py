# 입력
k, n = map(int, input().split())
arr = []


def choose(cnt=0):
    if cnt == n:
        print(*arr)
        return

    for i in range(1, k+1):
        if cnt != 0 and cnt >= n-1 and not [j for j in arr if j != i]:
            continue

        arr.append(i)
        choose(cnt+1)
        arr.pop()


choose()