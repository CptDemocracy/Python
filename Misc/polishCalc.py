import operator

def ParsePolishExpression(exp):
    if type(exp) != str:
        raise TypeError("expression must be of type string")
    try:

        supportedOperators = { '/': operator.div,\
                               '*': operator.mul,\
                               '+': operator.add,\
                               '-': operator.sub,\
                               '%': operator.mod }
        operators = []
        operands = []
        expLen = len(exp)
        result = 0.0
        i = 0
        c = exp[i]
        
        while (i < expLen):
            c = exp[i]
            if c in supportedOperators:
                op = supportedOperators[c]
                operators.append(op)
                break
            i += 1
        i += 1
        
        while len(operators) > 0:
            c = exp[i]
            if c in supportedOperators:
                op = supportedOperators[c]
                operators.append(op)
            elif c.isdigit() or c == '.':
                start = i
                while i < expLen:
                    c = exp[i]
                    if not c.isdigit() and c not in supportedOperators:
                        break
                    i += 1
                end = i
                i -= 1
                lit = exp[start:end]
                val = float(lit)
                operands.append(val)
                
            c = exp[i]
            if c == ')' or i == expLen - 1:            
                op = operators.pop()                   
                value = reduce(op, operands)
                operands = []
                operands.append(value)
            i += 1
        return operands.pop()
    except ValueError as e:
        raise e
