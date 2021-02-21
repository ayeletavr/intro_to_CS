###################################
# FILE : shapes.py
# WRITER : Ayelet Avraham, ayeletavr, 313451932
# EXERCISE : intro2cs ex2 2019
# DESCRIPTION : A Function that calculates areas of 3 shapes.
##################################

def circle_area(r):
    import math
    s = math.pi * pow(r, 2)
    return s


def rectangle_area(a, b):
    s = a * b
    return s


def triangle_area(a):
    import math
    s = ((math.sqrt(3))*pow(a,2)) / 4
    return s

def shape_area():
    shape = eval(input('Choose shape (1=circle, 2=rectangle, 3=triangle): '))

    if shape == 1:
        r = float(input())
        s = circle_area(r)
    elif shape == 2:
        a = float(input())
        b = float(input())
        s = rectangle_area(a, b)
    elif shape == 3:
        a = float(input())
        s = triangle_area(a)
    elif shape != 1 or 2 or 3:
        s = None
    return s