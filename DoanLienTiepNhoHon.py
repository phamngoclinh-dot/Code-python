t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = [1] * n
    for j in range(n):
        cnt = 1
        for k in range(j - 1, -1, -1):
            if a[k] <= a[j]: cnt += 1
            else: 
                b[j] = cnt
                break
            if k == 0: b[j] = cnt
    print(*b)