n = int(input())
arr = [0] * (n + 1)
for i in range(n - 1):
    a , b = map(int, input().split())
    arr[a] += 1
    arr[b] += 1
cnt1, cnt2 = 0, 0
for i in range(len(arr)):
    if arr[i] == 1: cnt1 +=1
    if arr[i] == n - 1: cnt2 +=1
if cnt1 == n - 1 and cnt2 == 1: print("Yes")
else :print("No")