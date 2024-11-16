# 해수면 높이 나누기
# 연속 판정

n = int(input())
arr = [int(input()) for _ in range(n)]

def count_bingsan(arr, h):
    over = False
    cnt = 0
    for bingsan in arr:
        if bingsan > h:
            over = True
        else:
            if over:
                cnt += 1
                over = False
    if over:
        cnt += 1
    return cnt

max_bingsan = 0
for h in range(min(arr), max(arr)+1):
    max_bingsan = max(max_bingsan, count_bingsan(arr, h))
print(max_bingsan)    