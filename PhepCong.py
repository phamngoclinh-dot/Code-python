import math
def ngto(n) :
    if n < 2: return False
    if n == 2 or n == 3 : return True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0 : return False
    return True
t = int(input())
for i in range(t):
    a = int(input())
    sum = 0
    for i in range(1,a) :
        if math.gcd(i, a) == 1: sum+=1
    if ngto(sum) == True :
        print("YES")
    else : 
        print("NO")
