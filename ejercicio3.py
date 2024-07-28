def checkPrecedence(c):
    precedenceDict = {
        "(": 1,
        "|": 2,
        "?": 4,
        "*": 4,
        "+": 4
    }

    if c in precedenceDict.keys():
        return precedenceDict.get(c)
    else:
        return 0

def transRegex(regex):
    res = ""
    stack = []

    for c in regex:

        if c == "(":
            stack.append(c)

        elif c == ")":
            tmp = stack.pop()
            stack.append(tmp)
            while tmp != "(":
                if stack:
                    res += stack.pop()
                else:
                    break
            if stack:
                stack.pop()

        else:
            while len(stack) > 0:
                tmp = stack.pop()
                stack.append(tmp)
                lastChar = tmp
                lastCharPrec = checkPrecedence(lastChar)
                currCharPrec = checkPrecedence(c)

                if lastCharPrec >= currCharPrec:
                    res += stack.pop()
                else:
                    break
        
        stack.append(c)
    
    while len(stack) > 0:
        res += stack.pop()

    return res

file = open("example2.txt", "r")

count = 0
for regex in file:
    count += 1
    postfixExp = transRegex(regex)
    print(f"Infix expression: {regex} ---- Postfix expression: {postfixExp}")

file.close()