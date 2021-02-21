###################################
# FILE : check_largest_and_smallest.py
# WRITER : Ayelet Avraham, ayeletavr, 313451932
# EXERCISE : intro2cs ex2 2019
# DESCRIPTION : Tester of Function 4.
##################################

def my_test():
    from largest_and_smallest import largest_and_smallest
    try1 = largest_and_smallest(1,1,1)
    check1 = bool(try1 == (1,1))
    try2 = largest_and_smallest(999,-1,0)
    check2 = bool(try2 == (999,-1))
    try3 = largest_and_smallest(-1,0,999)
    check3 = bool(try3 == (999,-1))
    try4 = largest_and_smallest(1000000,1000000.1,1000000.11)
    check4 = bool(try4 == (1000000.11,1000000))
    try5 = largest_and_smallest(0.001,0.0011,0.00111)
    check5 = bool(try5 == (0.00111,0.001))
    result = bool(check1 and check2 and check3 and check4 and check5)
    if result:
        print("Function 4 test success")
    else:
        print("Function 4 test failed")
    return result

if __name__ == "__main__":
    my_test()