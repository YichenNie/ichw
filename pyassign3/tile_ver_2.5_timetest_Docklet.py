## %%timeit

import time
import copy


'''
tile.py 铺砖问题
用a*b的砖铺满m*n的地板，给出所有的铺法
并选择其中一种画出示意图


例：3*2地板放2*1砖块
input: m, n, a, b用空格分割每个参数，如3 2 2 1

规定编号方向从0开始，左到右，上到下，3*2的方格为

| 0 | 1 | 2 |
| 3 | 4 | 5 |

print: 
0 [(0, 3), (1, 4), (2, 5)]
1 [(0, 3), (1, 2), (4, 5)]
2 [(0, 1), (2, 5), (3, 4)]
Amount of the solutions = 3  # 解的数量
0.0030007362365722656 sec  # 给出所有解需要的时间
'''


# 算法说明
# 对于没有被砖占有的编号最小的砖，放入一个以它为左下角的砖（横砖或竖砖）
# 判断放入的砖与已有的砖是否重叠

# 1.
# | A | 1 | 2 |  ... 1
# | A | 4 | 5 |
# 
# | A | A | 2 |  ... 2
# | 3 | 4 | 5 |
# 
# 2.
# | A | B | B |  ... 1-1
# | A | 4 | 5 |
# 
# | A | B | 2 |  ... 1-2
# | A | B | 5 |
#
# | A | A | B |  ... 2-1
# | 3 | 4 | B |
#
# 3.
# | A | B | B |  ... 1-1-1
# | A | C | C |
#
# | A | B | C |  ... 1-2-1
# | A | B | C |
#
# | A | A | B |  ... 2-1-1
# | C | C | B |

# 递归终止条件
# 没有剩余空方块


# 在x*y的地板上，方格0为右下角，长宽为z*t的矩形 
# basetile(4, 3, 3, 2) == [(0, 1, 2, 4, 5, 6), (0, 1, 4, 5, 8, 9)]
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

    if m[-1] < x*y and len(list(set(m))) == len(m):  # 不加最后一个判断条件，运行(2, 3, 2, 3)给出(0, 1, 2, 2, 3, 4)
        o.append(m)
    if n[-1] < x*y and m != n and len(list(set(n))) == len(n):
        o.append(n)
    
    return o


# 地板大小为t*u，在剩余空位（列表x）中
# 判断以y为左下角时，剩余能否放下与basetile（列表z）一样大小的砖，
def valid(x, y, z, t, u):
    
    tf = True
    v = y % t - z[0] % t
    for i in z:
        if not (i + y in x and (i + y) % t - i % t == v):  # 4*3的地板上，不能用1块砖覆盖7和8
            tf = False
    
    return tf


# 填砖
# empty: 空方格，occ: 被砖占有的方格
def tile(m, n ,a, b, empty, occ=[]):

    if empty == []:  #  所有砖块填满时停止递归
        return sols.append(occ)

    else:

        for v in bati:  # 两个方向或一个方向
            empty1 = copy.deepcopy(empty)  # 深拷贝防止进行另一方向砖放入时empty和occ发生更改
            occ1 = copy.deepcopy(occ)
            e = empty1[0]

            if valid(empty1, e, v, m, n) == True: # 如果可以填入bati[0]方向砖块
                
                occ1.append(tuple(j + e for j in v))  # 填入砖块
                for j in v:
                    empty1.remove(j + e)  # 空位置中删除填入的砖块
            
                tile(m, n, a, b, empty1, occ1)  # 递归  

                
def main():

    global sols,bati

    m, n, a, b = 6,6,4,1
    bati = basetile(m, n, a, b)

    em = list(range(m*n))
    if a < b:
        a, b = b, a  # 交换顺序，使得竖向的砖在basetile的第0个

    sols = []
    c=time.time()
    tile(m, n, a, b, em, occ=[])
    d=time.time()
    if sols != []:
        print('Amount of the solutions = ' + str(len(sols)))
        print('Time needed = ' + str(d-c) + ' sec')
        with open('tile_docklet_' + str(m) + '_' + str(n) + '_' + str(a) + '_' + str(b) + '.txt','w') as txt:
            txt.write('m, n, a, b = ' + str(m) + ', ' + str(n) + ', '
                      + str(a) + ', ' + str(b) + '\n')
            txt.write('len(sols) = ' + str(len(sols)) + '\n')
            txt.write('time=' + str(d-c) + ' sec' + '\n\n')
            txt.write(str(sols) + '\n' * 4)

        
if __name__ == "__main__":
    main()

