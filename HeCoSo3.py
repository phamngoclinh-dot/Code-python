def check(n):
    for i in n:
        if i >= '0' and i <= '9':
            if int(i) > 2: return 0
        else : return 0
    return 1
t = int(input())
for i in range(t):
    s = input()
    if check(s): print("YES")
    else : print("NO")