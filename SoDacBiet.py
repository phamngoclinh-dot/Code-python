t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = []
    while(k > 0):
        a.append(k % 2)
        k //= 2
    ans = 0
    for j in range(len(a) - 1, -1, -1):
        ans = (ans + a[j] * n ** j) % (10**9 + 7)
    print(ans)