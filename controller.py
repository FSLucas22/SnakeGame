from typing import Callable
from direction import Direction
from game import Game
from quitgame import quit_game


def invalid_request(name: str):
    print("Invalid request:", name)


class Controller:
    requests: dict[str, Callable] = dict()
    
    def __init__(self, game: Game):
        self.game = game

    @classmethod
    def register(cls, name: str):
        def get_action(action: Callable[[Game], None]) -> Callable[[Game], None]:
            cls.requests[name] = action
            return action
        return get_action
    
    def execute(self, request: str) -> None:
        if not request in self.requests:
            invalid_request(request)
            return
        print("Executing command:", request)
        self.requests[request](self.game)


@Controller.register('DO NOTHING')
def do_nothing(*args, **kwargs) -> None:
    return


@Controller.register('MOVE UP')
def go_up(game: Game) -> None:
    if game.snake.direction != Direction.DOWN:
        game.snake.change_direction(Direction.UP)


@Controller.register('MOVE RIGHT')
def go_right(game: Game) -> None:
    if game.snake.direction != Direction.LEFT:
        game.snake.change_direction(Direction.RIGHT)


@Controller.register('MOVE DOWN')
def go_down(game: Game) -> None:
    if game.snake.direction != Direction.UP:
        game.snake.change_direction(Direction.DOWN)


@Controller.register('MOVE LEFT')
def go_left(game: Game) -> None:
    if game.snake.direction != Direction.RIGHT:
        game.snake.change_direction(Direction.LEFT)


@Controller.register('QUIT')
def quit(game: Game) -> None:
    quit_game()
