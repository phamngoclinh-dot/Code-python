import math
def ngto(n):
    if n < 2: return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 : return 0
    return 1

a, b = map(int, input().split())
arr = []
for i in range(2, 100000):
    if ngto(i) : 
        arr.append(i)
arr2 = []
arr2.append(b)
for i in range(1,a + 1):
    arr2.append(arr2[i - 1] + arr[i - 1])
print(*arr2)