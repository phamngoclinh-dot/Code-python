import math
def ngto(n):
    if n < 2: return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return 0
    return 1
t = int(input())
for i in range(t):
    s = input()
    x = ""
    for i in range(len(s) - 4, len(s)):
        x = x + s[i]
    x = int(x)
    if ngto(x) : print("YES")
    else: print("NO")