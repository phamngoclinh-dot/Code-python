n = int(input())
a = [[int(x) for x in input().split()] for i in range(n)]
k = int(input())
sumTren = 0
sumDuoi = 0
for i in range(n):
    for j in range(n):
        if i + j < n - 1: sumTren += a[i][j]
        if i + j > n - 1: sumDuoi += a[i][j]
if abs(sumTren - sumDuoi) <= k: print("YES")
else : print("NO")
print(abs(sumTren - sumDuoi))