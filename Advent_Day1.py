def ch1(arr):
    finalNum = 0
    for i in arr:
        for j in arr:
            if int(i) + int(j) == 2020:
                finalNum = int(i) * int(j)
                break
    return finalNum

def ch2(arr):
    finalNum = 0
    for i in arr:
        for j in arr:
            for k in arr:
                if int(i) + int(j) + int(k) == 2020:
                    finalNum = int(i) * int(j) * int(k)
                    break
    return finalNum

arr = []
x = input()
while x != "-1":
    arr.append(x)
    x = input()

print(ch1(arr))
print(ch2(arr))

