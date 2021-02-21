###################################
# FILE : quadratic equation.py
# WRITER : Ayelet Avraham, ayeletavr, 313451932
# EXERCISE : intro2cs ex2 2019
# DESCRIPTION : Functions that solves quadratic equations.
##################################

#Q5: Function that solves quadratic equations.
def quadratic_equation(a,b,c):
    import math
    if (pow(b,2)-4*a*c) == 0 or (pow(b,2)-4*a*c) >= 0:
        X = (-b + math.sqrt(pow(b,2)-4*a*c))/(2*a)
        Y = (-b - math.sqrt(pow(b,2)-4*a*c))/(2*a)
        if X == Y:
            Y = None
    else:
        X = None
        Y = None
    return (X,Y)

#Q6: Function that gets parameters from user,
#and solves the equation
def quadratic_equation_user_input():
    abcStr = input("Insert coefficients a, b, and c: ")
    abcList = abcStr.split()
    a = eval(abcList[0])
    b = eval(abcList[1])
    c = eval(abcList[2])
    X,Y = quadratic_equation(a,b,c)
    if X != None and Y != None:
        print ("The equation has 2 solutions:",X, "and",Y)
    elif X != None and Y == None:
        print("The equation has 1 solution:",X)
    else:
        print("The equation has no solutions")
