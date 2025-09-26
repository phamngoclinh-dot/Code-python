t = int(input())
for i in range(t):
    n, d = map(int, input().split())
    a = list(int(x) for x in input().split())
    for i in range(d, len(a)):
        print(a[i], end =' ')
    for i in range(d):
        print(a[i], end = ' ')
    print()