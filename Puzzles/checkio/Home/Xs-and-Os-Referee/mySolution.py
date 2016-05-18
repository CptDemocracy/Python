TTT_X = "X"
TTT_O = "O"
TTT_D = "D"
TTT_EMPTY = "."

def checkio(grid):
    gridSize = len(grid)
    
    if gridSize <= 0:
        raise TypeError("grid cannot be empty")
    if gridSize != len(grid[0]):
        raise TypeError("a 2-dim grid expected")
    
    symbols = [TTT_X, TTT_O]
    for symbol in symbols:
        
        #check diagonally
        count = 0
        col = 0
        for row in range(gridSize):
            if grid[row][col].upper() != symbol.upper():
                break
            count += 1
            col += 1
        if count == gridSize:
            return symbol

        count = 0
        col = gridSize - 1
        for row in range(gridSize):
            if grid[row][col].upper() != symbol.upper():
                break
            count += 1
            col -=1
        if count == gridSize:
            return symbol

        #check rows        
        for row in range(gridSize):
            count = 0
            for col in range(gridSize):
                if grid[row][col].upper() != symbol.upper():
                    break
                count += 1
            if count == gridSize:
                return symbol

        #check cols
        for col in range(gridSize):
            count = 0
            for row in range(gridSize):
                if grid[row][col].upper() != symbol.upper():
                    break
                count += 1
            if count == gridSize:
                return symbol
            
    return TTT_D
