import string

def parse_chessboard_coord(coord):
    try:
        col = string.ascii_lowercase.index(coord[0])
        row = int(coord[1]) - 1
        return (row, col)
    except ValueError as e:
        raise e

def safe_pawns(coord_pairs_set):
    try:
        coords = []

        # parse coords
        for coord_pair in coord_pairs_set:
            coord = parse_chessboard_coord(coord_pair)
            coords.append(coord)

        # convert coords from list to set
        coords = set(coords)
        
        # calculate safe pawns
        safe_count = 0
        
        for coord in coords:
            if (coord[0] - 1, coord[1] - 1) not in coords:
                if (coord[0] - 1, coord[1] + 1) not in coords:
                    continue
            safe_count += 1
        return safe_count            
    except (TypeError, ValueError) as e:
        raise e
