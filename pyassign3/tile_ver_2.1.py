import time
import copy
import turtle

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
def valid(x, y, z, t, u):
    
    tf = True
    v = y % t - z[0] % t
    for i in z:
        if not (i + y in x and (i + y) % t - i % t == v):  # 4*3的地板上，不能用1块砖覆盖7和8
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


# 填砖
# empty: 空方格，occ: 被砖占有的方格
def tile(m, n ,a, b, empty, occ = []):

    if empty == []:  #  所有砖块填满时停止递归
        return sols.append(occ)

    else:

        for v in range(len(basetile(m, n, a, b))):  # 两个方向或一个方向
            empty1 = copy.deepcopy(empty)  # 深拷贝防止进行另一方向砖放入时empty和occ发生更改
            occ1 = copy.deepcopy(occ)

            k = basetile(m, n, a, b)[v]
            i = 0
            while i < len(empty1):  # 如果存在i，使得可以填入以empty[i]为左上，basetile[0]方向砖块
                e = empty1[i]
                # print('empty = ', empty, ', occ = ', occ, ', valid(',
                #       empty1, e, k, a, b, ') = ', valid(empty1, e, k, a, b))
                if valid(empty1, e, k, m, n) == True: # 如果可以填入bati[0]方向砖块
                    occ1.append(tuple(j + e for j in k))  # 填入砖块
                    for j in k:
                        empty1.remove(j + e)  # 空位置中删除填入的砖块
                
                    tile(m, n, a, b, empty1, occ1)  # 递归

                i += 1


# 绘制骨架部分
def skeleton(m, n):
    a = turtle.Turtle()
    a.speed(0)
    a.shapesize(0.0001)
    for i in range(m + 1):
        a.goto(i * 20, 0)
        a.pd()
        a.goto(i * 20, n * 20)
        a.pu()
    
    a.goto(0, 0)
    for i in range(n + 1):
        a.goto(0, i * 20)
        a.pd()
        a.goto(m * 20, i * 20)
        a.pu()

# 填入数字
def numbers(m, n):
    a = turtle.Turtle()
    a.speed(0)
    a.shapesize(0.0001)
    a.pu()
    for i in range(m*n):
        a.goto((i % m) * 20 + 10, int(i / m) * 20 + 2)
        a.write(str(i),move=False, align="center",font=("Arial", 10, "normal"))
        

# 画图部分
def draw(m, n, a, b, sol, e):
    pass


def main():

    global sols

    print('input m, n, a, b')
    m, n, a, b = map(int, input().split())
    em = list(range(m*n))
    if a < b:
        a, b = b, a  # 交换顺序，使得竖向的砖在basetile的第0个

    sols = []

    c = time.time()  # 开始计时

    tile(m, n, a, b, em, occ = [])

    if sols == []:
        print([])
    else:
        diffsols = []
        for i in sols:
            if issol(i, diffsols) == True:  # 如果不同解
                diffsols.append(i)

        for i in diffsols:
            print(i)

    d = time.time()
    print(str(d - c) + ' sec')

    print('Choose a solution to draw it.')
    e = int(input())
    if e > len(diffsols):
        print('Input of of range')
    else:
        draw(m, n, a, b, diffsols, e)


if __name__ == "__main__":
    main()
