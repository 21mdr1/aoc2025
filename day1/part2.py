input = open("./day1/inputday1.txt", "r").read()

combinations = input.split("\n")
code = 50

zerocounter = 0

for combination in combinations:
    lastCode = code

    if combination[0] == "R":
        code += int(combination[1:])
    elif combination[0] == "L":
        code -= int(combination[1:])

    zeropasses = abs(code) // 100

    if lastCode > 0 and code <= 0:
        zeropasses += 1

    zerocounter += zeropasses
    code %= 100


print(zerocounter)