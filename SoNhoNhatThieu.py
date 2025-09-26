n = int(input())
a = list(map(int, input().split()))
b = [0] * 30001
for i in range(len(a)):
    b[a[i]] = 1
for i in range(1, len(b)):
    if not b[i]:
        print(i)
        break
