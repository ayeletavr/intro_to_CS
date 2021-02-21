####################################################
# FILE: wave_editor.py
# WRITERS: golan shany, golans, 315534842,
# Ayelet Avraham, ayeletavr, 313451932
# EXERCISE: intro2cs ex6 2019
# DESCRIPTION: audio editing program for wav files
####################################################
from numpy import *
import os
from scipy import *
from wave_helper import *


def entrance_menu(saved_audio=None):
    """
    prints the main menu, and executes the appropriate action according
    to user's choice
    :return:
    """
    print("enter your choice: (1-4)")
    print("1. change wav. file")
    print("2. unite two wav. file")
    print("3. compose melody for wav. file")
    print("4. exit the program")
    entrance_choice = input()
    while entrance_choice != '1' and entrance_choice != '2' \
        and entrance_choice != '3' and entrance_choice != '4':
        entrance_choice = input("Invalid choice. Please enter a number 1-4. ")
    if entrance_choice == '1':
        change_wav_menu()
    if entrance_choice == '2':
        unite_wav_menu()
    if entrance_choice == '3':
        compose_wav_menu()
    if entrance_choice == '4':
        return saved_audio


def valid_change(change_input):
    """
    check if user request to make a valid change in wav audio.
    :param change_input:
    :return: True if valid, False if not.
    """
    if change_input == '1' or change_input == '2' or change_input == '3'\
            or change_input == '4' or change_input == '5'\
            or change_input == '6':
        return True
    else:
        return False


def change_wav_menu(audio_file=None):
    """
    get wav file
    prints the menu for the change wave choice, and execute the
    appropriate changing function
    :return:
    """
    if not audio_file:
        audio_file = input("the name and path of the desired wav file")
    print("enter your choice: (1-6)")
    print("1. reverse audio")
    print("2. accelerate speed")
    print("3. decelerate speed")
    print("4. raise volume")
    print("5. lower volume")
    print("6. low pass filter")
    change_menu_choice = input()
    while not valid_change(change_menu_choice):
        print("Invalid choice. Please enter a character 1-6.")
        print("1. reverse audio")
        print("2. accelerate speed")
        print("3. decelerate speed")
        print("4. raise volume")
        print("5. lower volume")
        print("6. low pass filter")
        change_menu_choice = input()
    if change_menu_choice == '1':
        go_to_intermediate_menu(reverse_audio(audio_file))
    if change_menu_choice == '2':
        go_to_intermediate_menu(accelerate_speed(audio_file))
    if change_menu_choice == '3':
        go_to_intermediate_menu(decelerate_speed(audio_file))
    if change_menu_choice == '4':
        go_to_intermediate_menu(raise_volume(audio_file))
    if change_menu_choice == '5':
        go_to_intermediate_menu(lower_volume(audio_file))
    if change_menu_choice == '6':
        go_to_intermediate_menu(low_pass_filter(audio_file))


def reverse_audio(audio_file):
    """
    get wav file and reverse it
    :param audio_file:
    :return:
    """
    initial_wave = load_wave(audio_file)
    while initial_wave == -1:
        audio_file = input("Invalid audio. Please enter a valid Wave file: ")
        initial_wave = load_wave(audio_file)
    reversed_wave = initial_wave[1]
    reversed_wave.reverse()
    to_save = (initial_wave[0], reversed_wave)
    return to_save


def accelerate_speed(audio_file):
    """
    Gets audio wave and returns even samples of audio file.
    :param audio_file:
    :return:
    """
    initial_wave = load_wave(audio_file)
    while initial_wave == -1:
        audio_file = input("Invalid audio. Please enter a valid Wave file: ")
        initial_wave = load_wave(audio_file)
    accelerated_wave = list()
    for sample_index in range(len(initial_wave[1])):
        if sample_index % 2 == 0:
            accelerated_wave.append(initial_wave[1][sample_index])
    to_save = (initial_wave[0],accelerated_wave)
    return to_save


def decelerate_speed(audio_file):
    """
    Gets audio wave and returns it with add samples between each 2
     samples which is their average.
    :param audio_file:
    :return:
    """
    wave_file = load_wave(audio_file)
    while wave_file == -1:
        audio_file = input("Invalid audio. Please enter a valid Wave file: ")
        wave_file = load_wave(audio_file)
    decelerated_wave = wave_file[1]
    for sample_index in range(0, len(decelerated_wave)*2 - 2, 2):
        decelerated_wave_sample = decelerated_wave[sample_index]
        decelerated_wave_next_sample = decelerated_wave[sample_index + 1]
        average_sample_left = int((decelerated_wave_sample[0] +
                                   decelerated_wave_next_sample[0]) / 2)
        average_sample_right = int((decelerated_wave_sample[-1] +
                                    decelerated_wave_next_sample[-1]) / 2)
        average_sample = [average_sample_left, average_sample_right]
        decelerated_wave.insert(sample_index + 1, average_sample)
    to_save = (wave_file[0],decelerated_wave)
    return to_save


