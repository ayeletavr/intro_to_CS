###################################
# FILE : calculate_mathematical_expression.py
# WRITER : Ayelet Avraham, ayeletavr, 313451932
# EXERCISE : intro2cs ex2 2019
# DESCRIPTION : Functions that solves basic mathematical exspressions.
##################################

#Q2: Function that helps Hermaione to calculate mathematical expressions.
def calculate_mathematical_expression(num1,num2,operator):
    if operator == '+':
        calc = num1 + num2
    elif operator == '-':
        calc = num1 - num2
    elif operator == '*':
        calc = num1 * num2
    elif operator == '/' and num2 != 0:
        calc = num1 / num2
    elif operator == '/' and num2 == 0:
        calc = None
    else: calc = None
    return calc

#Q3: Function that calculates from str.
def calculate_from_string(myStr):
    myList = myStr.split()
    if myList[2] == '+' or '-' or '*' or '/':
        num1 = float(myList[0])
        num2 = float(myList[2])
        operator = myList[1]
        calc = calculate_mathematical_expression(num1,num2,operator)
    else: calc = None
    return calc