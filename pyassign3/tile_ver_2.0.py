import time
import copy
from numba import jit  # 加快代码运行速度


# problem: 输出时长边为横向


# 算法说明
# 对于没有被砖占有的编号最小的砖，放入一个以它为右上角的砖
# 判断放入的砖与已有的砖是否重叠


# 例：3*2地板放2*1砖块

# 规定编号方向从0开始，左到右，上到下，3*2的方格为
# | 0 | 1 | 2 |
# | 3 | 4 | 5 |

# 每一次从最小的数开始放入横砖块和竖砖块
# 1.
# | A | 1 | 2 |
# | A | 4 | 5 |  ... 1
# 
# | A | A | 2 |
# | 3 | 4 | 5 |  ... 2
# 
# 2.
# | A | B | B |
# | A | 4 | 5 |  ... 1-1
# 
# | A | B | 2 |
# | A | B | 5 |  ... 1-2
#
# | A | A | B |
# | 3 | 4 | B |  ... 2-1
#
# 3.
# | A | B | B |
# | A | C | C |  ... 1-1-1
#
# | A | B | C |
# | A | B | C |  ... 1-2-1
#
# | A | A | B |
# | C | C | B |  ... 2-1

# 递归终止条件
# 没有剩余空方块

# 递归发生条件
# 能放下一块砖


# 在x*y的地板上，方格0为左上角，长宽为z*t的矩形 
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
    if n[-1] < x*y and m != n:
        o.append(n)
    
    return o


# 在剩余空位（列表x）中，判断以y为左上角时，剩余能否放下与basetile（列表z）一样大小的砖，地板大小为t*u
# 4*3的地板上，不能用1块砖覆盖7和8
def valid(x, y, z, t, u):
    
    tf = True
    v = y % t - z[0] % t
    for i in z:
        if not (i + y in x and (i + y) % t - i % t == v):
            tf = False
    
    return tf


# [[0], [1], [2]], [[1], [0], [2]]
# 认定以上情况为同解
# 同解输出False，不同解输出True
def diffsol(x, y):

    z = True

    for i in x:
        if not i in y:
            z = False
    
    return not z


# 判断x与y中任何一个元素都不同解
# 满足输出True，不满足输出False
def issol(x, y):

    z = True

    for i in y:
        if diffsol(x, i) == False:
            z = False

    return z


def tile(m, n ,a, b, empty, occ = []):

    if empty == []: # and issol(occ, cases):   所有砖块填满
        return cases.append(occ)

    else:

        for v in range(len(basetile(m, n, a, b))): # 两个方向或一个方向
            empty1 = copy.deepcopy(empty)  # 深拷贝防止进行另一方向砖放入时empty和occ发生更改
            occ1 = copy.deepcopy(occ)

            k = basetile(m, n, a, b)[v]
            i = 0  # 从空砖块列表的第一个开始
            while i < len(empty1):  # 如果存在i，使得可以填入以empty[i]为左上，basetile[0]方向砖块
                e = empty1[i]
                # print('empty = ', empty, ', occ = ', occ, ', valid(', empty1, e, k, a, b, ') = ', valid(empty1, e, k, a, b))
                if valid(empty1, e, k, m, n) == True: # 如果可以填入bati[0]方向砖块
                    occ1.append(tuple(j + e for j in k))  # 填入砖块
                    for j in k:
                        empty1.remove(j + e)  # 空位置中删除填入的砖块
                
                    tile(m, n, a, b, empty1, occ1)  # 递归

                i += 1
            
            del empty1, occ1, i, k  # 删除变量加快运行速度
'''
        else:

            empty1 = copy.deepcopy(empty)
            occ1 = copy.deepcopy(occ)

            k = basetile(m, n, a, b)[1]
            i = 0  # 从空砖块列表的第一个开始
            while i < len(empty1):  # 如果存在i，使得可以填入以empty[i]为左上，basetile[1]方向砖块
                e = empty1[i]
                if valid(empty1, e, k, a, b) == True: # 如果可以填入bati[0]方向砖块
                    occ1.append(tuple(j + e for j in k))  # 填入砖块
                    for j in k:
                        empty1.remove(j + e)  # 空位置中删除填入的砖块

                    tile(m, n, a, b, empty1, occ1)

                i += 1
            
            del empty1, occ1, e, i, k
'''


def main():

    global cases

    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    cases = []

    c = time.time()
    
    m = max(x)
    n = min(x)
    a = max(y)
    b = min(y)
    em = list(range(m*n))


    if ((m*n) % (a*b)) != 0:
        print([])

    tile(m, n, a, b, em, occ = [])

    if cases == []:
        print([])
    else:
        diffcases = []
        for i in cases:
            if issol(i, diffcases) == True:
                diffcases.append(i)

    for i in diffcases:
        print(i)

    d = time.time()
    
    print(str(d - c) + ' sec')

if __name__ == "__main__":
    main()
