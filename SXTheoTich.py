def Tich(n):
    tich = 1
    while n > 0:
        tich *= n % 10
        n //= 10
    return tich

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key = lambda x : (Tich(x), x))
    print(*a)