from enum import Enum
import random


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Game:
    def __init__(self, width: int, height: int, monsterProbability: float, treeProbability: float, wallProbability: float):
        self.width = width
        self.height = height
        self.monsterProbability = monsterProbability
        self.treeProbability = treeProbability
        self.wallProbability = wallProbability
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]

        self.grid[0][0] = 'P'
        self.playerPos = Position(0, 0)

        for i in range(height):
            for j in range(width):
                # don't modify start or goal
                if (i == 0 and j == 0) or (i == height - 1 and j == width - 1):
                    continue

                # priority to tree
                # 2nd priority monster
                # last priority wall
                if random.random() <= treeProbability:
                    self.grid[i][j] = 'T'
                elif random.random() <= monsterProbability:
                    self.grid[i][j] = 'M'
                elif random.random() <= wallProbability:
                    self.grid[i][j] = 'W'

        self.grid[height - 1][width - 1] = 'G'
        self.goalPos = Position(height - 1, width - 1)

        self.movesPlayed = 0
        self.monsterStart = -1
        self.treeStart = -1

    def renderBoard(self) -> None:
        print("-" * (2 * self.width + 1))

        for row in self.grid:
            print("|" + "|".join(row) + "|")

        print("-" * (2 * self.width + 1))

    def playMove(self, direction: Direction, render=True) -> bool:
        if self.monsterStart != -1 and self.movesPlayed - self.monsterStart < 6:
            pass
        elif self.treeStart != -1 and self.movesPlayed - self.treeStart < 2:
            pass
        else:
            prevX = self.playerPos.x
            prevY = self.playerPos.y
            x = self.playerPos.x
            y = self.playerPos.y
            if direction == Direction.UP:
                if x - 1 >= 0 and self.grid[x-1][y] != 'W':
                    x -= 1
            elif direction == Direction.DOWN:
                if x + 1 < self.height and self.grid[x+1][y] != 'W':
                    x += 1
            elif direction == Direction.LEFT:
                if y - 1 >= 0 and self.grid[x][y-1] != 'W':
                    y -= 1
            else:
                if y + 1 < self.width and self.grid[x][y+1] != 'W':
                    y += 1

            if self.grid[x][y] == 'T':
                self.treeStart = self.movesPlayed
            elif self.grid[x][y] == 'M':
                self.monsterStart = self.movesPlayed

            self.grid[prevX][prevY] = ' '
            self.grid[x][y] = 'P'
            self.playerPos.x = x
            self.playerPos.y = y

        self.movesPlayed += 1

        if render:
            self.renderBoard()

        return self.grid[self.height - 1][self.width - 1] == 'P'


def getDirection(d: str) -> Direction:
    if d == 'U' or d == 'u':
        return Direction.UP
    if d == 'D' or d == 'd':
        return Direction.DOWN
    if d == 'L' or d == 'l':
        return Direction.LEFT
    if d == 'R' or d == 'r':
        return Direction.RIGHT

    raise ValueError


if __name__ == "__main__":
    game = Game(4, 4, 0.1, 0.1, 0.3)
    game.renderBoard()

    while True:
        game.playMove(getDirection(input("Enter next move: ")))
