def exercise1():
    import time
    import keyboard
    import datetime as dt
    count = 0
    while not keyboard.is_pressed('esc'):
        char1 = dt.date.today()
        char2 = dt.datetime.today()
        if count % 20 == 0:
            with open('examples.log', mode='a+') as fipo:
                fipo.write(str(char1) + ' | ' + str(char2.strftime('%H:%M:%S')) + '\n')
            print(char1, char2.strftime('%H:%M:%S'))
        time.sleep(0.1)
        count += 1
    print('Programm stoped')
#exercise1()

def exercise2():
    import calendar
    a = calendar.LocaleHTMLCalendar(locale='Russian_Russia')
    with open('calendar.html', 'w+') as f:
        print(a.formatyear(2002, width=3), file=f)

#exercise2()

def exercise3():
    import random
    import datetime as dt

    s = set()
    a = []
    for i in range(100000):
        c = random.randint(0, 100000)
        while c in s:
            c = random.randint(0, 100000)
        s.add(c)
        a.append(c)
    c = int(input())
    i = 0
    print()
    d1 = dt.datetime.today()
    print(d1)
    while (a[i] != c):
        i += 1
    d2 = dt.datetime.today()
    print(d2)
    a.sort()
    l = 0
    r = 100000
    while r - l > 1:
        k = (l + r) // 2
        if a[k] >= c:
            l = k
        else:
            r = k
    d3 = dt.datetime.today()
    print(d3)
    print()
    print(d2 - d1, d3 - d2)

#exercise3()

def exercise4():
    import matplotlib.pyplot as plt
    import re

    pa = re.compile('\w+')

    def work_harder():
        dicty = {}
        with open('soulsdie.txt', mode='r', encoding = 'utf-8') as fi:
            f1 = str(fi.read().strip())
            x1 = pa.findall(f1)
            x2 = x1[0:100]
            for i in x2:
                if len(i) >= 4:
                    dicty[i] = x1.count(i)
            d3 = dict(sorted(dicty.items(), key=lambda x: x[1], reverse=True))
        return d3
    xs = work_harder()
    xs1 = {}
    c = 0
    for i, j in xs.items():
        xs1[i] = j
        c += 1
        if c == 10:
            break
    fig, ax = plt.subplots()
    ax.bar(xs1.keys(), xs1.values())
    ax.set_facecolor('white')
    fig.set_facecolor('white')
    fig.set_figwidth(12)
    fig.set_figheight(6)
    plt.show()

#exercise4()

def exercise5():
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import math


    plt.axis([0, 10, -1.5, 1.5])

    plt.title('Sin & Cos')
    plt.ylabel('F(x)')
    plt.xlabel('x')


    xs = []
    sin_vals = []
    cos_vals = []

    x = 0.0
    while x < 10.0:
        sin_vals += [math.sin(x)]
        cos_vals += [math.cos(x)]
        xs += [x]
        x += 0.1

    plt.plot(xs, sin_vals, color='blue', linestyle='solid',
            label='sin(x)')
    plt.plot(xs, cos_vals, color='red', linestyle='dashed',
             label='cos(x)')

    plt.legend(loc='upper left')
    plt.show()

#exercise5()
