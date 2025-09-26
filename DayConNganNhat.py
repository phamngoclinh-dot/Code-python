import math
t = int(input())
for u in range(t):
    n , k = map(int, input().split())
    a = [int(x) for x in input().split()]
    res = 1000000009
    for i in range(n):
        g = 0
        for j in range(i, n):
            g = math.gcd(g, a[j])
            if g < k: break
            if g % k != 0: break
            if g == k:
                res = min(res, j - i + 1)
                break
    if res != 1000000009: print(res)
    else: print(-1)
    