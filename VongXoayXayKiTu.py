t = int(input())
a = []
for i in range(t):
    a.append(input())
def Dich(x, s):
    if s == x: return 0
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s == x: 
            return i + 1
    return -1
res = 10**6
ok = True
for i in range(t):
    cnt = 0
    for j in range(t):
        if i != j:
            num = Dich(a[i], a[j])  
            if num == -1:
                ok = False
                break
            else:
                cnt += num

    res = min(res, cnt)
if ok: print(res)
else: print(-1)