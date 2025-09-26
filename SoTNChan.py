def TN(n):
    for i in range(len(n)//2):
        if n[i] != n[len(n) - 1- i] : return False
    return True
def ktra(n):
    cnt = 0
    for i in n:
        if int(i) % 2 != 0: return False
    if len(n) % 2 != 0 : return False
    return True
t = int(input())
for i in range(t):
    n = int(input())
    for j in range(n):
        s = str(j)
        if TN(s) and ktra(s):
            print(s, end = ' ')
    print()
