class Block:
    """
    Building blocks for the body of snake
    Node for a linked list
    (x, y) coordinate
    next as Block
    """

    def __init__(self, position=(None, None)):
        self.x = position[0]
        self.y = position[1]
        self.next = None

    def as_tuple(self):
        return (self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Body:
    """
    Body of the snake (a linked list)
    [head]->[next]->[next]...[next]->[tail]
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.blocks = [] 

    def add_head(self, position):
        """
        Add a block to the front
        @param positon as tuple(int, int)
        """
        block = Block(position)

        block.next = self.head
        self.head = block

        self.blocks = [position] + self.blocks

        if self.head.next is None:
            self.tail = block

        # update length
        self.length += 1

    def add_tail(self, position):
        block = Block(position)
        self.tail.next = block
        self.tail = block

        # update length
        self.length += 1

    def remove_tail(self):
        """
        Remove the last block i.e tail
        """
        last = self.head
        while self.tail != last.next:
            last = last.next
        self.tail = last
        self.tail.next = None

        self.blocks.pop(-1)

        # update length
        self.length -= 1

    def __repr__(self):
        body_str = ""
        last = self.head
        while last is not None:
            body_str = str(last) + body_str
            last = last.next
        return body_str


class Direction:
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"

    @classmethod
    def opposite(cls, dir):
        if dir == "up":
            return cls.DOWN
        elif dir == "down":
            return cls.UP
        elif dir == "left":
            return cls.RIGHT
        elif dir == "right":
            return cls.LEFT

    @classmethod
    def all(cls):
        return [cls.UP, cls.DOWN, cls.LEFT, cls.RIGHT]

class Snake:
    """
    Snake with body and a direction
    body as linked list `Body`
    direction as `Direction`
    """

    def __init__(self, block_size=1):
        self.block_size = block_size
        self.direction = Direction.RIGHT
        self.body = self.create_body()
        self.is_alive = True
        self.dying_reason = None
        self.head = self.body.head

    def create_body(self):
        body = Body()
        for i in range(4):
            body.add_head((i * self.block_size , self.block_size))
        return body

    def get_body(self):
        body = self.body.blocks
        return tuple(body)

    def get_head(self):
        head = self.body.head
        return (head.x, head.y)

    def grow(self):
        head = self.body.head
        if self.direction == Direction.RIGHT:
            new_block = (head.x + self.block_size, head.y)
        elif self.direction == Direction.LEFT:
            new_block = (head.x - self.block_size, head.y)
        elif self.direction == Direction.UP:
            new_block = (head.x, head.y - self.block_size)
        elif self.direction == Direction.DOWN:
            new_block = (head.x, head.y + self.block_size)

        # if snake touches itself it dies
        if self.overlap(new_block):
            self.is_alive = False
            self.dying_reason = f"Touched itself {new_block}"
            return
        self.body.add_head(new_block)
        # update head
        self.head = self.body.head

    def move_forward(self):
        self.grow()
        self.body.remove_tail()

    def overlap(self, point):
        block = Block(point)
        last = self.body.head
        while last is not None:
            if block == last:
                return True
            last = last.next
        return False

