# First option

def insert_zeros(seq):
    """delim lucky series by zeros"""
    lst = [int(x) for x in str(seq)]
    for i in range(len(lst)):
        if lst[i] != 5 and lst[i] != 6: 
            lst[i] = 0
    temp = ''.join(str(e) for e in lst)
    return temp

def list_of_seq(str):
    """keep list with not all same digits"""
    un_list = []
    for i in str.split('0'):
        if len(set(i)) > 1:
            un_list.append(i)
    return un_list

def get_longest(lst):
    """get longest lucky series"""
    if len(lst) > 0:
        return max(lst, key=len)
    else:
        return 0

var = input("Enter sequence: ")
print("Longest lucky series: {0}".format(get_longest(list_of_seq(insert_zeros(var)))))

# Second option

import re

def get_lucky_seq(seq):
    """get longest lucky series"""
    temp = re.split(r'[0-47-9]', str(seq))
    temp2 = [i for i in temp if len(set(i)) == 2]
    if len(temp2) > 0:
        return max(temp2, key=len)
    else:
        return 0

var = input("Enter sequence: ")
print("Longest lucky series: {0}".format(get_lucky_seq(var)))