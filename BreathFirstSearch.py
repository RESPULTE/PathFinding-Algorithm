from collections import deque
from functools import partial
from .type_hints import *
from .utility import *


def tiled_BFS(
        matrix: Matrix2D, 
        origin_tile: TilePosition, 
        target_tile: TilePosition = None, 
        adjacent: bool = False
        ) -> Union[Path, List[None]]:
    
    check_neighbour = partial(get_neighbour, matrix=matrix, tag=origin_tile, adjacent=adjacent)
    openSet         = deque([origin_tile])
    closedSet       = set()
    path            = {origin_tile: None}

    while openSet:

        # pop the 'oldest' node in the openSet
        current = openSet.popleft()

        if current == target_tile:
            return retracePath(current, path)

        closedSet.add(current)

        for neighbour in check_neighbour(node=current):
            # if the neighbour hasn't been 'seen' before, 
            # add it to the open set to be 'evaluated' in the next iteration
            if neighbour not in openSet and neighbour not in closedSet:
                openSet.append(neighbour)
                path[neighbour] = current

    # return an empty list or all the evaluated nodes, 
    # depending on whether the target_tile has been given
    return closedSet if not target_tile else []