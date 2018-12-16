import time
import copy
import turtle


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
        a.write(str(i),move=False, align="center",font=("Arial", 10, "normal"))
        

# 第i个方格在图中的位置
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
        c.goto(coor(m, n, i[0]))  #需要绘制砖块的左下角
        c.pd()
        if (i[-1] - i[0]) % m == a - 1:  #砖为横向
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

    print('Input m, n, a, b. Use blank spaces to separate all parameters.')
    m, n, a, b = map(int, input().split())
    em = list(range(m*n))
    if a < b:
        a, b = b, a  # 交换顺序，使得竖向的砖在basetile的第0个

    sols = []

    c = time.time()  # 终止计时

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
    
    with open('tile_' + str(m) + '_' + str(n) + '_' + str(a) + '_' + str(b) + '.txt', 'a') as tiletxt:
        tiletxt.write('m, n, a, b = ' + str(m) + ', ' +
                      str(n) + ', ' + str(a) + ', ' +
                      str(b) + '\n')
        tiletxt.write('len(sols) = ' + str(len(sols)) + '\n' * 2)
        tiletxt.write(str(sols) + '\n' * 4)

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
