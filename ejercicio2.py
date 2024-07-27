def isBalanced(string):
    openSign = ["(", "{", "["]
    closeSign = [")", "}", "]"]

    signCounter = [0, 0, 0]

    for c in string:
        pointer = 0
        while pointer <= 2:
            if c == openSign[pointer]:
                signCounter[pointer] += 1
            elif c == closeSign[pointer]:
                signCounter[pointer] -= 1
            pointer += 1

    if signCounter[0] == signCounter[1] == signCounter[2] == 0:
        return True
    else:
        return False


def checkExp(file):
    lineCount = 0

    for x in file:
        balance = False
        lineCount += 1
        print(f"Expression {lineCount}: {x}")
        balance = isBalanced(x)

        if balance:
            print("The expression is balanced.")
        else:
            print("The expression is not balanced.")        
        print("======================================")

file = open("example.txt", "r")
checkExp(file)

file.close()