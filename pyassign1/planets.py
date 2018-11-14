""" planets.py: Model of the solar system (6 planets + 1 comet + 1 asteroid)
__author__ = 'Yichen Nie'
__pkuid__ = '1800011703'
__email__ = '1800011703@pku.edu.cn'
"""

import math
import turtle
import time
from scipy.optimize import fsolve


# [semi-major axis, eccentricity, period, radius,
#   longitude of the ascending node, argument of periapsis,
#   colorR, colorG, colorB]
#   wikipedia
sun = [0*50, 0, 1, 109*0.01, 0, 0, 247, 196, 99]
mercury = [0.387*50, 0.206, 0.241, 0.467*0.05,
           48.33, 29.12, 126, 122, 126]
venus = [0.723*50, 0.00677, 0.615, 0.950*0.05,
         76.68, 54.88, 230, 178, 91]
earth = [1.000*50, 0.0167, 1.000, 1.000*0.05,
         -11.26, 114.21, 55, 63, 89]
mars = [1.523*50, 0.0934, 1.881, 0.532*0.05,
        49.56, 286.50, 238, 138, 104]
jupiter = [5.204*50, 0.0489, 11.86, 10.97*0.05,
           100.46, 273.87, 207, 191, 173]
saturn = [9.583*50, 0.0565, 29.46, 9.14*0.05,
          113.64, 339.39, 196, 164, 115]
halley = [17.8*50, 0.967, 75.3, 2*0.05,
          58.42, 111.33, 255, 255, 255]
phaethon = [1.271*50, 0.890, 1.43, 2*0.05,
            265.427, 321.978,
            128, 128, 128]

planet_list = [sun, mercury, venus, earth,
               mars, jupiter, saturn, halley,
               phaethon]


# coordinates of the planets
def coor(x, time):

    def xi_function(xi):
        xi = float(xi)
        return x[0]**(3/2) * (xi - x[1]*math.sin(xi)) / speed - time

    xi_root = fsolve(xi_function, 10)
    coor_x = x[0] * (math.cos(xi_root) - x[1])
    coor_y = x[0] * (1 - x[1]**2)**0.5 * math.sin(xi_root)

    polar_r = (coor_x**2 + coor_y**2)**0.5

    rot_ang = (x[4] + x[5])/180*math.pi

    if polar_r == 0:
        polar_theta = rot_ang
    elif coor_x > 0:
        polar_theta = math.atan(coor_y/coor_x) + rot_ang
    elif coor_x < 0 and coor_y >= 0:
        polar_theta = math.atan(coor_y/coor_x) + math.pi + rot_ang
    elif coor_x < 0 and coor_y < 0:
        polar_theta = math.atan(coor_y/coor_x) - math.pi + rot_ang
    elif coor_x == 0:
        if y > 0:
            polar_theta = math.pi/2 + rot_ang
        if y < 0:
            polar_theta = -math.pi/2 + rot_ang

    coor_x = polar_r * math.cos(polar_theta)
    coor_y = polar_r * math.sin(polar_theta)

    return [coor_x, coor_y]


def draworbit(planet_turtle, planet, i):

    planet_turtle.st()

    # coordinates
    planet_turtle.goto(coor(planet, i)[0],
                       coor(planet, i)[1])


def main():

    wn = turtle.Screen()
    wn.bgcolor("Black")
    global speed
    speed = int(turtle.numinput('speed control', 'slowest = 1, fastest = 10',
                                default=None, minval=1, maxval=10))

    j = 1
    time_counter = 0

    # create turtles
    a = turtle.Turtle()
    b = turtle.Turtle()
    c = turtle.Turtle()
    d = turtle.Turtle()
    e = turtle.Turtle()
    f = turtle.Turtle()
    g = turtle.Turtle()
    h = turtle.Turtle()
    i = turtle.Turtle()
    text_turtle = turtle.Turtle()

    turtles = [a, b, c, d, e, f, g, h, i]

    # time
    text_turtle.color("Black")
    text_turtle.speed(0)
    text_turtle.shapesize(0.0000000001)
    text_turtle.goto(-400, 200)
    text_turtle.left(-90)
    text_turtle.color("White")

    for x in turtles:

        # move to the orbits
        if j in range(1, 8):
            x.ht()
            x.goto(coor(planet_list[turtles.index(x)], j)[0],
                   coor(planet_list[turtles.index(x)], j)[1])

        x.shape("circle")

        x.pencolor(planet_list[turtles.index(x)][6] / 255,
                   planet_list[turtles.index(x)][7] / 255,
                   planet_list[turtles.index(x)][8] / 255)

        x.fillcolor(planet_list[turtles.index(x)][6] / 255,
                    planet_list[turtles.index(x)][7] / 255,
                    planet_list[turtles.index(x)][8] / 255)

        x.turtlesize(planet_list[turtles.index(x)][3])

        x.speed(0)

    time_start = time.clock()
    time_last = time_start

    text_turtle.write(str(0) + " days",
                      move=False, align="left",
                      font=("Arial", 24, "normal"))

    while True:

        b_lastxcoor = b.xcor()
        b_lastycoor = b.ycor()

        draworbit(turtles[j % 9],
                  planet_list[j % 9], j)

        # time parameter

        if b.xcor() < 0 and b.ycor() < 0 and \
           b_lastxcoor < 0 and b_lastycoor > 0:

            time_now = time.clock()
            day_parameter = 0.241 * 365.2422 / \
                ((time_now - time_start)/(time_counter + 0.5))

            time_counter += 1

            text_turtle.undo()

            text_turtle.color("White")
            text_turtle.write(str(int((time.clock() - time_start
                                       ) * day_parameter)) + " days",
                              move=False, align="left",
                              font=("Arial", 24, "normal"))

            time_last = time.clock()

        j += 1


if __name__ == "__main__":
    main()
