n, m, x = map(int, input().split())
check = [False]* (n + 1)
adj = [[] for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
def dfs(k):
    check[k] = True
    for i in adj[k]:
        if not check[i]:
            dfs(i)

dfs(x)
cnt = 0
for i in range(1, n + 1):
    if not check[i]:
        cnt+=1
        print(i)
if cnt == 0: print(0)