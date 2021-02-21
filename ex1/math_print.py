###################################
# FILE : math_print.py
# WRITER : Ayelet Avraham, ayeletavr, 313451932
# EXERCISE : intro2cs ex1 2019
# DESCRIPTION : Some mathematical functions I implied.
##################################

import math

# Function that prints golden ratio.
def golden_ratio():
    print((1 + math.sqrt(5)) / 2)

# Function that prints 6 power 3.
def six_cubed():
    print(6 ** 3)

# Function that prints hypotenuse.
def hypotenuse():
    print(math.sqrt(3 ** 2 + 5 ** 2))

# Function that print the number pi.
def pi():
    print(math.pi)

# Function that prints the number e.
def e():
    print(math.e)

# Function that prints triangular areas from 1 to 10.
def triangular_area():
    print(math.pow(1,2)/2, math.pow(2,2)/2, math.pow(3,2)/2,math.pow(4,2)/2,math.pow(5,2)/2,
          math.pow(6,2)/2, math.pow(7,2)/2, math.pow(8,2)/2,math.pow(9,2)/2,math.pow(10,2)/2)


if __name__ == "__main__":
    golden_ratio()
    six_cubed()
    hypotenuse()
    pi()
    e()
    triangular_area()