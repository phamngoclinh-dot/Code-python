t = int(input())
a = [int(x) for x in input().split()]
ans = 0
for i in range(len(a)):
    for j in range(len(a)):
        if i < j and a[i] > a[j]: ans += 1
print(ans)
