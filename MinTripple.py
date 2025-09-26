for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    if(n < 3):
        s = 0
        for x in a:
            s += x
        print(s)
    else:
        a.sort()
        s = a[0] + a[1]+ a[2]
        print(s)