from typing import Callable
import pygame
from dataclasses import dataclass
from button import Button
from colors import Color
from game import Game
from valued_enum import ValuedEnum
from controller import Controller


@dataclass
class Music:
    name: str
    command_name: str
    def play(self) -> None:
        print(f"playing {self.name}...")
        set_music(self.get_path())

    def get_name(self) -> str:
        return self.name

    def get_path(self) -> str:
        return 'musics/'+ self.name


class PlayList(ValuedEnum):
    UNITY = Music('TheFatRat - Unity.mp3', "PLAY UNITY")
    STRONGER = Music('TheFatRat - Stronger.mp3', "PLAY STRONGER")
    INFINITE_POWER = Music('TheFatRat - Infinite Power.mp3', "PLAY INFINITE POWER")


def set_music(music_path: str) -> None:
    pygame.mixer.music.load(music_path)


def music_playing(game: Game) -> None:
    if not game.musicplaying:
        game.musicplaying = True
        pygame.mixer.music.play(-1)


class MusicOptions:
    options: list[Button] = []

    @classmethod
    def set_music_options(cls, game: Game):
        width = 500
        height = 50
        for i, music in enumerate(PlayList.values()):
            button = Button(
                text=music.get_name(),
                x=game.width / 2 - width / 2,
                y=game.height / 5 + i * 50,
                width=width,
                height=height,
                inactive_color=Color.GREY,
                active_color=Color.BRIGHT_GREY,
                command=music.command_name
            )
            print('Button command:', button.command)
            cls.options.append(button)
    
    @classmethod
    def get_music_options(cls) -> list[Button]:
        return cls.options


def load_musics_in_controller() -> None:
    def music_function(music: Music) -> Callable[[], None]:
        return lambda *args, **kwargs: music.play()
    for music in PlayList.values():
        print('Registering music:', music)
        Controller.register(music.command_name)(music_function(music))
