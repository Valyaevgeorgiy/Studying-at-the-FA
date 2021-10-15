import numpy as np
import random
import matplotlib as mpl
import matplotlib.pyplot as plt

def beginexercise():
    a = np.array([20, 30, 40, 50])
    b = np.arange(4) ** 3

    print('a =', a)
    print('b =', b)
    print(a[2:])
    a[:2:2] = 10
    print(a)

    print(10*np.sin(a))
    print(a < 35)

    rg = np.random.default_rng()
    ff = rg.random((2, 3))
    print(ff)

#beginexercise()

def exercise1():
    a = list(np.ones(1))
    a += list(np.zeros(10))
    a += list(np.ones(1))
    return a

#exercise1()

def exercise2():
    s1 = np.array([random.randint(0, 1) for i in range(20)])
    a = 0
    a1 = 0
    for i in s1:
        if i == 1:
            a += 1
        else:
            a1 += 1
    if a1 > a:
        for j in s1:
            if (i == 1) and (a1 != 1):
                i = 0
    return (s1)

#exercise2()

def exercise3():
    x = np.array([i for i in range(100)])
    y = np.array([i ** 2 for i in range(100)])

    dpi = 80
    fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi))
    mpl.rcParams.update({'font.size': 10})
    plt.axis([0, 100, 0, 5000])
    plt.title('Массивчик')
    plt.ylabel('F(x)')
    plt.xlabel('x')
    plt.plot(x, y)
    plt.show()

#exercise3()

def exercise4():
    qs = np.random.randint(1, 100, (10, 10))
    y = []
    j = 0
    for i in range(len(qs)):
        y += [qs[i][j]]
        j += 1
    print(qs)
    print(y)
    x = [i + 1 for i in range(len(y))]
    dpi = 80
    fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi))
    mpl.rcParams.update({'font.size': 10})
    plt.axis([0, 100, 0, 10])
    plt.title('Массивчик')
    plt.ylabel('F(x)')
    plt.xlabel('x')
    plt.plot(x, y)
    plt.show()

#exercise4()