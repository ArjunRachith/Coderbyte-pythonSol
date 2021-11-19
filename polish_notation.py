def polish_eval(strArr):
    split_arr = strArr.split()
    stack = []

    for i in split_arr:
        if re.match ([\+\-\*\/], i):
            val2 = stack.pop()
            val1 = stack.pop()
						var = str(val1)+i+str(val2)
            stack.append(eval(var))
        else:
            stack.append(int(i))
    return stack[0]
