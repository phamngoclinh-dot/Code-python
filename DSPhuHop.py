t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    b.sort()
    ok = True
    for k in range(len(a)):
        if a[k] > b[k]:
            ok = False
            break
    if ok:
        print("YES")
    else : 
        print("NO")