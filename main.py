import pygame
from scenery import Scenerys
from foodgenerator import generate_food
from audio import PlayList, MusicOptions, load_musics_in_controller
import startmenu, musicsmenu, highscoremenu, gamescreen, gameover, pausemenu
from game import Game
from controller import Controller


pygame.init()


def main() -> None:
    width=800
    height=600
    game = Game(
        width=width,
        height=height,
        musicplaying=False,
        score=0,
        food=generate_food(width, height)
    )
    load_musics_in_controller()
    pygame.display.set_caption('Snake Game')
    MusicOptions.set_music_options(game)
    PlayList.UNITY.value.play()
    controller = Controller(game) 
    Scenerys.set_controller(controller)
    controller.execute("START MENU")


if __name__ == "__main__":
    main()
