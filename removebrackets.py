def RemoveBrackets(str): 
    stack =[]
    count = 0
    for c in str:
        if c == "(":
            stack.append("(")
        elif c == ")" and len(stack)==0:
            count += 1
        elif c == ")":
            stack.pop()
    return count+len(stack)
