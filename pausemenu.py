import random
import pygame
from pygame.locals import *
from colors import Color
from button import Buttons
from game import Game
from scenery import Scenery, Scenerys
from texts import Font, Text


@Scenerys.register
class PauseMenu(Scenery):
    name = "Pause Menu"

    buttons = [
        Buttons.HIGHSCORES,
        Buttons.AGAIN,
        Buttons.QUIT,
        Buttons.HIGHSCORES,
        Buttons.MUSICS
    ]
    quit_button = Buttons.RETURN
    texts = [Text(
                message="Pause",
                font=Font.LARGE,
            )]
    keys = {
        K_SPACE: "START GAME"
    }

    @classmethod
    def start_setup(cls, game: Game) -> None:
        super().start_setup(game)
        game.musicplaying = False
        pygame.mixer.music.pause()

    @classmethod
    def handle_events(cls, game: Game) -> None:
        for event in pygame.event.get():
            if event.type == QUIT:
                cls.controller.execute("QUIT")

            if event.type == KEYDOWN:
                if event.key in cls.keys:
                    command = cls.keys[event.key]
                    game.musicplaying = True
                    pygame.mixer.music.unpause()
                    cls.controller.execute(command)
    
    @classmethod
    def start(cls, game: Game) -> None:
        pygame.draw.rect(
            game.display, (random.randrange(15, 255), random.randrange(15, 255),
            random.randrange(15, 255)), Rect(game.food[0], game.food[1], 10, 10)
        )

        head = game.snake.get_head()
        pygame.draw.rect(game.display, Color.GREEN, Rect(head[0], head[1], 10, 10))

        for pos in game.snake.get_body():
            pygame.draw.rect(game.display, Color.GREEN, Rect(pos[0], pos[1], 10, 10))
