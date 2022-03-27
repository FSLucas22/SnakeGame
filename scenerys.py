from audio import generate_music_options
from button import Buttons, do_nothing
from quitgame import quit_game
from scores import get_high_score_file
from texts import Text, Font
from pygame.locals import *
from scenery import Scenery


class Scenerys:
    def __init__(self, game):
        self.game = game
    
    def start_scenery(self):
        buttons = {
            Buttons.START: self.game_scenery,
            Buttons.HIGHSCORES: self.scores_scenery,
            Buttons.MUSICS: self.music_scenery,
            Buttons.QUIT: quit_game,
        }  
        texts = [Text(
            message="Snake Game",
            font=Font.LARGE,
            position=(self.game.width // 2, self.game.height // 2))]
        keys = {
            K_SPACE, self.game_scenery
        }
        Scenery(
            game=self.game,
            buttons=buttons,
            keys=keys,
            texts=texts,
            name='Main'
        ).run()

    def scores_scenery(self):
        rfile = get_high_score_file()
        score_list = rfile.readlines()
        rfile.close()
        buttons = {
            Buttons.START: self.game_scenery,
            Buttons.MENU: self.start_scenery,
            Buttons.HIGHSCORES: self.scores_scenery,
        }
        return_button = (Buttons.RETURN, do_nothing)
        texts = [Text(
            message='High Scores:',
            font=Font.BASIC,
            position=(self.game.width // 2, self.game.height // 7)
        )]
        for i, score in enumerate(score_list):
            text = Text(
                message=f"{i+1}) {score[:-1]}",
                font=Font.SMALLER,
                position=(self.game.width // 2, self.game.height // 5 + i * 20)
            )
            texts.append(text)

        Scenery(
            game=self.game,
            buttons=buttons,
            quit_button=return_button,
            texts=texts,
            name='Scores'
        ).run()
    
    def music_scenery(self):
        buttons = {
            #Buttons.START: self.game_scenery,
            Buttons.HIGHSCORES: self.scores_scenery,
        }
        return_button = (Buttons.RETURN, do_nothing)
        for button in generate_music_options(self.game):
            buttons[button[0]] = button[1]
        texts = [Text(
            message="Musics:",
            font=Font.LARGE,
            position=(self.game.width // 2, self.game.height // 7)
        )]
        Scenery(
            game=self.game,
            buttons=buttons,
            quit_button=return_button,
            texts=texts,
            name="Musics"
        ).run()

    def game_scenery(self):
        #TODO
        Scenery(game=self.game, name="the game").run()
