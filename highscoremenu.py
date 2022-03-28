import pygame
from pygame.locals import *
from button import Buttons
from game import Game

from scenery import Scenery, Scenerys
from scores import get_high_score_file
from texts import Font, Text


@Scenerys.register
class HighScoreMenu(Scenery):
    name = "HighScores Menu"
    buttons = [
        Buttons.MUSICS,
    ]
    keys = {}
    quit_button = Buttons.RETURN
    texts = [Text(
                message='High Scores:',
                font=Font.BASIC,
            )]
    
    @classmethod
    def start(cls, game: Game) -> None:
        title = cls.texts[0]
        title.show(game, position=(game.width // 2, game.height // 7))
        for i, text in enumerate(cls.generate_scores_texts()):
            text.show(game, position=(game.width // 2, game.height // 5 + i * 20))


    @classmethod
    def generate_scores_texts(cls) -> list[Text]:
        rfile = get_high_score_file()
        score_list = rfile.readlines()
        rfile.close()
        texts = []
        for i, score in enumerate(score_list):
            text = Text(
                message=f"{i+1}) {score[:-1]}",
                font=Font.SMALLER,
            )
            texts.append(text)
        return texts