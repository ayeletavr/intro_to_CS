###################################
# FILE : far_to_cel.py
# WRITER : Ayelet Avraham, ayeletavr, 313451932
# EXERCISE : intro2cs ex2 2019
# DESCRIPTION : A Function that converts far to cel.
##################################

def convert_far_to_cel(f):
    f = float(f)
    c = (f - 32) * 5 / 9
    return c