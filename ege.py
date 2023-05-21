'''
from functools import lru_cache
@lru_cache(None)

def f(x, y):
    if x+y >= 41:#сумма камней после которой все ламается
        return 0
    if x > y:
        moves = [f(x, y+1), f(x, y+2), f(x, y+3), f(x, y*2), f(x+1, y), f(x+2, y), f(x+3, y)]
    if x < y:
        moves = [f(x, y + 1), f(x, y + 2), f(x, y + 3), f(x*2, y), f(x + 1, y), f(x + 2, y), f(x + 3, y)]
    if x==y:
        moves = [f(x, y + 1), f(x, y + 2), f(x, y + 3), f(x + 1, y), f(x + 2, y), f(x + 3, y)]
    lose = [i for i in moves if i <=0]
    if lose:
        result = -max(lose) + 1
    else:
        result = -max(moves)
    return result


for s in range(1, 36):
    print(s, f(s, 17))
#19 s + n * k * k = 61  k-во сколько раз умножить n- чило в одной из куч s - число камней в другой куче
#n+s*k*k=61
# Петя - положительные числа, Витя -ОТРИЦАТЕЛЬНЫЕ, f(9, s)-выводит на каком ходе кто выигрывает
'''

'''
def pr(x):
    for j in range(2, int(x**0.5)+ 1):
        if x % j == 0:
            return False
    return True
f = open('27-108a.txt').readlines()
ch2 = 60
s = []
for j in f:
    s.append(int(j))
sp = []
for i in range(ch2):
    cpr = 0
    cel = 0
    f = True
    ind = i
    sprov = []
    while f:
        for k in range(2, 9048 // 2 + 1):
            if s[ind] % k == 0:
                if pr(k):
                    if k not in sprov:
                        sprov.append(k)
                        cpr += 1
        cel += 1
        ind += 1
        if cpr >= 60:
            sp.append(cel)
            break
print(min(sp))
'''
'''
from itertools import *
a = set()
for n in range(18, 100):
    for i in product('123', repeat=n*3):
        s = ''.join(i)
        if s.count('1') == s.count('2') == s.count('3'):
            while '21' in s or '31' in s or '32' in s:

                if '21' in s:
                    s = s.replace('21', '12', 1)

                elif '31' in s:
                    s = s.replace('31', '13', 1)

                elif '32' in s:
                    s = s.replace('32', '23', 1)
    if len(s) > 50:
        if s[51] == '2':
            print(n*3)

            break
'''

'''
for p in range(7, 100):
    for y in range(p):
        for x in range(p):
            for z in range(p):
                a1 = y*p**2+4*p+y
                a2 = y*p**2+6*p+5
                a3 = x*p**3+z*p**2+2*p+3
                if a1+a2== a3:
                    print(x, y, z, p)
print(int('176', 9))
'''

'''
print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                f = ((x <= y) and (y <= w)) or (z == (x or y))
                if not f:
                    print(x, y, z, w)
'''

'''
def f(x, y):
    if x > y or x == 26:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x + 3, y)
print(f(1, 9) * f(9, 17))
'''