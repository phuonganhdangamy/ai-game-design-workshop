from game import Direction, Game
from typing import Tuple


def oppositeOf(d: Direction) -> Direction:
    if d == Direction.UP:
        return Direction.DOWN
    if d == Direction.DOWN:
        return Direction.UP
    if d == Direction.LEFT:
        return Direction.RIGHT
    if d == Direction.RIGHT:
        return Direction.LEFT


def solve(game: Game) -> Tuple[bool, int]:
    visited = []

    def visit(x: int, y: int):
        def visitNeighbour(nx: int, ny: int, d: Direction):
            if nx >= 0 and nx < game.height and ny >= 0 and ny < game.width and ((nx, ny) not in visited) and game.grid[nx][ny] != 'W':
                print(d)
                game.playMove(d)

                # check for tree or monster
                if game.grid[nx][ny] == 'M':
                    for _ in range(5):
                        game.playMove(d)
                elif game.grid[nx][ny] == 'T':
                    game.playMove(d)

                visit(nx, ny)
                print(oppositeOf(d))
                game.playMove(oppositeOf(d))

        visited.append((x, y))

        if not ((x == game.height - 1 and y == game.width - 1) or ((game.height - 1, game.width - 1) in visited)):
            visitNeighbour(x - 1, y, Direction.UP)
            visitNeighbour(x + 1, y, Direction.DOWN)
            visitNeighbour(x, y - 1, Direction.LEFT)
            visitNeighbour(x, y + 1, Direction.RIGHT)

    visit(0, 0)

    return ((game.height - 1, game.width - 1) in visited, game.movesPlayed)


game = Game(3, 3, 0.1, 0.1, 0.3)
game.renderBoard()
print(solve(game))
