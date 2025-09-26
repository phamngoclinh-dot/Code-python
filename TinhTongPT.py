t = int(input())
for i in range(t):
    n = int(input())
    sum = 0
    if n % 2 == 0:
        for i in range(2, n + 1, 2):
            sum += float(1/i)
        print("%.*f" %  (6, sum))
    else:
        for i in range(1, n + 1, 2):
            sum += float(1/i)
        print("%.*f" %  (6, sum))