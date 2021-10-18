import re, copy


def newSeat(sit1, sit2):
    for y in range(len(sit1)):
        for x in range(len(sit1[y])):
            if sit1[y][x] == "L":
                f = False
                if x > 0 and sit1[y][x - 1] == "#": f = True
                if x + 1 < len(sit1[y]) and sit1[y][x + 1] == "#": f = True
                if y > 0 and sit1[y - 1][x] == "#": f = True
                if y + 1 < len(sit1) and sit1[y + 1][x] == "#": f = True
                if x + 1 < len(sit1[y]) and y > 0 and sit1[y - 1][x + 1] == "#": f = True
                if x + 1 < len(sit1[y]) and y + 1 < len(sit1) and sit1[y + 1][x + 1] == "#": f = True
                if x > 0 and y + 1 < len(sit1) and sit1[y + 1][x - 1] == "#": f = True
                if x > 0 and y > 0 and sit1[y - 1][x - 1] == "#": f = True
                if not f:
                    sit2[y][x] = "#"
                else:
                    sit2[y][x] = "L"
            elif sit1[y][x] == "#":
                count = 0
                if x > 0 and sit1[y][x - 1] == "#": count += 1
                if x + 1 < len(sit1[y]) and sit1[y][x + 1] == "#": count += 1
                if y > 0 and sit1[y - 1][x] == "#": count += 1
                if y + 1 < len(sit1) and sit1[y + 1][x] == "#": count += 1
                if x + 1 < len(sit1[y]) and y > 0 and sit1[y - 1][x + 1] == "#": count += 1
                if x + 1 < len(sit1[y]) and y + 1 < len(sit1) and sit1[y + 1][x + 1] == "#": count += 1
                if x > 0 and y + 1 < len(sit1) and sit1[y + 1][x - 1] == "#": count += 1
                if x > 0 and y > 0 and sit1[y - 1][x - 1] == "#": count += 1
                if count >= 4:
                    sit2[y][x] = "L"
                else:
                    sit2[y][x] = "#"
            elif sit1[y][x] == ".":
                sit2[y][x] = "."


def ch1(lst1, lst2):
    while lst1 != lst2:
        newSeat(lst1, lst2)
        if lst1 == lst2:
            break
        lst1 = copy.deepcopy(lst2)
        for i in range(len(lst2)):
            for j in range(len(lst2[i])):
                lst2[i][j] = ""
    count = 0
    for y in lst1:
        for x in y:
            if x == "#":
                count += 1
    return count


def newSeat(sit1, sit2):
    for y in range(len(sit1)):
        for x in range(len(sit1[y])):
            if sit1[y][x] == "L":
                f = False
                ix = x
                iy = y
                while x - i > 0 and sit1[y][x - i] == ".":   
                    if sit1[y][x - i] == "#": f = True
                if x + 1 < len(sit1[y]) and sit1[y][x + 1] == "#": f = True
                if y > 0 and sit1[y - 1][x] == "#": f = True
                if y + 1 < len(sit1) and sit1[y + 1][x] == "#": f = True
                if x + 1 < len(sit1[y]) and y > 0 and sit1[y - 1][x + 1] == "#": f = True
                if x + 1 < len(sit1[y]) and y + 1 < len(sit1) and sit1[y + 1][x + 1] == "#": f = True
                if x > 0 and y + 1 < len(sit1) and sit1[y + 1][x - 1] == "#": f = True
                if x > 0 and y > 0 and sit1[y - 1][x - 1] == "#": f = True
                if not f:
                    sit2[y][x] = "#"
                else:
                    sit2[y][x] = "L"
            elif sit1[y][x] == "#":
                count = 0
                if x > 0 and sit1[y][x - 1] == "#": count += 1
                if x + 1 < len(sit1[y]) and sit1[y][x + 1] == "#": count += 1
                if y > 0 and sit1[y - 1][x] == "#": count += 1
                if y + 1 < len(sit1) and sit1[y + 1][x] == "#": count += 1
                if x + 1 < len(sit1[y]) and y > 0 and sit1[y - 1][x + 1] == "#": count += 1
                if x + 1 < len(sit1[y]) and y + 1 < len(sit1) and sit1[y + 1][x + 1] == "#": count += 1
                if x > 0 and y + 1 < len(sit1) and sit1[y + 1][x - 1] == "#": count += 1
                if x > 0 and y > 0 and sit1[y - 1][x - 1] == "#": count += 1
                if count >= 5:
                    sit2[y][x] = "L"
                else:
                    sit2[y][x] = "#"
            elif sit1[y][x] == ".":
                sit2[y][x] = "."


with open("AdventDay11", "r") as f:
    lines = f.readlines()
    temp = []
    for line in range(len(lines)):
        lines[line] = re.split("\n", lines[line])
        lines[line] = str("".join(list(filter(lambda x: x != "" and x is not None, lines[line]))))
        lines[line] = list(filter(lambda x: x != "", re.split("", lines[line])))

lst1 = lines
lst2 = copy.deepcopy(lst1)
for i in range(len(lst2)):
    for j in range(len(lst2[i])):
        lst2[i][j] = ""
print(ch1(lst1, lst2))
