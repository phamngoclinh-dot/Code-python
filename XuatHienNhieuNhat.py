t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * 1000001
    for j in range(len(a)):
        b[a[j]] += 1
    ok = True
    ans = 0
    for j in range(len(b)):
        if b[j] > n/2:
            ok = False
            ans = j
            break
    if ok: print("NO")
    else: print(ans)