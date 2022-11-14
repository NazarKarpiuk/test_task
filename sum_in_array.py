# First option

def find_pairs_v1(lst, S): 
    res = []
    while lst:
        temp = lst.pop()
        diff = S - temp
        if diff in lst:
            res = ((diff, temp))
            return res
    return -1

# Second option
    
def find_pairs_v2(lst, S):
    res = []
    for i in range(0, len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if (lst[i] + lst[j] == S):
                res = ((lst[i],lst[j]))
                return res
    return -1

# Third option - BEST ONE

def find_pairs_v3(lst, S):
    res = []
    lst.sort()
    (low, high) = (0, len(lst) - 1)
    while low < high:
        if lst[low] + lst[high] == S:
            res  = ((lst[low], lst[high]))
            return res
        if lst[low] + lst[high] < S:
            low = low + 1
        else:
            high = high - 1
    return -1