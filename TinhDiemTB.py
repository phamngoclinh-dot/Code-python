n = int(input())
a = list(map(float, input().split()))
cnt = 0
sum = 0
for i in range(len(a)):
    if a[i] != max(a) and a[i] != min(a):
        sum += a[i]
        cnt+= 1
print("{:.2f}".format(sum/cnt))