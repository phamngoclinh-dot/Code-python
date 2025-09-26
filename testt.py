import math
class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def rutgon(self):
        t = math.gcd(self.tu, self.mau)
        print(self.tu // t, self.mau//t, sep = '/')
arr = input().split()
p1 = PhanSo(int(arr[0]), int(arr[1]))
# p2 = PhanSo(int(arr[2]), int(arr[3]))
# p1.tong(p2)
p1.rutgon()