from functools import partial
from .type_hints import *
from .utility import *


def tiled_DFS(
        matrix: Matrix2D, 
        origin_tile: TilePosition, 
        target_tile: TilePosition = None, 
        adjacent: bool = False
        ) -> Union[Path, List[None]]:
    
    check_neighbour = partial(get_neighbour, matrix=matrix, tag=origin_tile, adjacent=adjacent)
    closedSet       = set()
    path            = {origin_tile: None}

    def DFS(current: TilePosition) -> Union[Path, List[None]]:
        if current == target_tile:
            return 

        closedSet.add(current)

        for neighbour in check_neighbour(node=current):
            # check if the neighbour of the current node has been evaluated or not
            # if not, add it to the 'closedSet', log it in the 'path' and call DFS again
            if neighbour not in closedSet:
                path[neighbour] = current
                DFS(neighbour)

        # check if the DFS has actually found the target tile or not
        # if not, just return all traversed path (closedSet) if no target is specified or 
        # an empty list if there is a target
        return retracePath(target_tile, path) if target_tile in path else closedSet if not target_tile else []

    return DFS(origin_tile)