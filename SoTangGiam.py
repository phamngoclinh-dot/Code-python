t = int(input())
for i in range(t):
    n = input()
    j = 0
    while j < len(n) - 1 and n[j] < n[j + 1] :
        j+=1
    if j == 0 or j == len(n) - 1: 
        print("NO")
        continue
    while j < len(n) - 1 and n[j] > n[j + 1]:
        j+=1
    if len(n) < 3:
        print("NO")
        continue
    if j == len(n) - 1: print("YES")
    else: print("NO")