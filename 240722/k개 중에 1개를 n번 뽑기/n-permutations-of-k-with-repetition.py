# 입력
k, n = map(int, input().split())
arr = []


def choose(cnt):
    if cnt == 0:
        print(*arr)
        return

    for i in range(1, k+1):
        arr.append(i)
        choose(cnt-1)
        arr.pop()


choose(n)