n = int(input())
fibo_li = [0, 1, 1] + [-1]*(n-2)


def fibo(n):
    if fibo_li[n] != -1:
        return fibo_li[n]
    else:
        return fibo(n-1) + fibo(n-2)


print(fibo(n))