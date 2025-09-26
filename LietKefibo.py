t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    f = [0]*93
    f[1] = 1
    for i in range(2, 93):
        f[i] = f[i - 1] + f[i - 2]
    for i in range(a, b + 1):
        print(f[i], end = ' ')
    print()