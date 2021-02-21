###################################
# FILE : ex3.py
# WRITER : Ayelet Avraham, ayeletavr, 313451932
# EXERCISE : intro2cs ex3 2019
# DESCRIPTION : Several functions that contains lists,
# for and while loops, and more...
##################################

#ex. 1: Converting sevral inputs into one List.
def input_list():
    string_from_user = input()
    list_of_strings = []
    list_of_strings.append(string_from_user)
    if string_from_user == '':
        return list_of_strings
    else:
        while string_from_user != '':
            string_from_user = input()
            list_of_strings.append(string_from_user)
            continue
        return list_of_strings[:-1]

#Ex. 2: Function that converts Lists items into one string
def concat_list(str_list):
    finalStr = ""
    for str in str_list:
        str = ''+str
        finalStr += str
    return finalStr

#print(concat_list(['Hello World', 'What', ' ', 'a nice day', '3']))

#Ex.3: Function that finds max value from a list.
def maximum(num_list):
    if num_list == []:
        return None
    else:
        return max(num_list)

#Ex. 4: Function that finds lists with cyclic permutation.
def cyclic(lst1, lst2):
    def same_nums(lst1,lst2): #to check if 2 lists contains same nums
        copylst1 = lst1[:].sort()
        copylst2 = lst2[:].sort()
        if copylst1 == copylst2:
            return True
        else:
            return False
    def int_list_to_str_list(str_list): #to convert from int to str
        n = 0
        while n < len(str_list):
            str_list = str_list[:]
            str_list[n] = str(str_list[n])
            n += 1
        return (str_list)
    if len(lst1) != len(lst2): #False for sure
        return False
    elif lst1 == lst2: #True for sure
        return True
    else:
        if same_nums(lst1,lst2) == False: #False for sure
            return False
        else: #maybe different order, maybe cyclic permutation
            strlst1 = int_list_to_str_list(lst1)
            strlst2 = int_list_to_str_list(lst2)
            sep = ","
            str1 = sep.join(strlst1)
            str2 = sep.join(strlst2)
            str2 = str2 + ','
            str2 = 2*str2
            if str1 in str2:
                return True
            else:
                return False
print(cyclic([1, 2, 3, 4],[3, 4, 1, 2]))

#Ex. 5: Function that plays seven boom.
def seven_boom(n):
    def int_list_to_str_list(str_list): #to convert from int to str
        n = 0
        while n < len(str_list):
            str_list[n] = str(str_list[n])
            n += 1
        return (str_list)
    seven_boom_range = range(1,n+1)
    seven_boom_list = []
    for i in seven_boom_range:
        if i % 7 == 0:
            i = "boom"
            seven_boom_list.append(i)
            continue
        else:
            str(i)
            seven_boom_list.append(i)
            continue
    #ints are still ints n seven_boom_list:
    seven_boom_list = int_list_to_str_list(seven_boom_list)
    return seven_boom_list

#Ex.6 Function that returns histogram.
def histogram(n, num_list):
    histogram = []
    for i in range(n):
        i = 0
        histogram.append(i)
    #summing the repeitations:
    for num in num_list:
        if num in range(n):
            histogram[num] += 1

    return histogram

#Ex. 7: Function that finds prime divisors.
def prime_factors(n):
    divisors_list = []
    for divisor in range(2,n+1):
        while n % divisor == 0:
            n = n / divisor
            divisors_list.append(divisor)
    return divisors_list

#Ex. 8: Function that calculates cartesian product.
def cartesian(lst1, lst2):
    list_of_pairs = []
    for i in lst1:
        for j in lst2:
            sub_list = [i,j]
            list_of_pairs.append(sub_list)
    return list_of_pairs


#Ex. 9: Function that finds pair with sum n from a list.
def pairs(num_list, n):
    list_of_pairs = []
    for m in num_list:
        for k in num_list:
            pair = [m,k]
            if m != k and m + k == n:
                list_of_pairs.append(pair)
#to remove same products:
    for pair1 in list_of_pairs:
        pair1.sort()
        for pair2 in list_of_pairs:
            if pair1 == pair2:
                list_of_pairs.remove(pair2)
    return list_of_pairs