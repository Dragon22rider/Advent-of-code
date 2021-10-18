def ch1(arr):
    x = 0
    count = 0
    for y in range(len(arr)):
        if arr[y][x%len(arr[y])] == "#":
            count += 1
        x += 3
    return count

def ch2_part1(arr, move, down):
    x = 0
    count = 0
    for y in range(0, len(arr), down):
        if arr[y][x%len(arr[y])] == "#":
            count += 1
        x += move
    return count

def ch2_part2(arr):
    slp1 = ch2_part1(arr, 1, 1)
    slp2 = ch2_part1(arr, 3, 1)
    slp3 = ch2_part1(arr, 5, 1)
    slp4 = ch2_part1(arr, 7, 1)
    slp5 = ch2_part1(arr, 1, 2)
    return slp1*slp2*slp3*slp4*slp5

arr = []
x = input()
while x != "-1":
    arr.append(x)
    x = input()

print(ch1(arr))

print(ch2_part2(arr))