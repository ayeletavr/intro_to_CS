###################################
# FILE : largest_and_smallest.py
# WRITER : Ayelet Avraham, ayeletavr, 313451932
# EXERCISE : intro2cs ex2 2019
# DESCRIPTION : A Function that finds min and max values.
##################################

def largest_and_smallest(n1,n2,n3):
    if n1 >= n2 and n1 >= n3:
        max_val = n1
        if n2 >= n3:
            min_val = n3
        else: min_val = n2
    elif n1 >= n2 and n1 <= n3:
        max_val = n3
        min_val = n2
    elif n1 <= n2 and n1 <= n3:
        min_val = n1
        if n2 <= n3:
            max_val = n3
        else: max_val = n2
    if n1 == n2 and n2 == n3:
        max_val = n1
        min_val = n3
    return(max_val,min_val)