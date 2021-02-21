###################################
# FILE : ex4.py
# WRITER : Ayelet Avraham, ayeletavr, 313451932
# EXERCISE : intro2cs ex4 2019
# DESCRIPTION : Hangman game.
##################################


from hangman_helper import *

"""Side functions to use in PART A"""
#Function that copies str and converts it to dict with it's index.
def indexed_copy(str):
    indexed_dict = dict(enumerate(str[:]))
    return indexed_dict

#Function that makes list of indexes (str)
def list_of_indexes(word_dict,letter):
    keys_list = list(word_dict)
    # keys_list = int_list_to_str_list(keys_list)
    values_list = list(word_dict.values())
    word_list = list(zip(values_list, keys_list))
    letter_list = list(letter[:])
    indexes_list = []
    for i in word_list:
        for l in i:
            if l == letter_list[0]:
                indexes_list.append(i[1])
    return (indexes_list)

#to set an initial pattern:
def initial_pattern(word):
    initial = []
    for letter in word:
        initial.append("_")
    sep = ""
    initial = sep.join(initial)
    return initial

#to determine if guess is a lower letter:
def lower_letter(letter):
    if ord(letter) in range (97,123):
        return True
    else:
        return False


#PART A - 1:
"""Function that updated pattern to use in game"""
def update_word_pattern(word, pattern, letter):
    word_dict = indexed_copy(word[:])
    word_list = list(word_dict.values())
    pattern_list = list(pattern[:])
    letter_list = list(letter[:])
    index_list = list_of_indexes(word_dict,letter)
    for l in word_list:
        if l == letter_list[0]:
            for num in index_list:
                pattern_list[num] = l
    sep = ""
    new_pattern = sep.join(pattern_list)
    return(new_pattern)
# print(update_word_pattern('apple','___l_','p'))

"""PART B"""
def filter_words_list(words, pattern, wrong_guess_lst):
    filter1 = []
    filter2 = []
    filtered_list = []
    pattern_len = len(pattern)
    seen_char_lst = [(char_index, pattern[char_index]) for char_index in range(pattern_len) if
                     pattern[char_index] != '_']

    for word in words:
        if pattern_len == len(word):
            filter1.append(word)


    if seen_char_lst!=[]: #to append filter2 that contains words with unseen letters.

        for filter1_word in filter1: #To filter words that have same letter in pattern, in same index.
            suitable_word = True
            for char_tuple in seen_char_lst:
                if filter1_word[char_tuple[0]] != char_tuple[1]:
                    suitable_word = False

            if(suitable_word):
                filter2.append(filter1_word)

        return filter2

    else:
        if wrong_guess_lst == []:
            return filter1


        else:
            for filter1_word in filter1: #to filter words that have same letters in wrong_geuss list
                suitable_word = True
                for wrong_lett in wrong_guess_lst:
                    if wrong_lett in filter1_word:
                        suitable_word = False

                if suitable_word:
                    filtered_list.append(filter1_word)

            return filtered_list


def most_common(lst):
    """to find most common item in any list"""
    return max(set(lst), key=lst.count)

#print(most_common(['duck','duck','goose','goose','horse']))

def choose_letter(words,pattern):
    big_list = []
    for word in words:
        for letter in word:
            if letter not in pattern:
                big_list.append(letter)

    return(most_common(big_list))
#print(choose_letter(['grape','straberry','tomato'],"___"))

#PART A - 2:
"""Function that runs a single game"""
def run_single_game(words_list):
    wrong_guess_lst = []
    random_word = get_random_word(words_list)
    msg = DEFAULT_MSG #game start
    error_count = 0
    pattern = initial_pattern(random_word)
    while error_count < MAX_ERRORS and random_word != pattern:
        display_state(pattern, error_count, wrong_guess_lst, msg, ask_play=False)
        guess = get_input()
        if guess == (HINT, None):
            filtered_list = filter_words_list(words_list, pattern, wrong_guess_lst)
            common_letter = choose_letter(filtered_list, pattern)
            msg = HINT_MSG+common_letter
            #display_state(pattern, error_count, wrong_guess_lst, HINT_MSG + common_letter, ask_play=False)
        elif len(guess[1]) != 1 or lower_letter(guess[1]) == False:
            msg = NON_VALID_MSG
        elif guess[1] in wrong_guess_lst or guess[1] in pattern:
            msg = ALREADY_CHOSEN_MSG
        elif guess[1] in random_word:
            pattern = update_word_pattern(random_word, pattern, guess[1])
            msg = DEFAULT_MSG
        else:
            wrong_guess_lst.append(guess[1])
            msg = DEFAULT_MSG
            error_count += 1


    if(error_count==MAX_ERRORS):
        msg = LOSS_MSG + random_word

    else:
        msg = WIN_MSG
    display_state(pattern, error_count, wrong_guess_lst, msg, ask_play=True)
# #
"""Function that runs game as many times as requesed"""
def main():
    play_again_request = True
    word_list = load_words(file='words.txt')
    while play_again_request == True:
        run_single_game(word_list)
        play_again, play_again_request = get_input()


if __name__ == "__main__":
    main()

