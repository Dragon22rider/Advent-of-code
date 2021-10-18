import re


def ch1(arr):
    temp = []
    count = 0
    for i in range(len(arr)):
        for j in re.split("[\s\n]", arr[i]):
            temp.append(re.split(":", j)[0])
            if temp[-1] == '':
                temp.remove(temp[-1])
        if len(temp) == 8 or (len(temp) == 7) and ("cid" not in temp):
            count += 1
        temp.clear()
    return count


def ch2_check(dic):
    if (not "byr" in dic) or (not "iyr" in dic) or (not "eyr" in dic) or (not "hgt" in dic) or (not "hcl" in dic) or (not "ecl" in dic) or (not "pid" in dic):
        return False
    if int(dic["byr"]) < 1920 or int(dic["byr"]) > 2002:
        return False
    if int(dic["iyr"]) < 2010 or int(dic["iyr"]) > 2020:
        return False
    if int(dic["eyr"]) < 2020 or int(dic["eyr"]) > 2030:
        return False
    if dic["hgt"][-2:] == "cm":
        if int(dic["hgt"][:-2]) < 150 or int(dic["hgt"][:-2]) > 193:
            return False
    elif dic["hgt"][-2:] == "in":
        if int(dic["hgt"][:-2]) < 59 or int(dic["hgt"][:-2]) > 76:
            return False
    else:
        return False
    if dic["hcl"][0] != "#" or len(dic["hcl"][1:]) != 6 or len(re.findall("[g-z]", dic["hcl"][1:])) > 0:
        return False
    eyeColor = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if not dic["ecl"] in eyeColor:
        return False
    if len(dic["pid"]) != 9 or not dic["pid"].isnumeric():
        return False
    return True


def ch2_piece(arr):
    dic = {}
    count = 0
    arr = re.split("[\s\n]", arr)
    if arr[-1] == '':
        arr.remove(arr[-1])
    for i in arr:
        dic[re.split(":", i)[0]] = re.split(":", i)[1]
    if ch2_check(dic):
        return True
    return False

def ch2(arr):
    count = 0
    for i in arr:
        if ch2_piece(i):
            count += 1
    return count


str = ""
arr = []
with open("AdventDay4", "r") as f:
    lines = f.readlines()
    last = lines[-1]
    for line in lines[:-1]:
        if line == "\n":
            arr.append(str)
            str = ""
        else:
            str += line
    arr.append(str + last)

print(ch1(arr))
print(ch2(arr))
