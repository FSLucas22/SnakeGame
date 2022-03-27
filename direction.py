from enum import Enum


class Direction(Enum):
    LEFT = [-10, 0]
    RIGHT = [10, 0]
    UP = [0, -10]
    DOWN = [0, 10]
    