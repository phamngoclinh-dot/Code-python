# t = int(input())
# for i in range(t):
#     n = input()
#     for i in n:
#         if 'a' <= i <= 'z': i = ' '
#     a = list(map(int, n.split(' ')))
#     min = 999999999
#     for i in a: 
#         if i < min: min = i
#     print(i)
t = int(input())
for _ in range(t):
    n = input()
    n = ''.join(' ' if 'a' <= ch <= 'z' else ch for ch in n)
    a = list(map(int, n.split()))
    min_val = max(a)
    print(min_val)
