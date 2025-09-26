t = int(input())
for i in range(t):
    m, n = map(int, input().split())
    a = [[int(x) for x in input().split()] for x in range(m)]
    b = [[int(x) for x in input().split()] for x in range(3)]
    ans = 0
    for j in range(m - 2):
        for k in range(n - 2):
            for x in range(3):
                for y in range(3):
                    ans += a[j + x][k + y] * b[x][y]
    print(ans)    