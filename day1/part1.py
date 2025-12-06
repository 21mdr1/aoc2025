input = open("inputday1.txt", "r").read()

combinations = input.split("\n")
code = 50

zerocounter = 0

for combination in combinations:
    # combination = "R50"
    if combination[0] == "R":
        code += int(combination[1:])
    elif combination[0] == "L":
        code -= int(combination[1:])
    
    code %= 100

    if code == 0:
        zerocounter += 1


print(zerocounter);