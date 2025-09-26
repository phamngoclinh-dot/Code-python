n = int(input())
d = {}
for i in range(n):
    a = [x for x in input().split()]
    if a[3] == "IN":
        if a[4] not in d:
            d[a[4]] = 0
        if int(a[2]) == 5:
            d[a[4]] += 10000
        if int(a[2]) == 7:
            d[a[4]] += 15000
        if int(a[2]) == 2:
            d[a[4]] += 20000
        if int(a[2]) == 29:
            d[a[4]] += 50000
        if int(a[2]) == 45:
            d[a[4]] += 70000
for i in d:
    print(f"{i}: {d[i]}")
    