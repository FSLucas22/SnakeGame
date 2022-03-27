from direction import Direction


class Snake:
    def __init__(self, head: list[int], body: list[list[int]], direction: Direction):
        self.head = head
        self.body = body
        self.direction = direction

    def change_direction(self, direction: Direction) -> None:
        self.direction = direction

    def move(self, food_position: list[int]) -> int:
        position = self.head
        self.body.append(position)
        self.update_head()

        if position == food_position:
            return 1

        self.body.pop(0)
        return 0
        
    def update_head(self) -> None:
        x = self.head[0] + self.direction.value[0]
        y = self.head[1] + self.direction.value[1]
        self.head = [x, y]

    def check_collision(self, display_width, display_height) -> int:
        if self.head[0] > display_width - 10 or self.head[0] < 0:
            return 1

        elif self.head[1] > display_height - 10 or self.head[1] < 0:
            return 1

        for bodyPart in self.body:
            if self.head == bodyPart:
                return 1

        return 0
    
    def get_head(self) -> list[int]:
        return self.head

    def get_body(self) -> list[list[int]]:
        return self.body
