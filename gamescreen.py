import random
import pygame
from pygame.locals import *
from audio import music_playing
from colors import Color
from button import Buttons
from foodgenerator import generate_food
from game import Game

from scenery import Scenery, Scenerys


@Scenerys.register
class StartGame(Scenery):
    name = "Start Game"
    buttons = []

    keys = {
        K_LEFT: "MOVE LEFT",
        K_RIGHT: "MOVE RIGHT",
        K_UP: "MOVE UP",
        K_DOWN: "MOVE DOWN",
        K_SPACE: "PAUSE MENU"
    }

    quit_button = Buttons.NONE

    texts = []

    @classmethod
    def start(cls, game: Game) -> None:
        music_playing(game)
        if game.snake.move(game.food) == 1:
            game.score += game.level
            game.food = generate_food(game.width, game.height)
            if game.score % (game.level+1) == 0:
                if game.score > 0:
                    game.difficult += 1
                    game.level += 1
    
        pygame.draw.rect(game.display,
            (random.randrange(15, 255), random.randrange(15, 255), random.randrange(15, 255)),
            Rect(game.food[0], game.food[1], 10, 10))

        head = game.snake.get_head()
        pygame.draw.rect(game.display, Color.GREEN, Rect(head[0], head[1], 10, 10))

        for pos in game.snake.get_body():
            pygame.draw.rect(game.display, Color.GREEN, Rect(pos[0], pos[1], 10, 10))

        if game.snake.check_collision(game.width, game.height) == 1:
            cls.controller.execute("GAME OVER")
            return

    @classmethod
    def update(cls, game: Game) -> None:
        pygame.display.set_caption(f'Snake Game | Lv: {game.level} | Score: {game.score}')
        pygame.display.flip()
        game.fps.tick(game.difficult)


@Scenerys.register
class ReplayGame(StartGame):
    name = "Replay"

    @classmethod
    def run(cls, game: Game) -> None:
        game.starting_configuration()
        super().run(game)
