from dataclasses import dataclass, field
from typing import Callable
from colors import Color
from direction import Direction
from foodgenerator import generate_food
from snake import Snake
import pygame


@dataclass
class Game:
    width: int
    height: int
    score: int
    food: tuple[int]
    snake: Snake = field(default=None)
    difficult: int = field(default=5)
    level: int = field(default=1)
    musicplaying: bool = field(default=False)
    background: Color = field(default=Color.BLACK)
    fps: pygame.time.Clock = field(default=pygame.time.Clock())

    def __post_init__(self):
        self.display = pygame.display.set_mode((self.width, self.height), 0, 32)
        if not self.snake:
            self.snake = self.starting_snake()

    def starting_snake(self) -> Snake:
        snake_head = [self.width // 2, self.height // 2]
        snake_body : list[list[int]] = [
        [self.width // 2, self.height // 2 + 10],
        [self.width // 2, self.height // 2 + 20],
        ]
        return Snake(snake_head, snake_body, Direction.UP)

    def starting_configuration(self) -> None:
        self.score = 0
        self.difficult = 5
        self.level = 1
        self.snake = self.starting_snake()
        self.food = generate_food(self.width, self.height)

        