def raise_volume(audio_file):
    """
    get wav file and return ith with raised volume by 1.2
    :param audio_file:
    :return:
    """
    frame_rate = load_wave(audio_file)[0]
    raised_volume = load_wave(audio_file)[1]
    while load_wave(audio_file) == -1:
        audio_file = input("Invalid audio. Please enter a valid Wave file: ")
        raised_volume = load_wave(audio_file)[1]
    for sample in raised_volume:
        sample[0] = int(1.2 * sample[0])
        if sample[0] > 32767:
            sample[0] = 32767
        if sample[0] < -32768:
            sample[0] = -32768
        sample[1] = int(1.2 * sample[1])
        if sample[1] > 32767:
            sample[1] = 32767
        if sample[1] < -32768:
            sample[1] = -32768
    to_save = (frame_rate, raised_volume)
    return to_save


def lower_volume(audio_file):
    """
    get wav file and return ith with decreased volume by 1.2
    :param audio_file:
    :return:
    """
    frame_rate = load_wave(audio_file)[0]
    low_volume = load_wave(audio_file)[1]
    while load_wave(audio_file) == -1:
        audio_file = input("Invalid audio. Please enter a valid Wave file: ")
        low_volume = load_wave(audio_file)[1]
    for sample in low_volume:
        sample[0] = int(sample[0] / 1.2)
        if sample[0] > 32767:
            sample[0] = 32767
        if sample[0] < -32768:
            sample[0] = -32768
        sample[1] = int(sample[1] / 1.2)
        if sample[1] > 32767:
            sample[1] = 32767
        if sample[1] < -32768:
            sample[1] = -32768
    to_save = (frame_rate, low_volume)
    return to_save


def low_pass_filter(audio_file):
    """
    apply low pass filter on the input wav file
    :param audio_file:
    :return:
    """
    wave_file = load_wave(audio_file)
    while wave_file == -1:
        audio_file = input("Invalid audio. Please enter a valid Wave file: ")
        wave_file = load_wave(audio_file)
    wave = wave_file[1]
    new_wave = list()
    for sample_index in range(len(wave)):
        wave_sample_left = wave[sample_index][0]
        wave_sample_right = wave[sample_index][1]
        if sample_index == 0:
            wave_next_sample_left = wave[sample_index + 1][0]
            wave_next_sample_right = wave[sample_index + 1][1]
            wave_sample_left = int((wave_sample_left +
                                    wave_next_sample_left) / 2)
            wave_sample_right = int((wave_sample_right +
                                     wave_next_sample_right) / 2)
        elif sample_index == len(wave) - 1:
            wave_previous_sample_left = wave[sample_index - 1][0]
            wave_previous_sample_right = wave[sample_index - 1][1]
            wave_sample_left = int((wave_previous_sample_left +
                                    wave_sample_left) / 2)
            wave_sample_right = int((wave_previous_sample_right +
                                     wave_sample_right) / 2)
        else:
            wave_next_sample_left = wave[sample_index + 1][0]
            wave_next_sample_right = wave[sample_index + 1][1]
            wave_previous_sample_left = wave[sample_index - 1][0]
            wave_previous_sample_right = wave[sample_index - 1][1]
            wave_sample_left = int((wave_previous_sample_left +
                                    wave_sample_left +
                                    wave_next_sample_left) / 3)
            wave_sample_right = int((wave_previous_sample_right +
                                     wave_sample_right +
                                     wave_next_sample_right) / 3)
        new_wave.append([wave_sample_left, wave_sample_right])
    to_save = (wave_file[0], new_wave)
    return to_save


def go_to_intermediate_menu(tuple_audio_file):
    """
    presents an option to save the audio file or change it
    :param audio_file:
    :return:
    """
    print("enter your choice: (1 or 2)")
    print("1. save audio file")
    print("2. change audio file")
    intermediate_menu_choice = input()
    if intermediate_menu_choice == '1':
        file_name = input("enter a file name for saving destination")
        frame_rate = tuple_audio_file[0]
        audio_data = tuple_audio_file[1]
        save_wave(frame_rate, audio_data, file_name)
        saved_audio = (file_name, (frame_rate,audio_data))
        entrance_menu(saved_audio)
    if intermediate_menu_choice == '2':
        change_wav_menu(tuple_audio_file)


def unite_wav_menu():
    """
    offer to unite two audio files, check validity, and then go to
    intermediate menu
    :return:
    """
    two_files_str = input("Enter two files (separate with space): ")
    two_files_list = two_files_str.split()
    audio_file1_name, audio_file2_name = two_files_list[0], two_files_list[1]
    while load_wave(audio_file1_name) == -1 or load_wave(audio_file2_name) == -1:
        print("Invalid one file or more.")
        two_files_str = input("Enter two files (separate with space): ")
        two_files_list = two_files_str.split()
        audio_file1_name, audio_file2_name = two_files_list[0], two_files_list[1]
    merged_file_to_save = unite_two_files(audio_file1_name, audio_file2_name)
    go_to_intermediate_menu(merged_file_to_save)


