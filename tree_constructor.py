def TreeConstructor(strArr):
    strArr = list(set(strArr)) # remove duplicates
    parents = [s.split(',')[1][:-1] for s in strArr]
    for parent in parents:
        count = parents.count(parent)
        if count > 2:
            return "false"
    children = [s.split(',')[0][1:] for s in strArr]
    if len(children) != len(set(children)):
        return "false"
    return "true"

print TreeConstructor(raw_input())
