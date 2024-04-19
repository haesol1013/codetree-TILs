a = int(input())
arr = []
for n in range(1, a+1):
    cond1 = n % 2 == 0 and n % 4 != 0
    cond2 = (n//8) % 2 == 0
    cond3 = (n % 7) < 4
    if not (cond1 or cond2 or cond3):
        arr.append(n)
print(*arr)