def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        if len(current) == 0:
            result["/".join(path)] = ""
        else: 
            for k, v in current.items():
                if isinstance(v, dict):
                    stack.append((path + (k,), v))
                else:
                    result["/".join((path + (k,)))] = v
    return result
