a = list(map(int, input().split()))
sum_ = sum(a)
std = sum_ // len(a)
diff = sum_ - std

print(sum_)
print(std)
print(diff)