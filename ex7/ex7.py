####################################################
# FILE: ex7.py
# WRITER: Ayelet Avraham, ayeletavr, 313451932
# EXERCISE: intro2cs ex7 2019 - Recursion
# DESCRIPTION: Recursion functions.
####################################################

### Part A - Simple recursion functions ###


def print_to_n(n):
    """
    Gets a natural number n and prints all natural numbers from 1 to n.
    :param n: any natural number.
    :return: None (only prints).
    """
    if n < 1:
        return None
    elif n == 1: #base case
        print(n)
    else:
        print_to_n(n-1)
        print(n)


def print_reversed(n):
    """
    Gets any natural number n and prints all natural numbers from n to 1.
    :param n: any natural number.
    :return: None (only prints).
    """
    if n < 1:
        return None
    elif n == 1: #base case
        print(n)
    else:
        print(n)
        return print_reversed(n-1)


def has_divisor_smaller_than(n,i):
    """
    Side function to is_prime. Gets a natural number n and natural number i,
     and checks for all natural numbers between 2 to i if any of them is a divisor to n.
    :param n: and natural number.
    :param i: a natural number up to n.
    :return: True if finds a divisor. else False.
    """

    #all base cases
    if n <= 2:
        return True if (n == 2) else False
    if n % i == 0:
        return False
    if i * i > n:
        return True

    return has_divisor_smaller_than(n, i+1)


def is_prime(n):
    """
    Gets any natural number and checks if prime.
    :param n: any natural number.
    :return: True if prime, else False.
    """
    if has_divisor_smaller_than(n,2):
        return True
    else:
        return False


def factorial(n):
    """
    Side function to exp_n_x. Gets any number and calculates its factorial.
    :param n: any number.
    :return: factorial n.
    """
    if n == 0: #base case
        return 1
    else:
        return n * factorial(n-1)


def exp_n_x(n,x):
    """
    Gets a natural number larger than 0 n, and any number x, and return exponential sum function.
    :param n: natural number n > 0.
    :param x: any float.
    :return:
    """
    if n == 0: #base case.
        return 1
    return (x**n / factorial(n)) + exp_n_x(n-1, x)


### Part B - more complicated recursive functions. ###

def play_hanoi(hanoi, n, src, dest, temp):
    """
    Play hanoi game, according to the rules.
    :param hanoi: graphics.
    :param n: number of disks.
    :param src: source pole - at the beginning, contains all n disks in the right order.
    :param dest: destination pole - the target is to move all n disks in the right order.
    :param temp: temporary pole for disks.
    :return: None (plays game).
    """
    if n > 0:
        play_hanoi(hanoi, n-1, src, temp, dest) #move n-1 disks from src to temp.
        hanoi.move(src,dest) #move the nth disk from src to dest.
        play_hanoi(hanoi, n-1, temp, dest, src) #move the rest n-1 disks from temp to dest.
    else:
        return


def print_sequences_helper(char_list, start, n, result):
    """
    helper to print_sequences. recursive function that prints strings in len(n),
     and builds them up from all chars in char list.
    :param char_list: characters only list.
    :param start: index.
    :param n: natural number >= 0.
    :param result: str.
    :return: strs - combinations of chars.
    """
    if len(result) >= n: #base case
        print(result)
        return
    if start < 0:
        return

    print_sequences_helper(char_list, start-1, n, result[:])

    result += char_list[start]
    print_sequences_helper(char_list,  len(char_list)-1, n, result)

def print_sequences(char_list, n):
    """Gets a char list and natural number n, returns all combinations in length n."""
    print_sequences_helper(char_list,  len(char_list)-1, n, "")


def print_no_repetition_helper(char_list, start, n, result):
    """
    helper to print_no_repetition_sequence. recursive function that prints strings in len(n),
     and builds them up from all chars in char list, but also returns only combination that has no repetitions.
    :param char_list: contains different letters only, and len(char_list) >= n
    :param start: index.
    :param n: natural number > 0.
    :param result: string that build itself up in recursion.
    :return: combination in length n that has no repetitions.
    """
    if len(set(result)) == len(result) == n: #base case
        print(result)
        return
    if len(result) > n:
        return
    if start < 0:
        return

    print_no_repetition_helper(char_list, start-1, n, result[:])
    result += char_list[start]
    print_no_repetition_helper(char_list, len(char_list)-1, n, result)


def print_no_repetition_sequences(char_list, n):
    print_no_repetition_helper(char_list, len(char_list)-1, n, "")


def parentheses_helper(n, left, right,s,lst):
    """
    This is a recursive function that returns a list of all combination of valid-balanced parentheses.
    base case of recorsion is when number of '(' is equal to number of ')'.
    :param n: a natural number > 0.
    :param left: appends '('.
    :param right: appends ')'.
    :param s: string contains balanced parentheses.
    :param lst: final list to return
    :return: final list with combinations.
    """
    if right == n: #base case
        lst.append(s)
    if left < n:
        parentheses_helper(n, left + 1, right, s + "(",lst)
    if right < left:
        parentheses_helper(n, left, right + 1, s + ")",lst)
    return lst

def parentheses(n):
    """Gets a natural number n > 0 and returns all combinations of valid-balanced parentheses in length n."""
    return parentheses_helper(n, 0, 0, "",[])


def up_and_right_helper(list, start, set):
    """This is a general function that gets a list, and returns a set with all permutations as str.
     Helper to up_and_right."""
    if start > len(list)-1: #base case
        string = "".join(list)
        set.add(string)
        return
    up_and_right_helper(list, start+1, set)
    for i in range(start+1, len(list)):
        list[start], list[i] = list[i], list[start]
        up_and_right_helper(list, start+1, set)
        list[start], list[i] = list[i], list[start]
    return set


def up_and_right(n, k):
    """
    Gets number of steps to turn right or up, and prints all possible ways to go.
    :param n: steps right.
    :param k: steps up.
    :return: None. only prints.
    """
    u_r_srt = 'r' * n + 'u' * k
    u_r_list = []
    for i in u_r_srt:
        u_r_list.append(i)

    resule_set = up_and_right_helper(u_r_list, 0, set())
    for str in resule_set:
        print(str)


def flood_fill_helper(image, x, y):
    """
    helper to flood_fill. allows user to start with filled dot, than finds valid ways to fill, and fills them.
    :param image: list of lists with '*' or '.'
    :param x: index in row.
    :param y: index in col.
    :return: filled ways.
    """
    image[x][y] = '*'
    if image[x-1][y] == '*' and image[x+1][y] == '*' and image[x][y-1] == '*' and image[x][y+1] == '*': #base case
        print(image)
        return
    if image[x-1][y] == '.':
        flood_fill_helper(image,x-1,y)
    if image[x+1][y] == '.':
        flood_fill_helper(image,x+1,y)
    if image[x][y-1] == '.':
        flood_fill_helper(image, x, y-1)
    if image[x][y+1] == '.':
        flood_fill_helper(image, x, y+1)


def flood_fill(image, start):
    """Gets a valid image (list of lists), and fills it according to the start point and the rules."""
    flood_fill_helper(image, start[0], start[1])
