class ThiSinh:
    def __init__(self, name, date, p1, p2, p3):
        self.name = name
        self.date = date
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def ChuanHoa(self):
        if self.date[1] == '/':
            self.date = "0" + self.date
        if self.date[4] == '/':
            self.date = self.date[:3] + "0" + self.date[3:]
        return self
a = ThiSinh(input(), input(), float(input()), float(input()), float(input()))
a.ChuanHoa()
sum = "{:.1f}".format(a.p1 + a.p2 + a.p3)
print(a.name, a.date, sum)
        