###################################
# FILE : stable_price.py
# WRITER : Ayelet Avraham, ayeletavr, 313451932
# EXERCISE : intro2cs ex2 2019
# DESCRIPTION : A Function that determines prices stability.
##################################

def is_it_stable(val, year1, year2, year3):
    result = bool(abs(year2 - year1) <= val and abs(year3 - year2) <= val)
    return result