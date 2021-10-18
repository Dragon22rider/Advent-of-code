import re, collections

def ch1_arr(arr):
    for i in range(len(arr)):
        temp = re.split("\n", arr[i])
        if '' in temp:
            temp.remove('')
        arr[i] = set(''.join(temp))
    return arr

def ch1(arr):
    arr = ch1_arr(arr)
    count = 0
    for i in arr:
        count += len(i)
    return count

def ch2_Crossover(arr):
    count = 0
    finalCount = 0
    temp = arr[0]
    for j in temp:
        for i in arr:
            count += i.count(j)
        if count == len(arr):
            finalCount += 1
        count = 0
    return finalCount

def ch2(arr):
    for i in range(len(arr)):
        temp = re.split("\n", arr[i])
        if '' in temp:
            temp.remove('')
        arr[i] = temp
    count = 0
    for i in arr:
        count += ch2_Crossover(i)
    return count


str = ""
arr = []
with open("AdventDay6", "r") as f:
    lines = f.readlines()
    last = lines[-1]
    for line in lines[:-1]:
        if line == "\n":
            arr.append(str)
            str = ""
        else:
            str += line
    arr.append(str + last)

print(ch1(arr.copy()))
print(ch2(arr))