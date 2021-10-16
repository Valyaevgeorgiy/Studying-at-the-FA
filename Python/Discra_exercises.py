# 1)	постройте таблицу истинности
# 3)	составьте полином Жегалкина булевой функции f.
# Справка:
# v - конъюнкция - логическое сложение - or
# x1x3 - дизьюнкция - логическое сложение - and
# ⊕ - исключающее или - ^
# ¬ (она же вертикальная черта над буквой) - отрицание - not или ~
# → - импликация - >>
import pandas as pd
import itertools
import re


class Gob(object):
    pass


class Truths(object):
    def __init__(self, base=None, phrases=None, ints=True):
        if not base:
            raise Exception('Base items are required')
        self.base = base
        self.phrases = phrases or []
        self.ints = ints

        self.base_conditions = list(itertools.product([False, True],
                                                      repeat=len(base)))

        self.p = re.compile(r'(?<!\w)(' + '|'.join(self.base) + ')(?!\w)')

    def calculate(self, *args):
        # store bases in an object context
        g = Gob()
        for a, b in zip(self.base, args):
            setattr(g, a, b)


        eval_phrases = []
        for item in self.phrases:
            item = self.p.sub(r'g.\1', item)
            eval_phrases.append(eval(item))

        row = [getattr(g, b) for b in self.base] + eval_phrases
        if self.ints:
            return [int(item) for item in row]
        else:
            return row

    def __str__(self):
        t = str(self.base + self.phrases) + '\n'
        for conditions_set in self.base_conditions:
             t += str(self.calculate(*conditions_set)) + '\n'
        return t


# x1x2¬x3 v ¬x2x3 v ¬x1  - как в задании
# x1 and x2 and not x3 or not x2 and x3 or not x1 - как это выглядит на питоне
# по такому же принципу вводите свои данные (чтобы пострить таблицу истинности)
print('Таблица истинности: ')
table = Truths(['x1', 'x2', 'x3'],                                    # !!! Свои данные
               ['not x1', 'not x2', 'not x3',                         # !!! Свои данные
                'x1 and x2', 'x1 and x2 and not x3',                  # !!! Свои данные
                'not x2 and x3',                                      # !!! Свои данные
                'x1 and x2 and not x3 or not x2 and x3 or not x1'])   # !!! Свои данные
# получаем таблицу истинности


def get_pyr(v): # решение полинома жегалкина методом пирамиды паскаля
    res = []
    res.append(v)
    while len(v) != 1:
        tmp = []
        for i in range(0, len(v) - 1):
            tmp.append((v[i] + v[i + 1]) % 2)
        res.append(tmp)
        v = tmp
    res = list(map(lambda x: x[0], res))
    coop = ['1', 'x3', 'x2', 'x2x3', 'x1', 'x1x3', 'x1x2',  'x1x2x3']
    ret = []
    for i in range(len(res)):
        if res[i]:
            ret.append(coop[i])
    return ret


def get_zheg(table):
    nt = []
    ntn = []
    for i in str(table).split('\n'):
        nt.append(i[1:-1].split(','))
    nt[0] = list(map(lambda x: x[1:-1], nt[0]))
    nt[0] = list(map(lambda x: x[1:], nt[0][1:]))
    nt[0].insert(0, 'x1')
    for i in nt[1:-1]:
        ntn.append(list(map(lambda x: int(x), i)))
    ntn.insert(0, nt[0])
    pand = pd.DataFrame(ntn[1:], columns=ntn[0])
    df = pand.iloc[:, 0:3]
    df['F(x1,x2,x3)'] = pand.iloc[:, -1]
    zheg = get_pyr(list(df['F(x1,x2,x3)']))
    return ' ⊕ '.join(zheg)


print('Полином Жегалкина: ', get_zheg(table))
zh = Truths(['x1', 'x2', 'x3'])
# for i in zh[1:]:
print('Таблица истинности для полинома Жегалкина: \n', zh)
# затем по полиному жегалкина сделать четвертый столбец в таблице с
# результатом функции
# 1 ⊕ 1 = 0
# 1 ⊕ 0 = 1
# 0 ⊕ 0 = 0
# 0 ⊕ 1 = 1