from ex3 import maximum

def test():
    if maximum([]) == None:
        print("Test 0 OK")
    else:
        print("Test 0 FAIL")
    if maximum([-1,-0.5,0]) == 0:
        print("Test 1 OK")
    else:
        print("Test 1 FAIL")
    if maximum([100000, 1000000, 10000000]) == 10000000:
        print("Test 2 OK")
    else:
        print("Test 2 FAIL")
    if maximum([0.0001, 0.00001, 0.000001]) == 0.0001:
        print("Test 3 OK")
    else:
        print("Test 3 FAIL")

if __name__ == '__main__':
    test()
