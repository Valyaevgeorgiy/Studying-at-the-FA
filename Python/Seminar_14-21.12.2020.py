def exercise1():
    lst = [i for i in range(0, 20, 2)]
    for j in range(len(lst)):
        print(lst[j], end=' ')

#exercise1()

def exercise2():
    n = input('Введите что-нибудь: ')
    n1 = n.split()
    n2 = ''.join(n1)
    n3 = list(set(n2))
    print(' '.join(n3))

#exercise2()

def exercise3():
    import winsound
    winsound.Beep(300, 400)
    print('game over')

#exercise3()