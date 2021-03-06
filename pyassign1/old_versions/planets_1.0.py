""" planets.py: Model of the solar system (6 planets)

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

#       saturn
#       semi-major axis = 9.583
#       eccentricity = 0.0565
#       period = 29.46
#       radius = 9.140
#       longitude of the ascending node = 113.64
#       argument of periapsis = 339.392


import math
import turtle


wn = turtle.Screen()
wn.bgcolor("Black")


# [semi-major axis, eccentricity, period, radius,
#   longitude of the ascending node, argument of periapsis,
#   colorR, colorG, colorB]
sun = [0*50, 0, 1, 109*0.01, 0, 0, 247, 196, 99]
mercury = [0.387*50, 0.206, 0.241, 0.467*0.05, 48.33, 29.12, 126, 122, 126]
venus = [0.723*50, 0.00677, 0.615, 0.950*0.05, 76.68, 54.88, 230, 178, 91]
earth = [1.000*50, 0.0167, 1.000, 1.000*0.05, -11.26, 114.21, 55, 63, 89]
mars = [1.523*50, 0.0934, 1.881, 0.532*0.05, 49.56, 286.50, 238, 138, 104]
jupiter = [5.204*50, 0.0489, 11.86, 10.97*0.05, 100.46, 273.87, 207, 191, 173]
saturn = [9.583*50, 0.0565, 29.46, 9.14*0.05, 113.64, 339.39, 196, 164, 115]

planet_list = [sun, mercury, venus, earth,
               mars, jupiter, saturn]


# parameter of an ellipse
def r(a, e, t):
    r = a*(1 - e**2)/(1 - e*math.cos(t/180*math.pi))
    return r


# covertion between polar and cartesian coordinates
def car(r, t):
    x = r*math.cos(t/180*math.pi)
    y = r*math.sin(t/180*math.pi)
    xy = [x, y]
    return xy


# define angular velocity
def ang(x, i):
    return i * mercury[2] / x[2] * 5


def draworbital(planet, x, i):

    # move to the orbital
    if i in range(1, 7):
        planet.ht()
        planet.goto(car(r(x[0], x[1], ang(x, i)), ang(x, i))[0],
                    car(r(x[0], x[1], ang(x, i)), ang(x, i))[1])
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
    planet.goto(car(r(x[0], x[1], ang(x, i)), ang(x, i))[0],
                car(r(x[0], x[1], ang(x, i)), ang(x, i))[1])


def main():

    # create turtles
    a = turtle.Turtle()
    b = turtle.Turtle()
    c = turtle.Turtle()
    d = turtle.Turtle()
    e = turtle.Turtle()
    f = turtle.Turtle()
    g = turtle.Turtle()
    text_turtle = turtle.Turtle()

    turtles = [a, b, c, d, e, f, g]

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
        draworbital(turtles[j % 7],
                    planet_list[j % 7], j)

        if j % 5 == 0:
            text_turtle.color("Black")
            text_turtle.write(len(str(int(j-50)*5*88.0/360))*"█" + " d",
                              move=False, align="left",
                              font=("Arial", 24, "normal"))
            text_turtle.color("White")
            text_turtle.write(str(int(j*5*88.0/360)) + " d",
                              move=False, align="left",
                              font=("Arial", 24, "normal"))

        j += 1


if __name__ == "__main__":
    main()
