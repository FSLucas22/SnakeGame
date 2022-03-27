from pygame.locals import *
from audio import MusicOptions
from button import Buttons
from game import Game
from scenery import Scenery, Scenerys
from texts import Font, Text


@Scenerys.register
class MusicsMenu(Scenery):
    name = "Musics Menu"

    buttons = [
        Buttons.HIGHSCORES,
    ]
    quit_button = Buttons.RETURN
    texts = [Text(
                message="Musics:",
                font=Font.LARGE,
            )]
    keys = {}
    
    @classmethod
    def end(cls, game: Game) -> None:
        for button in MusicOptions.get_music_options():
            if button.update(game.display) == 1:
                cls.controller.execute(button.command)