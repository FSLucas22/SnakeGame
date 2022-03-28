from enum import Enum, auto
import pygame
from dataclasses import dataclass, field
from texts import Font, text_object
from colors import Color


class ButtonState(Enum):
    INACTIVE = auto()
    ACTIVE = auto()
    PRESSED = auto()


@dataclass
class Button:
    text: str
    x: int
    y: int
    width: int
    height: int
    inactive_color: tuple[int]
    active_color: tuple[int]
    command: str

    previous_state: ButtonState = field(default=ButtonState.INACTIVE)
    state: ButtonState = field(default=ButtonState.INACTIVE)

    def update(self, game_display: pygame.display) -> int:
        status = 0
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            if click:
                self.update_state(ButtonState.PRESSED)
                pygame.draw.rect(game_display, Color.WHITE, (self.x, self.y, self.width, self.height))

            else:
                self.update_state(ButtonState.ACTIVE)
                pygame.draw.rect(game_display, self.active_color, (self.x, self.y, self.width, self.height))
            
            if self.previous_state == ButtonState.PRESSED and self.state == ButtonState.ACTIVE:
                status = 1
                
        else:
            self.state = ButtonState.INACTIVE
            pygame.draw.rect(game_display, self.inactive_color, (self.x, self.y, self.width, self.height))

        textSurf, textRect = text_object(self.text, Font.SMALL)
        textRect.center = ((self.x + (self.width / 2)), (self.y + (self.height / 2)))
        game_display.blit(textSurf, textRect)
        return status

    def update_state(self, state: ButtonState) -> None:
        self.previous_state = self.state
        self.state = state


class NoButton(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(
            text='Start!',
            x=150,
            y=450,
            width=100,
            height=50,
            inactive_color=Color.GREEN,
            active_color=Color.BRIGHT_GREEN,
            command = 'DO NOTHING'
        )
    def update(self, *args, **kwargs) -> int:
        return 0
        

class Buttons:
    START = Button(
        text='Start!',
        x=150,
        y=450,
        width=100,
        height=50,
        inactive_color=Color.GREEN,
        active_color=Color.BRIGHT_GREEN,
        command="START GAME"
    )
    QUIT = Button(
        text='Quit',
        x=550, y=450,
        width=100, height=50,
        inactive_color=Color.RED,
        active_color=Color.BRIGHT_RED,
        command="QUIT"
    )
    MENU = Button(
        text='Menu',
        x=350, y=450,
        width=100, height=50,
        inactive_color=Color.GREEN,
        active_color=Color.BRIGHT_GREEN,
        command="START MENU"
    )
    HIGHSCORES = Button(
        text='High Scores',
        x=550, y=10,
        width=130, height=50,
        inactive_color=Color.BLUE,
        active_color=Color.BRIGHT_BLUE,
        command="HIGHSCORES MENU"
        )
    MUSICS = Button(
            text='Musics',
            x=550, y=70,
            width=130, height=50,
            inactive_color=Color.GREY,
            active_color=Color.BRIGHT_GREY,
            command="MUSICS MENU"
        )
    AGAIN = Button(
        text='Again',
        x=150, y=450,
        width=100, height=50,
        inactive_color=Color.BLUE,
        active_color=Color.BRIGHT_BLUE,
        command="REPLAY"
    )
    RETURN = Button(
        text='Return',
        x=150, y=450,
        width=100, height=50,
        inactive_color=Color.GREEN,
        active_color=Color.BRIGHT_GREEN,
        command='DO NOTHING'
    )
    NONE = NoButton()
