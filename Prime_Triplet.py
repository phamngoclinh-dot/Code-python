pri = [True] * 100005
pri[0] = pri[1] = False
p = 2
while p * p <= 100000:
    if pri[p]:
        for i in range(p * p, 100001, p):
            pri[i] = False
    p+=1
t = int(input())
for i in range(t):
    n = int(input())
    res = 0
    for k in range(2, n):
        if (pri[k] and pri[k + 2] and pri[k + 6]) and k + 6 < n:
            res += 1
        if (pri[k] and pri[k + 4] and pri[k + 6]) and k + 6 < n:
            res += 1
    print(res)