def unite_two_files(audio_file1_name, audio_file2_name):
    """
    the new sampling rate is the smaller one, and the lists merging is done
    according to the relative sampling rates as defined in the functions:
    shorten_list_for_merge, merge_to_long_list
    :param audio_file1_name:
    :param audio_file2_name:
    :return: the united file
    """
    audio_file1 = load_wave(audio_file1_name)
    audio_file2 = load_wave(audio_file2_name)
    rate1 = audio_file1[0]
    rate2 = audio_file2[0]
    list1 = audio_file1[1]
    list2 = audio_file2[1]
    gc = find_greatest_common_divisor(rate1, rate2)
    relative_rate1 = rate1/gc
    relative_rate2 = rate2/gc
    new_rate = rate1
    if rate1 > rate2:
        list1 = shorten_list_for_merge(list1, relative_rate1, relative_rate2)
        new_rate = rate2
    elif rate2 > rate1:
        list2 = shorten_list_for_merge(list2, relative_rate2, relative_rate1)
        new_rate = rate1
    if list1 >= list2:
        list1 = merge_to_long_list(list1, list2)
        to_save = (new_rate, list1)
        return to_save
    else:
        list2 = merge_to_long_list(list2, list1)
        to_save = (new_rate, list2)
        return to_save


def find_greatest_common_divisor(rate1, rate2):
    """
    find greatest common divisor, according to Euclid's algorithm
    :param rate1:
    :param rate2:
    :return:
    """
    while rate1 > 0:
        rate2, rate1 = rate1, rate2 % rate1
    return rate2


def shorten_list_for_merge(fast_list, relative_rate, other_relative_rate):
    """
    shorten the list according to the relative rates.
    assisting unite_two_files
    :param fast_list:
    :param relative_rate:
    :param other_relative_rate:
    :return:
    """
    delete_pair_index = 1
    fast_list_copy = list(fast_list)
    for pair in fast_list:
        if delete_pair_index > other_relative_rate:
            fast_list_copy.remove(pair)
        if delete_pair_index < relative_rate:
            delete_pair_index = delete_pair_index + 1
        else:
            delete_pair_index = 1
    return fast_list_copy


def merge_to_long_list(long_list, short_list):
    """
    while two lists have value, the new value is the average,
    otherwise, the value of the long list
    :param long_list:
    :param short_list:
    :return: the merged list
    """
    for pair_index in range(len(short_list)):
        long_list[pair_index][0] = int((long_list[pair_index][0] +
                                        short_list[pair_index][0]) / 2)
        long_list[pair_index][1] = int((long_list[pair_index][1] +
                                        short_list[pair_index][1]) / 2)
    return long_list


# print(unite_two_files("seinfeld.wav", "seinfeld.wav"))


def compose_wav_menu():
    """
    If user is willing to compose a melody, will enter a valid text file with
     notes and times.
    :return: A wav. file.
    """
    compose_menu_choice = input(
        "enter a text file")
    while not text_file_ok(compose_menu_choice):
        compose_menu_choice = input(
            "Invalid Text file. Please enter a valid choice.")
    composed_file_to_save = create_array_with_composed_melody(compose_menu_choice)
    go_to_intermediate_menu(composed_file_to_save)


def text_file_ok(file_name):
    """
    check if name of text file exist.
    :param file_name:
    :return: True if valid, False if invalid.
    """
    if os.path.isfile(file_name):
        return True
    else:
        return False


def compose_single_note(note, time):
    """
    Creates samples list for a single note, that plays for a certain time.
    :param note: A to G
    :param time: an integer, while 1 represents 1/16 sec.
    :return:
    """
    audio_list = []
    MAX_VOLUME = 32767
    f_A, f_B, f_C, f_D, f_E, f_F, f_G,  = 440, 494, 523, 587, 659, 698, 784
    sample_rate = time * 125
    if note == 'A':
        frequency = f_A
    elif note == 'B':
        frequency = f_B
    elif note == 'C':
        frequency = f_C
    elif note == 'D':
        frequency = f_D
    elif note == 'E':
        frequency = f_E
    elif note == 'F':
        frequency = f_F
    elif note == 'G':
        frequency = f_G
    elif note == 'Q':
        counter = 0
        for i in range(sample_rate):
            while counter <= len(range(sample_rate)):
                audio_list.append([0, 0])
                counter += 1
            return audio_list
    samples_per_cycle = 2000/frequency
    for i in range(sample_rate):
        i = int(MAX_VOLUME * math.sin((2 * math.pi * i) / samples_per_cycle))
        sample = [i,i]
        audio_list.append(sample)
    return audio_list


def create_array_with_composed_melody(txt_file):
    """
    compose melody according to a notes per time list.
    :param txt_file:
    :return: a composed wav file.
    """
    text_file = open(txt_file)
    text_list = text_file.read().split()
    audio_list = []
    counter = 0
    index = 0
    while counter <= len(text_list) / 2:
        note_list = compose_single_note(text_list[index], int(text_list[index + 1]))
        for sample in note_list:
            audio_list.append(sample)
        counter += 1
        index += 2
        if index == (len(text_list)):
            break
    to_save = (2000,audio_list[:-1])
    return to_save


if __name__ == "__main__":
    entrance_menu()