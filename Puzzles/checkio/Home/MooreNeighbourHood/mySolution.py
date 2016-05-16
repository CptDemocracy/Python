EMPTY_CELL     = 0
NEIGHBOUR_CELL = 1

def count_neighbours(grid, x_pos, y_pos, radius = 1):
    neighbour_count = 0
    for row in range(x_pos - radius, x_pos + radius + 1):
        for col in range(y_pos - radius, y_pos + radius + 1):
            try:
                if row < 0 or col < 0: 
                    raise IndexError()
                if grid[row][col] == NEIGHBOUR_CELL:
                    if row == x_pos and col == y_pos:
                        # if we are at (x_pos, y_pos) and there's a 
                        # neighbor cell at these coords, don't count it
                        pass
                    else:
                        neighbour_count += 1
            except IndexError:
                pass
    return neighbour_count
