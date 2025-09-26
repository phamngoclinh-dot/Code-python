import math
t = int(input())
for i in range(t):
    n = int(input())
    x = n
    sum = 0
    while n > 0:
        sum += math.factorial(n % 10)
        n //= 10
    if sum == x: print("Yes")
    else: print("No")
