####################################################
# FILE: ex8.py
# WRITER: Ayelet Avraham, ayeletavr, 313451932
# EXERCISE: intro2cs ex8 2019 - Sudoko and k subsets.
# DESCRIPTION: Backtracking functions.
####################################################

#### PART A - Sudoko ####

import math

def find_empty_location(board, list):
    """This function searches in board to find an empty location (0).
     list is a variable that tracking threw the board."""
    for row in range(len(board[0])):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                list[0] = row
                list[1] = col
                return True
    return False

def safe_row(board, row, num):
    """Returns False if num is already taken in row, else True."""
    for i in range(len(board[0])):
        if board[row][i] == num:
            return False
    return True

def safe_col(board, col, num):
    """Returns False if num is already taken in col, else True."""
    for i in range(len(board[0])):
        if board[i][col] == num:
            return False
    return True


def safe_inner_square(board, row, col, num):
    """Returns False if num is already taken in inner square, else True."""
    for i in range(int(math.sqrt(len(board[0])))):
        for j in range(int(math.sqrt(len(board[0])))):
            if board[i + int(row)][j + int(col)] == num:
                return False
    return True


def safe_placement(board, row, col, num):
    """
    checks for specific number if there are legal placement in board (according to the rules).
     returns True if finds a placement, else False.
    :param board: empty or half-filled board.
    :param row: row in board.
    :param col: col in board.
    :param num: a natural number 1 to length of row in board.
    :return: True if finds a legal placement, else False.
    """
    if safe_col(board, col, num) and safe_row(board, row, num)\
            and safe_inner_square(board, row - row % (math.sqrt(len(board[0]))),
                                  col - col % (math.sqrt(len(board[0]))), num):
        return True
    else:
        return False

def solve_sudoku(board):
    """
    Main function that solves sudoku board. As it starts with list index [row-0, col-0],
     it runs back and forward through the board, checks if location is empty and legal according to game rules,
      then place a number. keeps back and forward (backtracking) until board if full according to rules game.

    :param board: n*n size board (square root of n is natural number).
    :return: True if solved, else False.
    """
    l = [0, 0] #this will be used as a row and column index.
    if not find_empty_location(board, l): #base case - there is no empty locating and sudoku in solved.
        return True
    row = l[0]
    col = l[1]
    for num in range(len(board)+1):
        if (safe_placement(board, row, col, num)):
            board[row][col] = num
            if (solve_sudoku(board)):
                return True
            board[row][col] = 0 #if fails and need to go back.
    return False


##################################################################

#### PART B - k Subsets ###

def print_set(cur_set):
    """helper to k_subsets_helper. Prints a list contains a subset."""
    lst_to_print = []
    for (index, in_cur_set) in enumerate(cur_set):
        if in_cur_set:
            lst_to_print.append(index) #appends a subset list.
    print(lst_to_print)


def k_subset_helper(cur_set, k, index, picked):
    """Helper to print_k_subsets. This is the recursive functions that threw backtracking finds all subsets.
     We did this in the Tirgul."""
    # Base: we picked out k items.
    if k == picked:
        print_set(cur_set)
        return

    # If we reached the end of the list, backtrack.
    if index == len(cur_set):
        return

    # Runs on all sets that include this index.
    cur_set[index] = True
    k_subset_helper(cur_set, k, index + 1, picked + 1)

    # Runs on all sets that do not include index.
    cur_set[index] = False
    k_subset_helper(cur_set, k, index + 1, picked)


def print_k_subsets(n,k):
    """
    Main Function that prints all k subsets, using the helper and the print_set.
    :param n: a natural number >= 0.
    :param k: a natural number > 0.
    :return: None, only prints.
    """
    if k <= n:
        cur_set = [False] * n
        k_subset_helper(cur_set, k, 0, 0)

###################################################################

def fill_list(cur_set, list):
    """Helper to fill_k_subsets_helper. appends subsets to a list."""
    sub_list = []
    for (index, in_cur_set) in enumerate(cur_set):
        if in_cur_set:
            sub_list.append(index)
    list.append(sub_list)

def fill_k_subsets_helper(cur_set, k, index, list, picked):
    """Helper to fill_k_subsets. This is the recursive functions that threw backtracking finds all subsets,
     as we did in the Tirgul."""

    # Base: we picked out k items.
    if k == picked:
        fill_list(cur_set, list)
        return

    # If we reached the end of the list, backtrack.
    if index == len(cur_set):
        return

    # Runs on all sets that include this index.
    cur_set[index] = True
    fill_k_subsets_helper(cur_set, k, index + 1, list, picked + 1)

    # Runs on all sets that do not include index.
    cur_set[index] = False
    fill_k_subsets_helper(cur_set, k, index + 1, list,  picked)

def fill_k_subsets(n,k,list):
    """
    Main function that uses helpers above to append all k subsets to a list.
    :param n: a natural number >= 0
    :param k: a natural number > 0.
    :param list: list to append all subsets (initial list is empty).
    :return: None, only changes the list.
    """
    if k <= n:
        cur_set = [False] * n
        fill_k_subsets_helper(cur_set, k, 0, list, 0,)

#################################################

def return_k_subsets(n, k):
    """
    This function returns a list of lists with k subsets. the n-1 iteration keeps us not passing the k length.
    :param n: a natural number >= 0
    :param k: a natural number >0
    :return: list of lists.
    """
    if n < k or k < 0:
        return []
    if k == n:
        return [list(range(k))]
    # Recursive list comprehension,
    # that relies on the fact tht there is only one subset that is in length k and >= 0 and < n.
    return return_k_subsets(n-1, k) + [i+[n-1] for i in return_k_subsets(n-1, k-1)]