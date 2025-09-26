import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def dis(self,other):
        s=(self.x-other.x)**2+(self.y-other.y)**2
        return math.sqrt(s)
class Triangle:
    def __init__(self,p1,p2,p3):
        self.a=p1.dis(p2)
        self.b=p2.dis(p3)
        self.c=p3.dis(p1)
    def check(self):
        if self.a+self.b<=self.c or self.a+self.c<=self.b or self.b+self.c<=self.a: return False
        return True
    def perimeter(self):
        s= self.a+self.b+self.c
        return s

if __name__=='__main__':
    a = []
    t = int(input())
    for x in range(t):
        a += [float(i) for i in input().split()]
    i = 0
    for index in range(t):
        p1=Point(a[i+0],a[i+1])
        p2=Point(a[i+2],a[i+3])
        p3=Point(a[i+4],a[i+5])
        tri=Triangle(p1,p2,p3)
        if (not tri.check()): print('INVALID')
        else:
            print(f'{tri.perimeter():.3f}')
        i+=6