""" planets.py: Model of the solar system (6 planets + 1 comet)

__author__ = 'Yichen Nie'
__pkuid__ = '1800011703'
__email__ = '1800011703@pku.edu.cn'
"""


# data from wikipedia
# solar
# radius = 109

# mercury
#   semi-major axis = 0.387 au
#   eccentricity = 0.206
#   period = 0.241 a
#   radius = 0.467 earth_radius
#   longitude of the ascending node = 48.331 degree
#   argument of periapsis = 29.124 degree

#   venus
#       semi-major axis = 0.723
#       eccentricity = 0.00677
#       period = 0.615
#       radius = 0.950
#       longitude of the ascending node = 76.680
#       argument of periapsis = 54.884

#   earth
#       semi-major axis = 1.000
#       eccentricity = 0.0167
#       period = 1.000
#       radius = 1.000
#       longitude of the ascending node = -11.261
#       argument of periapsis = 114.208

#   mars
#       semi-major axis = 1.523
#       eccentricity = 0.0934
#       period = 1.881
#       radius = 0.532
#       longitude of the ascending node = 49.558
#       argument of periapsis = 286.502

#   jupiter
#       semi-major axis = 5.204
#       eccentricity = 0.0489
#       period = 11.86
#       radius = 10.97
#       longitude of the ascending node = 100.464
#       argument of periapsis = 273.867

#   saturn
#       semi-major axis = 9.583
#       eccentricity = 0.0565
#       period = 29.46
#       radius = 9.140
#       longitude of the ascending node = 113.64
#       argument of periapsis = 339.392

#   halley comet
#       semi-major axis = 17.8
#       eccentricity = 0.967
#       period = 75.3
#       radius = approx.0
#       longitude of the ascending node = 58.42
#       argument of periapsis = 111.33


import math
import turtle
from scipy.optimize import fsolve


wn = turtle.Screen()
wn.bgcolor("Black")


# [semi-major axis, eccentricity, period, radius,
#   longitude of the ascending node, argument of periapsis,
#   colorR, colorG, colorB]
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

planet_list = [sun, mercury, venus, earth,
               mars, jupiter, saturn, halley]


# coordinates of the planets
def coor(x, time):

    def xi_function(xi):
        xi = float(xi)
        return x[0]**(3/2) * (xi - x[1]*math.sin(xi)) / 10 - time

    xi_root = fsolve(xi_function, 10)
    coor_x = x[0] * (math.cos(xi_root) - x[1])
    coor_y = x[0] * (1 - x[1]**2)**0.5 * math.sin(xi_root)
    return [coor_x, coor_y]


def draworbital(planet, x, i):

    # move to the orbital
    if i in range(1, 9):
        planet.ht()
        planet.goto(coor(x, i)[0],
                    coor(x, i)[1])

    else:
        planet.st()
        # color
        planet.pencolor(x[6] / 255, x[7] / 255,
                        x[8] / 255)
        planet.fillcolor(x[6] / 255, x[7] / 255,
                         x[8] / 255)

        # size
        planet.turtlesize(x[3])

        # rotation
        planet.left(x[4] + x[5])

        # speed
        planet.speed(0)

        # coordinates
        planet.goto(coor(x, i)[0],
                    coor(x, i)[1])


def main():

    # create turtles
    a = turtle.Turtle()
    b = turtle.Turtle()
    c = turtle.Turtle()
    d = turtle.Turtle()
    e = turtle.Turtle()
    f = turtle.Turtle()
    g = turtle.Turtle()
    h = turtle.Turtle()
    text_turtle = turtle.Turtle()

    turtles = [a, b, c, d, e, f, g, h]

    text_turtle.color("Black")
    text_turtle.speed(0)
    text_turtle.shapesize(0.0000000001)
    text_turtle.goto(-400, 200)
    text_turtle.left(-90)
    text_turtle.color("White")

    for x in turtles:
        x.shape("circle")

    j = 1
    while True:
        draworbital(turtles[j % 8],
                    planet_list[j % 8], j)
        if j % 10 == 0:
            text_turtle.color("Black")
            text_turtle.write((5 + len(str(
                                      int((j-10)*0.040511*365.2422)
                                      )))*"█",
                              move=False, align="left",
                              font=("Arial", 24, "normal"))
            text_turtle.color("White")
            text_turtle.write(str(int(j*0.004511*365.2422)) + " days",
                              move=False, align="left",
                              font=("Arial", 24, "normal"))

        j += 1


if __name__ == "__main__":
    main()
