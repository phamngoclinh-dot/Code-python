t = int(input())
for i in range(t):
    m, n = map(int, input().split())
    a = [[int(x) for x in input().split()] for x in range(m)]
    b = [[0] * m for _ in range(n)]
    # c = [[0] * n] * n
    for j in range(m):
        for k in range(n):
            b[k][j] = a[j][k]
    # print(*a)
    # print(*b)
    for j in range(m):
        for x in range(m):
            sum = 0
            for y in range(n):
                sum += a[j][y] * b[y][x]
            print(sum, end = ' ')
        print()