import time
import copy
from numba import jit  # 加快代码运行速度

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
# 放不下下一个方块？


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


# 在剩余空位（列表x）中，判断以y为左上角时，剩余能否放下与basetile（列表z）一样大小的砖
def valid(x, y, z):
    
    tf = True
    for i in z:
        if not i + y in x:
            tf = False
    
    return tf


def tile(m, n ,a, b, empty, occ = []):

    if empty == []:  # 所有砖块填满
        return cases.append(occ)
    
    em = copy.deepcopy(empty)

    else:
        for k in basetile(m, n, a, b):

            i = 0  # 从空砖块列表的第一个开始
            while i < len(em):  # 如果存在i，使得可以填入以empty[i]为左上，bati[0]方向砖块
                e = em[i]
                if valid(em, e, k) == True: # 如果可以填入bati[0]方向砖块
                    occ.append(tuple(j + e for j in k))  # 填入砖块
                    for j in k:
                        em.remove(j + e)  # 空位置中删除填入的砖块
                    
                    tile(m, n, a, b, empty, occ)

                i += 1


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
        for i in cases:
            print(i)

    d = time.time()
    
    print(str(d - c) + ' sec')

if __name__ == "__main__":
    main()
