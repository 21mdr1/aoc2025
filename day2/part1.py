input = open("./day2/inputday2.txt", "r").read()

idRanges = input.split(',')

for idRange in idRanges:
    start, end = map(int, idRange.split("-"))

    