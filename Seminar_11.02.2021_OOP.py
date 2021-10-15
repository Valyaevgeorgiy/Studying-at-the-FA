class Sharp:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.screen = [['.'] * 20 for _ in range(20)]

    def print_screen(self):
        for line in self.screen:
            for symb in line:
                print(symb, end='')
            print()

    def draw(self):
        self.screen = [['.'] * 20 for _ in range(20)]
        self.screen[self.x][self.y] = 'R'
        self.print_screen()

    def dr_column(self):
        self.screen = [['.'] * 20 for _ in range(20)]
        for i in range(20):
            self.screen[i][self.y - 1] = '*'
            self.screen[i - 4][self.y - 1] = '*'
        self.print_screen()

    def dr_row(self):
        self.screen = [['.'] * 20 for _ in range(20)]
        self.screen[self.x] = '*' * 20
        self.print_screen()

    def dr_row_column(self):
        self.screen = [['.'] * 20 for _ in range(20)]
        for i in range(20):
            self.screen[i][self.y - 1] = '$'
            self.screen[self.x - 1][i] = '#'
        self.print_screen()

    def _str_(self):
        return f'Это точка с координатами ({self.x};{self.y})'

def num1():
    sh = Sharp(8, 4)
    return sh.x, sh.y
# num1()

def num2():
    sh = Sharp(8, 4)
    print('Вся матрица 20 х 20: ')
    Sharp.print_screen(sh)
    print()
    Sharp.draw(sh)
    print()
    print(Sharp._str_(sh))
num2()

def num3():
    sh = Sharp(8, 4)
    print('Перекрашенный столб и строка х и у: ')
    Sharp.dr_row_column(sh)
# num3()

class Sharp2:
    def __init__(self, x1, y1, a, b):
        self._x1 = x1
        self._y1 = y1
        self._a = a
        self._b = b
        self.screen = [['.'] * 20 for _ in range(20)]

    def print_screen(self):
        for line in self.screen:
            for symb in line:
                print(symb, end=' ')
            print()

    def square1(self):
        self.screen = [['.'] * 20 for _ in range(20)]
        for i in range(self._x1, self._x1 + self._a):
            for j in range(self._y1, self._y1 + self._b):
                self.screen[i - 1][j - 1] = '3'
        self.print_screen()

    def square2(self):
        self.screen = [['.'] * 20 for _ in range(20)]
        for i in range(self._x1, self._x1 + self._a + 1):
            self.screen[self._y1][i] = '3'
            self.screen[self._y1 + self._b + 1][i] = '3'
        for i in range(self._y1, self._y1 + self._b + 1):
            self.screen[i][self._x1] = '3'
            self.screen[i][self._x1 + self._a] = '3'
        self.print_screen()

    def _str_(self):
        return f'Это точка с координатами ({self._x};{self._y})'

def num4():
    print('Полный прямоугольник на матрице: ')
    P = Sharp2(2, 2, 7, 7)
    Sharp2.square1(P)
# num4()

def num5():
    print('Контур прямоугольника на матрице: ')
    P = Sharp2(2, 2, 7, 7)
    Sharp2.square2(P)
# num5()

class Square(Sharp2):
    def __init__(self, x, y, w):
        super().__init__(x, y, w, w)

    def __str__(self):
        return f'Это квадрат со стороной {self.w}'

def num6():
    print('Полный квадрат на матрице: ')
    P = Square(2, 2, 10)
    Square.square2(P)
# num6()

class Triangle(Sharp):
    def __init__(self, sh1, sh2, sh3):
        self.sh1 = sh1
        self.sh2 = sh2
        self.sh3 = sh3
        self.screen = [['.'] * 20 for _ in range(20)]

    def line(self, sh1, sh2):
        L = max(sh2.x - sh1.x, sh2.y - sh1.y) + 1
        dx = ((sh2.x - sh1.x) / L) if L != 0 else 0
        dy = ((sh2.y - sh1.y) / L) if L != 0 else 0
        y = sh1.y
        x = sh1.x
        for i in range(0, L):
            self.screen[round(y)][round(x)] = '*'
            y += dy
            x += dx
        self.screen[sh2.y][sh2.x] = '*'

    def draw(self):
        self.screen = [['_'] * 40 for _ in range(20)]
        self.line(self.sh1, self.sh2)
        self.line(self.sh1, self.sh3)
        self.line(self.sh2, self.sh3)
        self.print_screen()

    def area(self):
        from math import sqrt
        a = sqrt((self.sh1.x - self.sh2.x) ** 2 + (self.sh1.y - self.sh2.y) ** 2)
        b = sqrt((self.sh1.x - self.sh3.x) ** 2 + (self.sh1.y - self.sh3.y) ** 2)
        c = sqrt((self.sh2.x - self.sh3.x) ** 2 + (self.sh2.y - self.sh3.y) ** 2)
        p = (a + b + c) / 2
        s = sqrt(p * (p - a) * (p - b) * (p - c))
        return s

    def __str__(self):
        from math import sqrt
        a = sqrt((self.sh1.x - self.sh2.x) ** 2 + (self.sh1.y - self.sh2.y) ** 2)
        b = sqrt((self.sh1.x - self.sh3.x) ** 2 + (self.sh1.y - self.sh3.y) ** 2)
        c = sqrt((self.sh2.x - self.sh3.x) ** 2 + (self.sh2.y - self.sh3.y) ** 2)
        return f'Это треугольник с длинами сторон {a, b, c}'

    def right_Triangle(self):
        n = 0
        self.screen = [['.'] * 20 for i in range(20)]
        for i in range(self.sh2, self.sh3):
            for j in range(self.sh1 - n, self.sh1 + n + 1):
                self.screen[i][j] = '*'
            self.screen[i][self.sh1] = '*'
            n += 1
        self.print_screen()

def num7():
    print('Прямоугольный треугольник на матрице: ')
    tr = Triangle(Sharp(2, 2), Sharp(2, 15), Sharp(38, 2))
    tr.draw()
# num7()

def num8():
    print('Правильный треугольник на матрице: ')
    tr2 = Triangle(10, 3, 10)
    tr2.right_Triangle()
# num8()