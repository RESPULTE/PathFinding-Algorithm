from collections import namedtuple
from functools import partial
from .type_hints import *
from .utility import *


def tiled_Dijkstra(
        matrix: Matrix2D, 
        origin_tile: TilePosition, 
        target_tile: TilePosition, 
        adjacent: bool = False
        ) -> Union[Path, List[None]]:
    
    check_neighbour = partial(get_neighbour, matrix=matrix, tag=origin_tile, adjacent=adjacent)
    # using a Node pseudo-class to make accessing and caching the determinents (f-score & g-score) easier
    Node            = namedtuple("Node", ['g_score', 'tile'])
    openSet         = [Node(0, origin_tile)]
    closedSet       = set()
    path            = {origin_tile: None}
    
    while openSet:

        # get the tile with the least f_score in the 'openSet'
        current = heappop(openSet)
        
        if target_tile == current.tile:
            return retracePath(current.tile, path)

        closedSet.add(current.tile)

        for neighbour in check_neighbour(node=current.tile):
            
            # calculater the g_score and f_score of the neighbour
            # g_score : distance from origin with the path taken \\ not the raw distance
            # h_score : distance to the target 
            # f_score : g_score + h_score \\ total cost of taking that particular node
            g_score = unit_distance(neighbour, current.tile) + current.g_score

            # if the node hasn't been evaluated before nor been added into queue for evaluation, 
            # create a node and add it into the queue 
            if neighbour not in closedSet and neighbour not in [node.tile for node in openSet]:
                sneighbour_node = Node(g_score, neighbour)
                heappush(openSet, neighbour_node)
                path[neighbour] = current.tile
        

    return []