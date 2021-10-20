from typing import List, Tuple, Union, TypeVar

Matrix2D     = List[List[str]]
TilePosition = Tuple[int, int]
Path         = List[Tuple[int, int]]
CheckTag     = TypeVar('CheckTag', int, float, str, bool)