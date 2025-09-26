import math
def tong(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum
def ngto(n):
    if n < 2: return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return 0
    return 1
t = int(input())
for i in range(t):
    n = input()
    if ngto(tong(n)): print("YES")
    else : print("NO")        