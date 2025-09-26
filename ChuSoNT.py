import math
def ngto(n):
    if n < 2 : return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return 0
    return 1
def check1(n):
    if ngto(len(n)): return 1
    return 0
def check2(n):
    cnt = 0
    for i in range(len(n)):
        if ngto(int(n[i])): cnt+=1
    if cnt > len(n) - cnt : return 1
    return 0
t = int(input())
for i in range(t):
    n = input()
    if check1(n) and check2(n): print("YES")
    else : print("NO")