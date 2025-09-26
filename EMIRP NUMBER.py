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
t = int(input())
for i in range(t):
    n = int(input())
    a = [0] * 100001
    for i in range(12, n + 1):
        if ngto(i) and nguoc(i) <= n and ngto(nguoc(i)) and i != nguoc(i) and a[i] == 0 and a[nguoc(i)] == 0:
            print(i, nguoc(i), end = ' ')
            a[i] = 1
            a[nguoc(i)] = 1
    print()