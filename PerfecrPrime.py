import math
def ngto(n):
    if n < 2: return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return 0
    return 1
def nguoc(n):
    x = 0
    while n > 0:
        x = x * 10 + n % 10
        n //= 10
    return x
def tong(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
def ChuSo(n):
    while n > 0:
        if not ngto(n % 10): return 0
        n //= 10
    return 1
t = int(input())
for i in range(t):
    n = int(input())
    if ngto(n) and ngto(nguoc(n)) and ngto(tong(n)) and ChuSo(n) : print("Yes")
    else : print("No")