input = open("./day2/inputday2.txt", "r").read()
idRanges = input.split(',')

total = 0

for idRange in idRanges:
    start, end = map(int, idRange.split("-"))

    if len(str(start)) % 2: # 1
        startHalf = "1" + "0" * (len(str(start)) // 2)
    else:
        startHalf = str(start)[:len(str(start))//2]

    while True:
        num = int(startHalf + startHalf)

        if num > end:
            break
        
        if num >= start:
            total += num
        
        startHalf = str(int(startHalf) + 1)

print(total)
    