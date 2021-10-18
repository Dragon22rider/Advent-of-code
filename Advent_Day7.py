import re

def getDict_Part1(file):
    str = ""
    arr = []
    with open(file, "r") as f:
        lines = f.readlines()

    lst = {}
    for line in lines:
        if "no other bags" in line:
            temp = re.split("bags contain no other bags\.\n?", line)
        else:
            temp = re.split("(?: bags contain \d? | bags?, \d? | bags?\.\n?)", line)
        code = temp[0]
        bags = list(filter(lambda x: x != "", temp))[1:]
        lst[code] = bags
    return lst

def check(dic, color, count):
    for key in dic:
        if color in dic[key]:
            dic[key] = []
            count = check(dic, key, count) + 1
    return count

def ch1(file):
    dic = getDict_Part1(file)
    return check(dic, "shiny gold", 0)

def getDict_part2(file):
    str = ""
    arr = []
    with open(file, "r") as f:
        lines = f.readlines()

    lst = {}
    for line in lines:
        if "no other bags" in line:
            temp = re.split("bags contain no other bags\.\n?", line)
        else:
            temp = re.split("(?: bags contain (\d?) | bags?, (\d?) | bags?\.\n?)", line)
        code = temp[0].strip()
        bags = list(filter(lambda x: x != "" and x is not None, temp))[1:]
        lst[code] = bags
    return lst

def newDic(dic):
    temp = 0
    newDic = {}
    for key in dic:
        for i in dic[key]:
            if i.isnumeric():
                temp = int(i)
            else:
                newDic[i] = temp
        dic[key] = newDic
        newDic = {}
    return dic

def check2(dic, color, count):
    if dic[color] == {}:
        return 1
    for key in dic[color]:
        count += check2(dic, key, 0)*dic[color][key]
    if color != "shiny gold":
        count += 1
    return count

def ch2(file):
    dic = getDict_part2(file)
    dic = newDic(dic)
    return check2(dic, "shiny gold", 0)

print(ch1("AdventDay7"))
print(ch2("AdventDay7"))