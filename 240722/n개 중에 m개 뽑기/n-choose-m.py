# 입력
n, m = map(int, input().split())
arr = []


def permutation(curr_num=1, cnt=0):
    if curr_num == n+1:
        if cnt == m:
            print(*arr)
        return

    arr.append(curr_num)
    permutation(curr_num+1, cnt+1)
    arr.pop()

    permutation(curr_num+1, cnt)


permutation()