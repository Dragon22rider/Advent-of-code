import re

def ch1(lst):
    acc = 0
    i = 0
    order = []
    for i in range(len(lst)):
        order.append(0)
        i += 1
    i = 0
    while i < len(lst):
        order[i] += 1
        if order[i] > 1:
            return acc
        if lst[i][0] == "acc":
            acc += int(lst[i][1])
            i += 1
        elif lst[i][0] == "jmp":
            i += int(lst[i][1])
        else:
            i += 1

def ch2():
    return

with open("AdventDay8", "r") as f:
    lines = f.readlines()
    lst = []
    for line in lines:
        lst.append(re.split("[ \n]", line))
    for i in range(len(lst)):
        lst[i] = list(filter(lambda x: x != "" and x is not None, lst[i]))

print(ch1(lst))
