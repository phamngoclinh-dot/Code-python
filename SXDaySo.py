t = int(input())
for i in range(t):
    n , k = map(int, input().split())
    a = [int(x) for x in input().split()]
    b = []
    for j in a:
        if j < 0: 
            b.append(j)
    idx = -1
    x = max(a)
    for j in range(len(a)):
        if a[j] == x:
            idx = j
            break
    for j in range(idx):
        if a[j] >= 0:
            b.append(a[j])
    b.append(k)
    for j in range(idx, len(a)):
        if a[j] >= 0:
            b.append(a[j])
    print(*b)