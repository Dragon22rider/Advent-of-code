import re


def ch1(lst, adapter):
    jolts = 0
    dic = {1: 0, 2: 0, 3: 0}
    while jolts < adapter:
        if jolts + 1 in lst:
            jolts += 1
            dic[1] += 1
        elif jolts + 2 in lst:
            jolts += 2
            dic[2] += 1
        elif jolts + 3 in lst:
            jolts += 3
            dic[3] += 1
        if jolts + 3 == adapter:
            jolts += 3
            dic[3] += 1
    return dic[1] * dic[3]


# The place you put the adapter in, the level of volts
# is 0, meaning the lowest the adapter's level could be
# is: 1,2,3 (biggest of 3 difference) and adapter is
# the biggest adapter + 3 (the difference between the
# port and the "charger"
def is_Pos(lst, adapter):
    jolts = 0
    if not lst:
        return False
    while jolts < adapter:
        if jolts + 1 in lst:
            jolts += 1
        elif jolts + 2 in lst:
            jolts += 2
        elif jolts + 3 in lst:
            jolts += 3
        elif jolts + 3 == adapter:
            jolts += 3
        else:
            return False
    return True

# Recursive - checks if every possible version of a list is
# possible, if yes, if every version of that new list is possible
# Then adds it to a big array that has every version that is
# possible that's been checked (so it doesn't check the same ones
# Does that until it's not possible
# i.e if the first list is: [1,2,4,5,6,9]
# the list: [1,4,5,6,9] is also possible
# So checks that, and then also: [1,4,6,9]
# Then it's not possible
def ch2(lst, full_lst, max):
    if lst not in full_lst:
        full_lst.append(lst)
    for x in range(len(lst)):
        temp = lst[:x] + lst[x + 1:]
        if is_Pos(temp, max + 3) and temp not in full_lst:
            full_lst.append(temp)
            ch2(temp, full_lst, max)
    return len(full_lst)

# Creates a list of ints, that is the same as the file numbers:
# i.e if the lines show: 1,2,3,4 it'll create a list called lst
# That looks like this: lst = [1,2,3,4]
with open("adventDay10", "r") as f:
    lines = f.readlines()
    lst = []
    for line in lines:
        lst.append(re.split("[ ,\n]", line))
    for i in range(len(lst)):
        lst[i] = list(filter(lambda x: x != "" and x is not None, lst[i]))
        lst[i] = int("".join(lst[i]))

print(lst)
# print(ch1(lst, max(lst)+3))
fLst = []
# print(ch2(lst, fLst, max(lst)))