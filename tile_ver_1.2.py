import random
import math
import copy
import time
from numba import jit

# 算法说明
# 构造所有长度为m*n，元素为0到m*n-1且不重复的数列，总数为(m*n)!个
# 对每一个数列，切成a*b长度的多个小数列，检验每一个a*b长度的数列是否能形成一个矩形


# 将一个长度为y的列表x按长度为z重新构造list，并对其排序 cut([1, 2, 4, 3], 2) => [[1, 2], [3, 4]]
def cut(x, z):

    y = len(x)

    n = []

    for i in range(int(y/z)):
        m = x[z*i:z*(i+1)]
        m.sort()
        n.append(m)

    return n


# 在x*y的地板上，构造包含方格0，长宽为z*t的矩形 
# basetile(4, 3, 3, 2) == [[0, 1, 2, 4, 5, 6], [0, 1, 4, 5, 8, 9]]
def basetile(x, y, z, t):

    m = []
    n = []
    o = []

    for i in range(z):
        for j in range(t):
            m.append(i*x + j)
            n.append(j*x + i)
    
    m.sort()
    n.sort()

    if m[-1] < x*y:
        o.append(m)
    if n[-1] < x*y:
        o.append(n)
    
    return o


# 在x*y的地板上，判断z中的元素是否能形成t*u的矩形
def istile(x, y, z, t, u):

    m = basetile(x, y, t, u)
    v = copy.deepcopy(z)

    for i in v:
        k = i[0]
        for j in range(len(i)):
            i[j] = i[j] - k
    
    j = True
    for i in v:
        j = j and (i in m)
    
    return j

# [[0], [1], [2]], [[1], [0], [2]]
# 认定以上情况为同解
# 同解输出False，不同解输出True
def diffsol(x, y):

    z = True

    for i in x:
        if i in y:
            z = False
    
    return z

# 判断x与y中任何一个元素都不同解
# 满足输出True，不满足输出False
def issol(x, y):

    z = True

    for i in y:
        if diffsol(x, i) == False:
            z = False

    return z

# 输出所有合法解
def valid(m, n, a, b):

    s = m*n
    
    case = []  # 遍历所有情况储存在集合内
    validcase = []  # 合法的情况

    while len(case) != math.factorial(m*n):
        
        seq = random.sample(range(s), s)

        if not seq in case:
            case.append(seq)
            i = copy.deepcopy(seq)
            i = cut(i, a*b)
                       
            if istile(m, n, i, a, b) == True:
                if issol(i, validcase) == True:
                    validcase.append(i)

    return validcase


def main():

    c = time.time()

    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    m = max(x)
    n = min(x)
    a = max(y)
    b = min(y)


    if ((m*n) % (a*b)) != 0:
        print([])

    else:
        print(valid(m, n, a, b))

    d = time.time()

    print(str(d - c) + ' sec')


if __name__ == '__main__':
    main()