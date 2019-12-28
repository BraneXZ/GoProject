from dlgo.gotypes import Point

def is_point_an_eye(board, point, color):
    if board.get(point) is not None: #An eye is an empty point
        return False
    for neighbor in point.neighbors(): #All adjacent pointts must contain friendly stones
        if board.is_on_grid(neighbor):
            neighbor_color = board.get(neighbor)
            if neighbor_color != color:
                return False
    
    # We must control three out of four corners if
    # the point is in the middle of hte board; on the edge,
    # you must control all corners
    friendly_corners = 0 
    off_board_corners = 0        
    corners = [
            Point(point.row - 1, point.col - 1),
            Point(point.row - 1, point.col + 1),
            Point(point.row + 1, point.col - 1),
            Point(point.row + 1, point.col + 1)]
    for corner in corners:
        if board.is_on_grid(corner):
            corner_color = board.get(corner)
            if corner_color == color:
                friendly_corners += 1
        else:
            off_board_corners += 1
    if off_board_corners > 0:
        return off_board_corners + friendly_corners == 4
    return friendly_corners >= 3