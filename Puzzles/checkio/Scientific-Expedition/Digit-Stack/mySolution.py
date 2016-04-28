import re

class StackCommand(object):
    def execute(self, stack, strCmd):
        raise NotImplementedError("abstract class Command")

    def isCommand(self, strCmd):
        raise NotImplementedError("abstract class Command")

class StackPushCommand(StackCommand):
    def __init__(self):
        self._cmdPattern = re.compile("PUSH (\d)")

    def execute(self, stack, strCmd):
        m = re.match(self._cmdPattern, strCmd)
        if m == None:
            raise ValueError("syntax error")
        try: 
            num = int(m.group(1))
        except ValueError as e:
            raise e
        stack.append(num)        

    def isCommand(self, strCmd):
        return re.match(self._cmdPattern, strCmd) != None

class StackPeekCommand(StackCommand):
    def __init__(self):
        self._cmdPattern = re.compile("PEEK")

    def execute(self, stack, strCmd):
        if not self.isCommand(strCmd):
            raise ValueError("syntax error")
        if len(stack) == 0:
            return 0
        return stack[-1]

    def isCommand(self, strCmd):
        return re.match(self._cmdPattern, strCmd) != None

class StackPopCommand(StackCommand):
    def __init__(self):
        self._cmdPattern = re.compile("POP")

    def execute(self, stack, strCmd):
        if not self.isCommand(strCmd):
            raise ValueError("syntax error")
        if len(stack) == 0:
            return 0
        return stack.pop()

    def isCommand(self, strCmd):
        return re.match(self._cmdPattern, strCmd) != None
    
def digit_stack(commands):
    if len(commands) == 0:
        return 0
    cmdObjects = [StackPeekCommand(),
                  StackPushCommand(),
                  StackPopCommand()]
    stack = []
    count = 0
    for command in commands:
        is_valid = False
        for cmdObject in cmdObjects:
            is_valid = is_valid or cmdObject.isCommand(command)
            if is_valid:
                result = cmdObject.execute(stack, command)
                if type(cmdObject) in (StackPopCommand, StackPeekCommand) and type(result) == int:
                    count += result
                break
        if not is_valid:
            raise ValueError("syntax error")
    return count
