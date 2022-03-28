from pygame.locals import *
from button import Buttons
from scenery import Scenery, Scenerys
from texts import Font, Text


@Scenerys.register
class StartMenu(Scenery):
    name = "Start Menu"
    buttons = [
        Buttons.START,
        Buttons.HIGHSCORES,
        Buttons.MUSICS,
        Buttons.QUIT,
    ]
    keys = {
        K_SPACE: "START GAME"
    }
    quit_button = Buttons.NONE

    texts = [Text(
                message="Snake Game",
                font=Font.LARGE,
            )]
