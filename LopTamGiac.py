from decimal import Decimal 
import math     
class Point:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def distance(self, other):
        return math.sqrt((self.tu - other.tu)**2 + (self.mau - other.mau)**2)
        # return "{:.3f}".format(x)
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        p3 = Point(Decimal(arr[4]), Decimal(arr[5]))
        a = p1.distance(p2)
        b = p2.distance(p3)
        c = p3.distance(p1)
        if a + b <= c or a + c <= b or b + c <= a:
            print("INVALID")
        else:
            print("{:.3f}".format(a + b + c))
        t -= 1