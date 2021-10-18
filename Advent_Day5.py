import re

def ch1_seatNum(str):
    row = [0, 127]
    col = [0, 7]
    for i in str:
        if i == "F":
            row[1] = sum(row)/2
        if i == "B":
            row[0] = sum(row)/2
        if i == "L":
            col[1] = sum(col)/2
        if i == "R":
            col[0] = sum(col)/2
    return round(sum(row)/2) * 8 + round(sum(col)/2)

def ch1_checkAllSeats(arr):
    max = 0
    for i in arr:
        temp = ch1_seatNum(i)
        if temp > max:
            max = temp
    return max

def ch2_seatedArr(arr):
    newArr = []
    for i in arr:
        newArr.append(ch1_seatNum(i))
    return newArr

def ch2(arr):
    newArr = ch2_seatedArr(arr)
    newArr.sort()
    for i in range(len(newArr)-1):
        if newArr[i] == newArr[i+1]-2:
            return newArr[i]+1

arr = []
with open("AdventDay5", "r") as f:
    lines = f.readlines()
    temp = []
    for i in range(len(lines)):
        arr.append(re.split("\n", lines[i])[0])

print(ch1_checkAllSeats(arr))
print(ch2(arr))