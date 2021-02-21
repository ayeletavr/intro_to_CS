###################################
# FILE : ex5.py
# WRITER : Ayelet Avraham, ayeletavr, 313451932
# EXERCISE : intro2cs ex5 2019
# DESCRIPTION : Test of WordSearch.
##################################

from wordsearch import *
def test_search_r():
    if search_r(['No','Yes','mayBe','no','yes'],[['a','b''c'],['e','f','g'],['h','i','j']]) == []:
        print("Test 01 success.")
    else:
        print("Test 01 fail.")
    if search_r(['efg'],[['a','b''c'],['e','f','g'],['h','i','j']]) == ['efg']:
        print("Test 02 success.")
    else:
        print("Test 02 fail.")
    if search_r(['pop','pop'],[['a','b''c'],['e','f','g'],['p','o','p']]) == ['pop','pop']:
        print("Test 03 success.")
    else:
        print("Test 03 fail.")
    if search_r(['i','am','Lord','Voldemort'],[['a','m''c'],['l','o','r'],['h','i','j']]) == ['i','am'] or ['am','i']:
        print("Test 04 success.")
    else:
        print("Test 04 fail.")

if __name__ == "__main__":
    test_search_r()