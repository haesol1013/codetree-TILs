# 입력
k, n = map(int, input().split())
arr = []


def choose(cnt=0):
    if cnt == n:
        print(*arr)
        return

    for i in range(1, k+1):
        if cnt >= 2 and arr[-1] == i and arr[-2] == i:
            continue

        arr.append(i)
        choose(cnt+1)
        arr.pop()


choose()