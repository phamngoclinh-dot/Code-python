import math
from collections import Counter

def ngto(n):
    if n < 2: return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return 0
    return 1

t = int(input())
a = list(map(int, input().split()))

count = Counter(a)  # đếm số lần xuất hiện của tất cả các số
b = set()  # để lưu số nguyên tố đã in

for num in a:
    if ngto(num) and num not in b:
        print(num, count[num])
        b.add(num)