import re


def check_In_Range(lst, sum):
    for i in lst:
        for j in lst:
            if j + i == sum:
                return True
    return False


def ch1(lst, prem):
    for i in range(prem, len(lst)):
        if not check_In_Range(lst[i - prem: i], lst[i]):
            return lst[i]
    return None


def largest_In_Range(lst):
    min = lst[0]
    max = 0
    for i in lst:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max


def ch2(lst, sumF):
    sumOf = 0
    nums = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sumOf += lst[j]
            if sumOf > sumF:
                break
            if sumOf == sumF:
                return sum(list(largest_In_Range(lst[i: j + 1])))
        sumOf = 0


with open("adventDay9", "r") as f:
    lines = f.readlines()
    lst = []
    for line in lines:
        lst.append(re.split("[ \n]", line))
    for i in range(len(lst)):
        lst[i] = list(filter(lambda x: x != "" and x is not None, lst[i]))
        lst[i] = int("".join(lst[i]))

weakness = ch1(lst, 25)
print(weakness)
print(ch2(lst, weakness))
