def minMaxArgs(key, operator, *args):    
    if key == None:
        key = lambda x : x   
    minMaxVal = args[0]
    for arg in args:
        cmpKey = key(arg)
        if operator(cmpKey, key(minMaxVal)):
            minMaxVal = arg
    return minMaxVal

def minMaxIter(iterable, operator, key):
        if key == None:
            key = lambda x : x
        count = 0
        for item in iterable:
            if count == 0:
                minMaxVal = item
            count += 1
            cmpKey = key(item)
            if operator(cmpKey, key(minMaxVal)):
                minMaxVal = item
        return minMaxVal

def minmax(operator, *args, **kwargs):
    if not hasattr(operator, "__call__"):
        raise TypeError("operator must be callable")
    if len(args) == 0:
        raise TypeError("expected at least one argument, got 0 arguments")
    key = lambda x : x
    if "key" in kwargs:
        key = kwargs["key"]
        if not hasattr(key, "__call__"):
            raise TypeError("%s is not callable" % type(key))
    elif len(kwargs) > 0:
        raise ValueError("unexpected keyword argument")
    if len(args) == 1 and (hasattr(args[0], "__iter__") or hasattr(args[0], "__getitem__") or hasattr(args[0], "__next__")):
        return minMaxIter(args[0], operator, key)
    else:
        return minMaxArgs(key, operator, *args)

def max(*args, **kwargs):
    return minmax(lambda x, y: x > y, *args, **kwargs)

def min(*args, **kwargs):
    return minmax(lambda x, y: x < y, *args, **kwargs)
