import numpy as np
import random


"""
樹形図データをJavaScriptに渡すための文字列（カンマ区切り）にして返す
Chart.jsだと線でうまくつなげないのでshowLineは空(false)
"""


class GrTree:

    def __init__(self, lpx=320.0, lpy=380.0):
        self.tx = []
        self.ty = []
        self.tx.append(lpx)
        self.ty.append(lpy)

    def __move(self, leng, lpx, lpy, angle):
        x = lpx + leng * np.cos(angle * np.pi / 180.0)
        y = lpy + leng * np.sin(angle * np.pi / 180.0)
        self.tx.append(x)
        self.ty.append(y)
        return x, y

    def draw(
            self,
            leng=120.0,
            lpx=320.0,
            lpy=380.0,
            angle=90.0,
            scale=0.7):
        if(leng >= 5.0):
            self.tx.append(lpx)
            self.ty.append(lpy)
            lpx, lpy = self.__move(leng, lpx, lpy, angle)
            self.draw(leng * scale, lpx, lpy, angle + 20.0)
            self.draw(leng * scale, lpx, lpy, angle - 20.0)
        return ','.join(map(str, self.tx)), ','.join(map(str, self.ty))


class GrFern:

    def __init__(self):
        self.tx = [0]
        self.ty = [0]

    def __tran_1(self, p):
        x = p[0]
        y = p[1]
        x1 = 0.85 * x + 0.04 * y
        y1 = -0.04 * x + 0.85 * y + 1.6
        return x1, y1

    def __tran_2(self, p):
        x = p[0]
        y = p[1]
        x1 = 0.2 * x - 0.26 * y
        y1 = 0.23 * x + 0.22 * y + 1.6
        return x1, y1

    def __tran_3(self, p):
        x = p[0]
        y = p[1]
        x1 = -0.15 * x + 0.28 * y
        y1 = 0.26 * x + 0.24 * y + 0.44
        return x1, y1

    def __tran_4(self, p):
        # x = p[0]
        y = p[1]
        x1 = 0
        y1 = 0.16 * y
        return x1, y1

    def get_index(self):
        prob = [0.85, 0.07, 0.07, 0.01]
        r = random.random()
        c = 0
        sump = []
        for p in prob:
            c += p
            sump.append(c)
        for item, sp in enumerate(sump):
            if(r <= sp):
                return item
        return len(prob) - 1

    def __tran(self, p):
        trans = [self.__tran_1, self.__tran_2, self.__tran_3, self.__tran_4]
        tindex = self.get_index()
        t = trans[tindex]
        x, y = t(p)
        return x, y

    def draw(self, n=10000):
        x1 = 0
        y1 = 0
        for i in range(n):
            x1, y1 = self.__tran((x1, y1))
            self.tx.append(x1)
            self.ty.append(y1)
        return ','.join(map(str, self.tx)), ','.join(map(str, self.ty))


class GrGasket():

    def __init__(self):
        self.tx = [0]
        self.ty = [0]

    def __tran_1(self, p):
        x = p[0]
        y = p[1]
        x1 = 0.5 * x
        y1 = 0.5 * y
        return x1, y1

    def __tran_2(self, p):
        x = p[0]
        y = p[1]
        x1 = 0.5 * x + 0.5
        y1 = 0.5 * y + 0.5
        return x1, y1

    def __tran_3(self, p):
        x = p[0]
        y = p[1]
        x1 = 0.5 * x + 1.0
        y1 = 0.5 * y
        return x1, y1

    def __get_index(self):
        prob = [0.333, 0.333, 0.333]
        r = random.random()
        c = 0
        sump = []
        for p in prob:
            c += p
            sump.append(c)
        for item, sp in enumerate(sump):
            if(r <= sp):
                return item
        return len(prob) - 1

    def __tran(self, p):
        trans = [self.__tran_1, self.__tran_2, self.__tran_3]
        tindex = self.__get_index()
        t = trans[tindex]
        x, y = t(p)
        return x, y

    def draw(self, n=5000):
        x1 = 0
        y1 = 0
        for i in range(n):
            x1, y1 = self.__tran((x1, y1))
            self.tx.append(x1)
            self.ty.append(y1)
        return ','.join(map(str, self.tx)), ','.join(map(str, self.ty))


class GrSnow():

    def __init__(self):
        self.tx = []
        self.ty = []

    def __move(self, leng, lpx, lpy, angle):
        x = lpx + leng * np.cos(angle * np.pi / 180.0)
        y = lpy - leng * np.sin(angle * np.pi / 180.0)
        self.tx.append(x)
        self.ty.append(y)
        return x, y

    def __turn(self, angle, chg_angle):
        ang = angle + chg_angle
        ang2 = ang - ang + ang % 360.0
        return ang2

    def __koch(self, leng, lpx, lpy, angle):
        leng_t = 0.0
        px = lpx
        py = lpy
        ang = angle
        if(leng <= 60.0):
            px, py = self.__move(leng, px, py, ang)
        else:
            leng_t = leng / 3.0
            px, py = self.__koch(leng_t, px, py, ang)
            ang = self.__turn(ang, 60.0)
            px, py = self.__koch(leng_t, px, py, ang)
            ang = self.__turn(ang, -120.0)
            px, py = self.__koch(leng_t, px, py, ang)
            ang = self.__turn(ang, 60.0)
            px, py = self.__koch(leng_t, px, py, ang)
        return px, py

    def draw(self, r0=1000.0):
        x0 = 0.0
        y0 = 0.0
        sx = x0 - r0 * np.sqrt(3.0) / 2
        sy = y0 - r0 / 2
        self.tx.append(sx)
        self.ty.append(sy)
        leng = r0 * np.sqrt(3.0)
        angle = 0.0
        for i in range(3):
            sx, sy = self.__koch(leng, sx, sy, angle)
            angle = self.__turn(angle, -120.0)
        return ','.join(map(str, self.tx)), ','.join(map(str, self.ty))


class GrCcurve:
    def __init__(self):
        self.tx = [1.0]
        self.ty = [2.0]

    def __move(self, lpx, lpy, dx, dy):
        self.tx.append(lpx + dx)
        self.ty.append(lpy + dy)

    def draw(self, st_len=10.0, lpx=0.0, lpy=0.0, dx=2.0, dy=0.0):
        leng = st_len
        if(leng <= 0.0):
            self.__move(lpx, lpy, dx, dy)
        else:
            self.draw(leng - 1.0,
                      self.tx[-1],
                      self.ty[-1],
                      (dx + dy) / 2,
                      (dy - dx) / 2)
            self.draw(leng - 1.0,
                      self.tx[-1],
                      self.ty[-1],
                      (dx - dy) / 2,
                      (dy + dx) / 2)
        return ','.join(map(str, self.tx)), ','.join(map(str, self.ty))
