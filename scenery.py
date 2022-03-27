from abc import ABC

import pygame
from texts import Text
from pygame.locals import *
from button import Button
from game import Game
from controller import Controller


class Scenery(ABC):
    name: str
    controller: Controller
    buttons: list[Button]
    quit_button: Button
    keys: dict[int, str]
    texts: list[Text]

    @classmethod
    def run(cls, game: Game) -> None:
        cls.start_setup(game)
        while True:
            cls.handle_events(game)

            game.display.fill(game.background)
            cls.start(game)

            for text in cls.texts:
                text.show(game, position=(game.width // 2, game.height // 2))

            for button in cls.buttons:
                if button.update(game.display) == 1:
                    cls.controller.execute(button.command)

            if cls.quit_button.update(game.display) == 1:
                cls.controller.execute(cls.quit_button.command)
                break

            cls.end(game)

            cls.update(game)
        cls.end_setup(game)
    
    @classmethod
    def handle_events(cls, game: Game) -> None:
        for event in pygame.event.get():
                if event.type == QUIT:
                    cls.controller.execute("QUIT")

                if event.type == KEYDOWN:
                    if event.key in cls.keys:
                        command = cls.keys[event.key]
                        cls.controller.execute(command)
                        break

    @classmethod
    def start_setup(cls, game: Game) -> None:
        print(f'Running {cls.name}...')

    @classmethod
    def update(cls, game: Game) -> None:
        """updates the scenery screen"""
        pygame.display.update()
        game.fps.tick(15)

    @classmethod
    def start(cls, game: Game) -> None:
        """Runs in the begining of the scenery loop"""

    @classmethod
    def end(cls, game: Game) -> None:
        """Runs at the end of the scenery loop"""

    @classmethod
    def close_setup(cls, game: Game) -> None:
        """Runs after the scenery loop"""
        

class Scenerys:
    scenery: dict[str, Scenery] = dict()

    @classmethod
    def set_controller(cls, controller: Controller) -> None:
        for name, scenery in cls.scenery.items():
            scenery.controller = controller
            controller.register(name.upper())(scenery.run)
        
    @classmethod
    def register(cls, scenery: Scenery) -> Scenery:
        cls.scenery[scenery.name] = scenery
        return scenery
