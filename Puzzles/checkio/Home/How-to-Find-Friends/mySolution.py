def check_connection(network, name1, name2):
    SEPARATOR = '-'
    pairs = {}
    for pair in network:
        pairTuple = pair.split(SEPARATOR)
        if pairTuple[0] in pairs:
            pairs[pairTuple[0]].append(pairTuple[1])
        else:
            pairs[pairTuple[0]] = [pairTuple[1]]
        if pairTuple[1] in pairs:
            pairs[pairTuple[1]].append(pairTuple[0])
        else:
            pairs[pairTuple[1]] = [pairTuple[0]]                               
    marked = {}    
    stack  = [[name1]]
    while len(stack) > 0:
        for friend in stack.pop():
            if friend == name2:
                return True
            if friend in pairs and friend not in marked:
                stack.append(pairs[friend])
                marked[friend] = 1        
    return False
