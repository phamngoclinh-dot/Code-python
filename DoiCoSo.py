t = int(input())
for i in range(t):
    k = int(input())
    n = input()
    b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    sum = 0
    for i in range(len(n) - 1, -1, -1):
        sum += int(n[i]) * (2 ** (len(n) - 1 - i))
    a = []
    while sum > 0:
        a.append(b[sum % k])
        sum //= k
    a.reverse()
    print(*a, sep = '', end = '')
    print()
