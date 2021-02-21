###################################
# FILE : ex5.py
# WRITER : Ayelet Avraham, ayeletavr, 313451932
# EXERCISE : intro2cs ex5 2019
# DESCRIPTION : Word-Search in a matrix.
##################################
import sys

#Side Functions to check_input_args(args)
def check_word_file(word_file): #checks secound argument
    word_file = open(word_file)
    for word in word_file: #to use file as str.
        if type(word) == str and word[-1] == '\n' and ' ' not in word:
            return True
        else:
            return False

def check_matrix_file(matrix_file): #checks third argument.
    matrix_file = open(matrix_file)
    for row in matrix_file:
         if type(row) == str and row[-1] == '\n':
                 return True
         else:
             return False

def check_directions(directions): #checks fifth argument.
    if type(directions) == str:
        counter = 0
        valid_direct = []
        directs_list = directions[:].split()
        for direction in directs_list:
            while counter <= len(directions):
                if direction in 'udrlwxyz':
                    valid_direct.append(direction)
                    counter += 1
                else: break
                if valid_direct == directs_list:
                    return True
        else:
            return False
    else: return False

def check_input_args(args):
    """Function that checks that all arguments are valid."""
    msg_lst = []
    if len(args) != 5:
        return "Invalid number of arguments."
    elif check_word_file(args[1]) and check_matrix_file(args[2])\
        and check_directions(args[4]):
        return None
    else:
        if check_word_file(args[1]) == False or None:
            msg_lst.append("Word file does not exist.")
        if check_matrix_file(args[2]) == False or None:
            msg_lst.append("Matrix file does not exist.")
        if check_directions(args[4]) == False or None:
            msg_lst.append("Invalid directions.")
        sep = " "
        msg_lst = sep.join(msg_lst)
        return msg_lst

def read_wordlist_file(filename):
    """Gets word file and returns list of words."""
    word_file = open(filename)
    word_list = []
    for word in word_file: #to use file as str.
        word_list.append(word.split("\n")[0])
    return word_list

def read_matrix_file(filename):
    """Gets matrix file and returns matrix list."""
    matrix_file = open(filename)
    mid_list = []
    final_lst = []
    for matrix in matrix_file:
        mid_list.append(matrix[:-1])
    for row in mid_list:
        final_lst.append(row.split(","))
    return final_lst

###Side functions to find_words_in_matrix:###

def transpose(matrix): # to transpose
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed

def reverse(matrix): #to reverse a matrix.
    counter = 0
    while counter <= len(matrix[0]):
        for row in matrix:
            row.reverse()
            counter += 1
        return matrix

def upside_down(matrix): #to flip upside-down a matrix.
        matrix.reverse()
        return matrix

def diag_y_lst(matrix):#to make diagonals list.
    srch_y = []
    m, n = len(matrix), len(matrix[0])
    for offset in range(min(m,n)):
        diag_upper = [row[i + offset]
                      for i, row in enumerate(matrix)
                      if 0 <= i + offset < n]
        if offset != 0:
            diag_lower = [row[i - offset]
                      for i, row in enumerate(matrix)
                      if 0 <= i - offset < m]
            srch_y.append(diag_upper)
            srch_y.append(diag_lower)
        else:
            srch_y.append(diag_upper)
    return srch_y

def histogram(word_list): #to arrange in a dictionary.
    words_dict = dict()
    for word in word_list:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1
    return words_dict

###each function for a single direction.###
def search_r(word_list,matrix): #for r direction.
    join_mat = []
    r_lst = []
    sep = ""
    for row in matrix[:]:
        join_mat.append(sep.join(row))
    for word in word_list:
        for row in join_mat:
            index = row.find(word)
            if index != -1:
                r_lst.append(word)
                while index <= len(row):
                    index = row.find(word, index + 1)  # to check until there are no letters left.
                    if index != -1:
                        r_lst.append(word)
                    else:
                        break
    return r_lst

def search_l(word_list,matrix): #for l direction.
    l_lst = search_r(word_list,reverse(matrix[:]))
    return l_lst

def search_d(word_list,matrix): #for d direction.
    d_lst = search_r(word_list,transpose(matrix[:]))
    return d_lst

def search_u(word_list,matrix): #for u direction.
    trans_up_down = transpose(upside_down(matrix[:]))
    u_lst = search_r(word_list,trans_up_down)
    return u_lst

def search_y(word_list,matrix): #for y direction.
    y_lst = search_r(word_list, diag_y_lst(matrix[:]))
    return y_lst

def search_w(word_list,matrix): #for w direction.
    flipped = upside_down(matrix[:])
    z_lst = search_r(word_list,diag_y_lst(flipped))
    return z_lst

def search_z(word_list,matrix): #for z direction.
    z_lst = search_r(word_list, diag_y_lst(reverse(matrix[:])))
    return z_lst

def search_x(word_list,matrix): #for x direction.
    flipped_z = reverse(upside_down(matrix[:]))
    x_lst = search_r(word_list, diag_y_lst(flipped_z))
    return x_lst

def find_words_in_matrix(word_list, matrix, directions):
    """search certain words in a matrix,
    and returns a list that countains the word that
    appeard in the matrix, and how many times."""
    words_dict = dict()
    if 'u' in directions:
        words_dict.update(histogram(search_u(word_list,matrix)))
    if 'd' in directions:
        words_dict.update(histogram(search_d(word_list,matrix)))
    if 'r' in directions:
        words_dict.update(histogram(search_r(word_list,matrix)))
    if 'l' in directions:
        words_dict.update(histogram(search_l(word_list,matrix)))
    if 'x' in directions:
        words_dict.update(histogram(search_x(word_list,matrix)))
    if 'y' in directions:
        words_dict.update(histogram(search_x(word_list,matrix)))
    if 'z' in directions:
        words_dict.update(histogram(search_z(word_list,matrix)))
    if 'w' in directions:
        words_dict.update(histogram(search_u(word_list,matrix)))
    pairs_list = []
    for item in words_dict:
        tup = (item,words_dict[item])
        pairs_list.append(tup)
    return pairs_list

def write_output_file(results, output_filename):
    """creates and returns output file in the requested format."""
    output_file = open(output_filename,'w')
    for tup in results:
        str_result = tup[0] + "," + str(tup[1]) + "\n"
        output_file.write(str_result)
    output_file.close()

def main_function(args):
    """This is the function that connects all parts together
     so user can run the program."""
    if check_input_args(args) != None:
        return check_input_args(args)
    else:
        word_file = args[1]
        matrix_file = args[2]
        out_file = args[3]
        directions = args[4]
        word_list = read_wordlist_file(word_file)
        matrix = read_matrix_file(matrix_file)
        results = find_words_in_matrix(word_list,matrix,directions)
        out_file = write_output_file(results,out_file)
        return out_file

if __name__ == "__main__":
    main_function(sys.argv)