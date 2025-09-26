import math
t = int(input())
for i in range(t):
    n = int(input())
    ans = 0
    for k in range(2, int(math.sqrt(2 * n)) + 1):
        if 2*n % k == 0 and (2*n/k - k + 1) % 2 == 0 and (2*n/k - k + 1)/2 >= 1: # n = k*(2a + k - 1) / 2
            ans += 1
    print(ans)