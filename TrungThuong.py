t = int(input())
for i in range(t):
    n = int(input())
    l = []
    for i in range(n):
        l.append(int(input()))
    b = [0] * 1001
    for i in range(len(l)):
        b[l[i]] += 1
    max1 = 0
    cnt = 0
    for i in range(1, len(b)):
        if b[i] > cnt :
            cnt = b[i]
            max1 = i
    print(max1)
