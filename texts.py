import pygame
from colors import Color
from dataclasses import dataclass
from game import Game

pygame.init()

class Font:
    BASIC = pygame.font.SysFont(None, 48, False, True)
    LARGE = pygame.font.Font('freesansbold.ttf', 50)
    SMALL = pygame.font.Font("freesansbold.ttf", 20)
    SMALLER = pygame.font.Font('freesansbold.ttf', 15)


@dataclass
class Text:
    message: str
    font: Font

    def show(self, game: Game, position: tuple[int]) -> None:
        text_surface, text_rect = text_object(self.message, self.font)
        text_rect.center = position
        game.display.blit(text_surface, text_rect)


def text_object(text: str, font: pygame.font) -> tuple[pygame.Surface, pygame.Rect]:
    textSurface = font.render(text, True, Color.WHITE)
    return textSurface, textSurface.get_rect()
