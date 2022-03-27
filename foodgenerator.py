import random

def generate_food(width: int, height: int) -> tuple[int]:
    position = [random.randrange(0, width // 10) * 10, random.randrange(1, height // 10) * 10]
    return position
    