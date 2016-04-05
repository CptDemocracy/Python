""" ALPHA VERSION
As of currently, this version of the calculator does not address expressions such as: "1 + --1" or "1 + -(-1)" properly.
This will be addressed in the next version of the calculator
"""
import operator

SUPPORTED_OPERATORS = (     \
                            \
    {'+': operator.add,     \
     '-': operator.sub},    \
                            \
    {'/': operator.div,     \
     '*': operator.mul,     \
     'mod': operator.mod},  \   
                            \
    {'^': operator.pow })   \

def IsTokenOperator(token):
    for opset in SUPPORTED_OPERATORS:
        if token in opset:
            return True
    return False

def GetTokenOperatorFunc(token):
    for opset in SUPPORTED_OPERATORS:
        if token in opset:
            return opset[token]
    raise ValueError("token not a supported operator")
    
def ComparePrecedence(operator1, operator2):
    p1 = -1
    p2 = -1
    i = 0
    for opset in SUPPORTED_OPERATORS:
        if operator1 in opset:
            p1 = i
        if operator2 in opset:
            p2 = i
        if p1 > -1 and p2 > -1 and p1 == p2:
            return 0
        i += 1
    if p1 > p2:
        return 1
    elif p1 < p2:
        return -1
    return 0

def TokenizeExp(exp):
    explen = len(exp)
    if explen < 1:
        return []
    tokens = []
    token  = [exp[0]]
    i = 1   
    while i < explen:        
        if ((exp[i].isdigit() and exp[i - 1].isdigit())
            or (exp[i].isalpha() and exp[i - 1].isalpha())
            or (exp[i].isdigit() and exp[i - 1].isalpha())
            or (exp[i].isalpha() and exp[i - 1].isdigit())
            or (exp[i].isdigit() and exp[i - 1] == '.')
            or (exp[i] == '.' and exp[i - 1].isdigit())):
            token.append(exp[i])
        else:
            if len(token) > 0:
                tokens.append("".join(token))
            if not exp[i].isspace():
                token = [exp[i]]
            else:
                token = []
        if i == explen - 1 and len(token) > 0:
            tokens.append("".join(token))
            break
        i += 1
    return tokens

def InfixToRPN(exp):
    """uses Dijkstra's "Shunting Yard" Algorithm"""
    
    outputQueue = []
    operatorStack = []

    tokens = TokenizeExp(exp)

    for token in tokens:
        try:
            # if token is a number
            num = float(token)
            outputQueue.append(num)
        except ValueError:
            # token not a number
            if IsTokenOperator(token):
                # if operator
                while (len(operatorStack)
                       and ComparePrecedence(token, operatorStack[-1]) <= 0):
                    operator = operatorStack.pop()
                    outputQueue.append(operator)
                operatorStack.append(token)
            elif token == '(':
                operatorStack.append(token)
            elif token == ')':
                try:
                    while operatorStack[-1] != '(':
                        operator = operatorStack.pop()
                        outputQueue.append(operator)
                    operatorStack.pop()
                except IndexError:
                    raise ValueError("misplaced parentheses in the expression")
            else:
                raise ValueError("expression in a wrong format")

    while len(operatorStack) > 0:
        operator = operatorStack.pop()
        if operator == '(':
            raise ValueError("misplaced parenthesis in the expression")
        outputQueue.append(operator)

    return outputQueue

def ParseRPN(exp):
    operandsStack = []
    
    tokens = TokenizeExp(exp)
    
    for token in tokens:
        try:
            # if token is a number
            value = float(token)
            operandsStack.append(value)
        except ValueError:
            if IsTokenOperator(token):
                operator = GetTokenOperatorFunc(token)
                if len(operandsStack) > 1:                    
                    operand2 = operandsStack.pop()
                    operand1 = operandsStack.pop()
                    value = operator(operand1, operand2)
                else:
                    value = operator(0, operandsStack.pop())
                operandsStack.append(value)
            else:
                raise ValueError("expression in a wrong format")
    return operandsStack.pop()

def ParseInfix(exp):
    rpnOutputQueue = InfixToRPN(exp)
    return ParseRPN(" ".join([str(token) for token in rpnOutputQueue]))

while True:
    try:
        exp = raw_input(">>> ")
        ret = ParseInfix(exp)
        print ret
    except ValueError:
        print "error"
