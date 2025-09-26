t = int(input())
for j in range(t):
    n = input()
    a = []
    cnt = 0
    res = []
    for i in n:
        if i == '(':
            cnt+=1
            a.append(cnt)
            res.append(str(cnt))
        elif i == ')':
            res.append(str(a.pop()))
    print(" ".join(res))
    