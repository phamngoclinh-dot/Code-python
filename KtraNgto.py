import math
def ngto(n):
    if n < 2: return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return 0
    return 1
m , n = map(int, input().split())
a = [[int(x) for x in input().split()] for x in range(m)]
for i in range(m):
    for j in range(n):
        if ngto(a[i][j]):
            print(1, end = ' ')
        else: 
            print(0, end = ' ')
    print()