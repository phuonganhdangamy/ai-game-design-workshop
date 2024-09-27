from game import Game
from autoplay import solve
from random import random


def mutate(prob: float) -> float:
    prob += (random() - 0.5) * 0.1
    return prob if prob <= 1 and prob >= 0 else (1 if prob > 1 else 0)


def procGen(width: int, height: int, desiredMovesToWin: int, allowance: int):
    pass
