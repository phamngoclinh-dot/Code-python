def SoDep(n):
    for i in range(len(n) - 2):
        if n[i] != n[i + 2]: return 0
        if n[i] == n[i + 1]: return 0
    return 1
t = int(input())
for i in range(t):
    n = input()
    if SoDep(n): print("YES")
    else : print("NO")