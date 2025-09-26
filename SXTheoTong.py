def T(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
# def cmp(a, b):
#     if Tong(a) == Tong(b): return a < b
#     return Tong(a) < Tong(b)
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key = lambda x : (Tong(x), x))
    print(*a)