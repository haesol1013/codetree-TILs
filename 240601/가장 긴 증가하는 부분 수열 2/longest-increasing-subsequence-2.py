import sys

input = sys.stdin.readline

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
idx = 0
while len(arr)>1 and idx < len(arr)-1:
    if arr[idx] > arr[idx+1]:
        arr.remove(arr[idx+1])
    else:
        idx += 1
print(len(arr))