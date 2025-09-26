class SoPhuc:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def Tong(self, other):
        return SoPhuc(self.re + other.re, self.im + other.im)

    def Tich(self, other):
        re_new = self.re * other.re - self.im * other.im
        im_new = self.re * other.im + self.im * other.re
        return SoPhuc(re_new, im_new)

    def __str__(self):
        return f"{self.re} + {self.im}i"
    
t = int(input())
for i in range(t):
    a = [int(x) for x in input().split()]
    A = SoPhuc(a[0], a[1])
    B = SoPhuc(a[2], a[3])
    C0 = A.Tong(B)
    C = C0.Tich(A)
    D = C0.Tich(C0)
    print(C, D, sep=', ')
