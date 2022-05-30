
from unittest import runner
import src.csp as csp

# @ <component>: <usage>

# @ stderr: reporting errors
# @ stdin: receiving input
from sys import stderr

# @ product: creation of the Var' domains
# @ permutations: determine the satisfiability of an operation
from itertools import product, permutations

# @ reduce: determine the result of an operation
from functools import reduce

# @ seed: seed the pseudorandom number generator
# @ random, shuffle, randint, choice: generation a random kenken puzzle
from random import random, shuffle, randint, choice

# @ time: benchmarking
from time import time

# @ writer: output benchmarking data in a csv format
from csv import writer


def opp(operation):
    """
     function used in order to determine the opp corresponding

    """
    if operation == '+':
        return lambda a, b: a + b
    elif operation == '-':
        return lambda a, b: a - b
    elif operation == '*':
        return lambda a, b: a * b
    elif operation == '/':
        return lambda a, b: a / b
    else:
        return None

def set_value(xy1, xy2):
   
    x1, y1 = xy1
    x2, y2 = xy2

    dx, dy = x1 - x2, y1 - y2

    return (dx == 0 and abs(dy) == 1) or (dy == 0 and abs(dx) == 1)

def generation(size):

    Board = [[((i + j) % size) + 1 for i in range(size)] for j in range(size)]
    
    for _ in range(size):
        shuffle(Board)

    for c1 in range(size):
        for c2 in range(size):
            if random() > 0.5:
                for r in range(size):
                    Board[r][c1], Board[r][c2] = Board[r][c2], Board[r][c1]

    Board = {(j + 1, i + 1): Board[i][j] for i in range(size) for j in range(size)}

    notcaged = sorted(Board.keys(), key=lambda var: var[1])

    cliq = []
    while notcaged:

        cliq.append([])

        zsize = randint(1, 4)

        Cell = notcaged[0]

        notcaged.remove(Cell)

        cliq[-1].append(Cell)

        for _ in range(zsize - 1):

            adjsu = [other for other in notcaged if set_value(Cell, other)]

            Cell = choice(adjsu) if adjsu else None

            if not Cell:
                break

            notcaged.remove(Cell)
            
            cliq[-1].append(Cell)
            
        zsize = len(cliq[-1])
        if zsize == 1:
            Cell = cliq[-1][0]
            cliq[-1] = ((Cell, ), '+', Board[Cell]) #replace . -> +
            continue
        elif zsize == 2:
            fst, snd = cliq[-1][0], cliq[-1][1]
            if Board[fst] / Board[snd] > 0 and not Board[fst] % Board[snd]:
                operation = "/" # choice("+-*/")
            else:
                operation = "-" # choice("+-*")
        else:
            operation = choice("+*")

        result = reduce(opp(operation), [Board[Cell] for Cell in cliq[-1]])

        cliq[-1] = (tuple(cliq[-1]), operation, int(result))

    return size, cliq

def validation(size, cliq):
   
    Out = lambda xy: xy[0] < 1 or xy[0] > size or xy[1] < 1 or xy[1] > size

    mention = set()
    for i in range(len(cliq)):
        Member, operation, result = cliq[i]

        cliq[i] = (tuple(set(Member)), operation, result)

        Member, operation, result = cliq[i]

        if operation not in "+-*/.":
            exit(1)

        hard = list(filter(Out, Member))
        if hard:
            exit(2)

        hard = mention.intersection(set(Member))
        if hard:
            exit(3)

        mention.update(set(Member))

    indx = range(1, size + 1)

    hard = set([(x, y) for y in indx for x in indx]).difference(mention)

    if hard:
        exit(4)

def check_row_column(xy1, xy2):

    return (xy1[0] == xy2[0]) != (xy1[1] == xy2[1])

def conflict(X, x, Y, y):
    for i in range(len(X)):
        for j in range(len(Y)):
            mX = X[i]
            mY = Y[j]

            mx = x[i]
            my = y[j]
            if check_row_column(mX, mY) and mx == my:
                return True

    return False

def satisfiable(val, opp, result):

    for p in permutations(val):
        if reduce(opp, p) == result:
            return True

    return False

def game_domain(size, cliq):
    
    domains = {}
    for clique in cliq:
        Member, operation, result = clique

        domains[Member] = list(product(range(1, size + 1), repeat=len(Member)))

        qualification = lambda val: not conflict(Member, val, Member, val) and satisfiable(val, opp(operation), result)

        domains[Member] = list(filter(qualification, domains[Member]))

    return domains

