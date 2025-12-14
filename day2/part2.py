input = open("./day2/inputday2.txt", "r").read()
idRanges = input.split(',')

total = 0

for idRange in idRanges:
    start, end = map(int, idRange.split("-"))

    for num in range(start, end+1):
        numLength = len(str(num))

        for bundles in range(2, numLength + 1):
            if numLength % bundles != 0:
                continue

            smallNum = str(num)[:(numLength // bundles)]

            if int(smallNum * bundles) == num:
                total += num
                break

print(total)