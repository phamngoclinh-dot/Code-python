def Nguoc(n):
    x = ""
    for i in range(len(n)):
        x = n[i] + x
    return x   
t = int(input())
for i in range(t):
    n = input()
    j = 999
    ok = False
    sum = 0
    if int(n) % 7 == 0: 
        print(n)
        continue
    while j > 2:
        x = Nguoc(n)
        sum = int(n) + int(x)
        if sum % 7 == 0: 
            ok = True
            break
        n = str(sum)
        j -=1
    if ok == False: print(-1)
    else: print(sum)