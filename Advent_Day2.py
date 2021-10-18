import re

def ch1(arr):
    count = 0
    for i in arr:
        min = int(re.split("[- ]", i[0])[0])
        max = int(re.split("[- ]", i[0])[1])
        num = str.count(i[1], re.split("[- ]", i[0])[2])
        if num >= min and num <= max:
            count += 1
    return count

def ch2(arr):
    count = 0
    f = False
    for i in arr:
        temp = re.split("[- ]", i[0])
        pos1 = int(temp[0]) - 1
        pos2 = int(temp[1]) - 1
        letter = temp[2]
        if i[1][pos1] == temp[2]:
            f = True
        if i[1][pos2] == temp[2] and f:
            f = False
        elif i[1][pos2] == temp[2] and not f:
            f = True
        if f:
            count += 1
    return count

arr = []
x = input()
while x != "-1":
    arr.append(re.split(": ", x))
    x = input()

print(ch1(arr))
print(ch2(arr))