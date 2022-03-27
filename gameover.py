import random
import pygame
from pygame.locals import *
from button import Buttons
from game import Game
from colors import Color
from scenery import Scenery, Scenerys
from scores import update_highscore
from texts import Font, Text


@Scenerys.register
class GameOver(Scenery):
    name = "Game Over"
    buttons = [
        Buttons.AGAIN,
        Buttons.HIGHSCORES,
        Buttons.MUSICS,
        Buttons.QUIT,
    ]
    keys = {
        K_SPACE: "START GAME"
    }
    quit_button = Buttons.MENU

    texts = [Text(
                message="Game Over",
                font=Font.LARGE,
            )]

    @classmethod
    def start_setup(cls, game: Game) -> None:
        super().start_setup(game)
        update_highscore(game.score)
        game.musicplaying = False
        pygame.mixer.music.stop()
        print('Collision details:')
        print(f'\thead: {game.snake.get_head()} body: {game.snake.get_body()}')

    @classmethod
    def start(cls, game: Game) -> None:
        pygame.draw.rect(game.display,
            (random.randrange(15, 255), random.randrange(15, 255), random.randrange(15, 255)),
            Rect(game.food[0], game.food[1], 10, 10)
        )

        head = game.snake.get_head()
        pygame.draw.rect(game.display, Color.GREEN, Rect(head[0], head[1], 10, 10))

        for pos in game.snake.get_body():
            pygame.draw.rect(game.display, Color.GREEN, Rect(pos[0], pos[1], 10, 10))
