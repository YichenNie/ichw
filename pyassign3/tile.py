import time
import copy
import turtle


'''
tile.py 铺砖问题
用a*b的砖铺满m*n的墙面，给出所有的铺法
并选择其中一种画出示意图
同时创建tile_m_n_a_b.txt将所有解写入其中


例：3*2墙面放2*1砖块
input: m, n, a, b用空格分割每个参数，如3 2 2 1

规定编号方向从0开始，左到右，下到上，3*2的方格为

| 3 | 4 | 5 |
| 0 | 1 | 2 |

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


# 在m*n的墙面上，方格0为右下角，长宽为a*b的矩形（横铺或输铺）
# basetile(4, 3, 3, 2) == [(0, 1, 2, 4, 5, 6), (0, 1, 4, 5, 8, 9)]
def basetile(m, n, a, b):

    bati1 = []
    bati2 = []
    bati_lst = []

    for i in range(a):
        for j in range(b):
            bati1.append(i * m + j)
            bati2.append(j * n + i)

    bati1.sort()
    bati2.sort()

    if bati1[-1] < m * n and len(list(set(bati1))) == len(bati1):
        # 不加最后一个判断条件，运行(2, 3, 2, 3)给出(0, 1, 2, 2, 3, 4)
        bati_lst.append(bati1)
    if (bati2[-1] < m * n and bati1 != bati2 and
            len(list(set(bati2))) == len(bati2)):
        bati_lst.append(bati2)

    return bati_lst


# 墙面大小为m*n，在剩余空位（列表empty）中
# 判断以coor0为左下角时，剩余能否放下与basetile（列表z）一样大小的砖，
def valid(empty, coor0, z, m, n):

    tf = True
    v = coor0 % m - z[0] % m
    for i in z:
        if not (i + coor0 in empty and (i + coor0) % m - i % m == v):
            # 4*3的墙面上，不能用1块砖覆盖7和8
            tf = False

    return tf


# 填砖
# empty: 空方格，occ: 被砖占有的方格
def tile(m, n, a, b, empty, occ=[]):

    if empty == []:  # 所有砖块填满时停止递归
        return sols.append(occ)

    else:
        for v in bati:  # 两个方向或一个方向
            empty1 = copy.deepcopy(empty)
            occ1 = copy.deepcopy(occ)
            # 深拷贝防止进行另一方向砖放入时empty和occ发生更改
            e = empty1[0]

            if valid(empty1, e, v, m, n):
                # 如果可以填入bati[0]方向砖块

                occ1.append(tuple(j + e for j in v))  # 填入砖块
                for j in v:
                    empty1.remove(j + e)  # 空位置中删除填入的砖块

                tile(m, n, a, b, empty1, occ1)  # 递归


# 绘制骨架部分
def skeleton(m, n):
    a = turtle.Turtle()
    a.speed(0)
    a.shapesize(0.0001)
    for i in range(m + 1):
        a.goto(i * 20, 0)
        a.pd()
        a.goto(i * 20, -n * 20)
        a.pu()

    a.goto(0, 0)
    for i in range(n + 1):
        a.goto(0, -i * 20)
        a.pd()
        a.goto(m * 20, -i * 20)
        a.pu()


# 填入数字
def numbers(m, n):
    a = turtle.Turtle()
    a.speed(0)
    a.shapesize(0.0001)
    a.pu()
    for i in range(m*n):
        a.goto((i % m) * 20 + 10, -int(i / m) * 20 - 2)
        a.write(str(i), move=False, align="center",
                font=("Arial", 10, "normal"))


# 第o个方格在图中的位置
def coor(m, n, o):
    return [(o % m) * 20, -int(o / m) * 20]


# 画图部分
def draw(m, n, a, b, sol):
    c = turtle.Turtle()
    c.shapesize(0.0001)
    c.pensize(3)
    c.speed(0)
    c.pu()
    for i in sol:
        c.goto(coor(m, n, i[0]))  # 需要绘制砖块的左下角
        c.pd()
        if (i[-1] - i[0]) % m == a - 1:  # 砖为横向
            c.forward(a * 20)  # 绘制矩形
            c.right(90)
            c.forward(b * 20)
            c.right(90)
            c.forward(a * 20)
            c.right(90)
            c.forward(b * 20)
            c.right(90)

        else:
            c.forward(b * 20)
            c.right(90)
            c.forward(a * 20)
            c.right(90)
            c.forward(b * 20)
            c.right(90)
            c.forward(a * 20)
            c.right(90)

        c.pu()


def main():

    global sols, bati

    print('Input m, n, a, b. \
Use a blank space to separate each parameter.')
    m, n, a, b = map(int, input().split())
    em = list(range(m*n))
    if a < b:
        a, b = b, a  # 交换顺序，使得竖向的砖在basetile的第0个

    sols = []

    c = time.time()  # 开始计时

    bati = basetile(m, n, a, b)

    tile(m, n, a, b, em, occ=[])

    d = time.time()  # 终止计时

    if sols == []:
        print([])
    else:
        for i in range(len(sols)):
            print(i, sols[i])

    if sols != []:
        print('Amount of the solutions = ' + str(len(sols)))

    print(str(d - c) + ' sec')

    # 写入解法，不需要生成txt文件请删掉这段
    with open('tile_' + str(m) + '_' + str(n) + '_' + str(a) +
              '_' + str(b) + '.txt', 'w') as tiletxt:
        tiletxt.write('m, n, a, b = ' + str(m) + ', ' +
                      str(n) + ', ' + str(a) + ', ' +
                      str(b) + '\n')
        tiletxt.write('len(sols) = ' + str(len(sols)) + '\n')
        tiletxt.write('time = ' + str(d - c) + ' sec' + '\n' * 2)
        for i in range(len(sols)):
            tiletxt.write(str(i) + ' ' + str(sols[i]) + '\n')
        tiletxt.write('\n' * 3)

    if sols != []:

        e = int(turtle.numinput('Choose a solution (index) to draw it.',
                                'min = 0, max = ' + str(len(sols) - 1),
                                default=None, minval=0, maxval=len(sols) - 1))

        turtle.setup(width=800, height=800)
        turtle.setworldcoordinates(-10, 10, 790, -790)
        print('Solution to draw is ' + str(sols[e]))

        skeleton(m, n)
        numbers(m, n)
        draw(m, n, a, b, sols[e])
        turtle.done()


if __name__ == "__main__":
    main()
