while True:
    a,b,c,d = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and d == 0: break
    ans = 0
    while a != b or b != c or c != d:
        tmp = a
        a = abs(a - b)
        b = abs(b - c)
        c = abs(c - d)
        d = abs(d - tmp)
        ans += 1
    print(ans)
