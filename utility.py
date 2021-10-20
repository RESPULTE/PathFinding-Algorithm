from .type_hints import *

# _______________________________________HELPER FUNCTIONS______________________________________________________

def heuristic(from_this: TilePosition, to_this: TilePosition) -> int:
    return (abs(to_this[0] - from_this[0]) + abs(to_this[1] - from_this[1])) * 10


def unit_distance(from_this: TilePosition, to_this: TilePosition) -> int:
    result = heuristic(from_this, to_this)
    return 14 if result > 10 else 10


def is_valid(matrix: Matrix2D, node: TilePosition, tag: CheckTag) -> bool:
    col, row = node
    # whether row and col of node is within the matrix and not equals to the given tag (hasn't been traversed/tagged)
    return row >= 0 and col >=0 and row < len(matrix) and col < len(matrix[0]) and matrix[row][col] != tag


def get_neighbour(matrix: Matrix2D, node: TilePosition, tag: CheckTag, adjacent: bool = False) -> Path:
    col, row = node
    # LEFT, RIGHT, UP, DOWN
    neighbour = [(col - 1, row), (col + 1, row), (col, row - 1), (col, row + 1)]
    if adjacent:
        neighbour.extend([(col - 1, row - 1), (col + 1, row - 1), (col - 1, row + 1), (col + 1, row + 1)])
    valid_neighbour = [(col, row) for col, row in neighbour if is_valid(matrix, (col, row), tag)]
    
    return valid_neighbour


def retracePath(node: TilePosition, path: Path) -> Path:
    result = [node]
    # check the 'parent' of each node in path
    # if the parent is None, it's the starting node
    while path[node] is not None:
        node = path[node]
        result.append(node)

    # appending the node to the resultant path from the left to right
    # practically reversing the path on the fly
    return result[::-1]