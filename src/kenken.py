
from unittest import runner
import src.csp as csp

from sys import stderr

from itertools import product, permutations

from functools import reduce

from random import random, shuffle, randint, choice

from time import time

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

def game_neighbors(cliq):
    neighbors = {}
    for Member, _, _ in cliq:
        neighbors[Member] = []

    for X, _, _ in cliq:
        for Y, _, _ in cliq:
            if X != Y and Y not in neighbors[X]:
                if conflict(X, [-1] * len(X), Y, [-1] * len(Y)):
                    neighbors[X].append(Y)
                    neighbors[Y].append(X)

    return neighbors

class Kenken(csp.CSP):

    def __init__(self, size, cliq):
        validation(size, cliq)
        
        Var = [Member for Member, _, _ in cliq]
        
        domains = game_domain(size, cliq)

        neighbors = game_neighbors(cliq)

        csp.CSP.__init__(self, Var, domains, neighbors, self.constraint)

        self.size = size
        self.checks = 0
        self.padding = 0

        self.meta = {}
        for Member, operation, result in cliq:
            self.meta[Member] = (operation, result)
            self.padding = max(self.padding, len(str(result)))        

    

    def constraint(self, X, x, Y, y):
       
        self.checks += 1

        return X == Y or not conflict(X, x, Y, y)

    def display(self, assignment):
    
        if assignment:
            uint = {}
            for Member in self.Var:
                val = assignment.get(Member)

                if val:
                    for i in range(len(Member)):
                        uint[Member[i]] = val[i]
                else:
                    for member in Member:
                        uint[member] = None
        else:
            uint = {member:None for Member in self.Var for member in Member}

        uint = sorted(uint.items(), key=lambda item: item[0][1] * self.size + item[0][0])

        padding = lambda c, offset: (c * (self.padding + 2 - offset))

        embrace = lambda inner, beg, end: beg + inner + end

        mention = set()

        def meta(member):
            for var, val in self.meta.items():
                if member in var and var not in mention:
                    mention.add(var)
                    return str(val[1]) + " " + (val[0] if val[0] != "." else " ")

            return ""

        fit = lambda word: padding(" ", len(word)) + word + padding(" ", 0)

        cpadding = embrace(2 * padding(" ", 0), "|", "") * self.size + "|"

        def show(row):

            rpadding = "".join(["|" + fit(meta(item[0])) for item in row]) + "|"

            data = "".join(["|" + fit(str(item[1] if item[1] else "")) for item in row]) + "|"

            print(rpadding, data, cpadding, sep="\n")

        rpadding = embrace(2 * padding("-", 0), "+", "") * self.size + "+"

        print(rpadding)
        for i in range(1, self.size + 1):

            show(list(filter(lambda item: item[0][1] == i, uint)))

            print(rpadding)

    def info(self):
    
        for var in self.Var:
            print(var)

        print("\nDomains:")
        for var in self.Var:
            print("domains[", var, "] =", self.domains[var])

        print("\nNeighbors:")
        for var in self.Var:
            print("neighbors[", var, "] =", self.neighbors[var])

def benchmark(kenken, algorithm):

        kenken.checks = kenken.nassigns = 0

        dt = time()

        assignment = algorithm(kenken)

        dt = time() - dt

        return assignment, (kenken.checks, kenken.nassigns, dt)

def gather(iterations, out):
    bt         = lambda ken: csp.backtracking_search(ken)
    fc         = lambda ken: csp.backtracking_search(ken, inference=csp.forward_checking)
    mac        = lambda ken: csp.backtracking_search(ken, inference=csp.mac)

    algorithms = {
        "BT": bt,
        
        "FC": fc,
        
        "MAC": mac
        
    }

    with open(out, "w+") as file:

        out = writer(file)

        out.writerow(["Algorithm", "Size", "Result", "Constraint checks", "Assignments", "Completion time"])

        for name, algorithm in algorithms.items():
            # for size in range(3, 10):
                size = 4
                checks, assignments, dt = (0, 0, 0)
                for iteration in range(1, iterations + 1):
                    size, cliq = generation(size)

                    assignment, data = benchmark(Kenken(size, cliq), algorithm)

                    print("algorithm =",  name, "size =", size, "iteration =", iteration, "result =", "Success" if assignment else "Failure", file=stderr)

                    checks      += data[0] / iterations
                    assignments += data[1] / iterations
                    dt          += data[2] / iterations
                    
                out.writerow([name, size, checks, assignments, dt])

    
def runner(x, algorithm, cliq):
            # size, cliq = generation(x)
            ken = Kenken(x, cliq)
            if(algorithm == "BT"):
                answer = csp.backtracking_search(ken)
            if(algorithm == "BTF"):
                answer = csp.backtracking_search(ken, inference=csp.forward_checking)
            if(algorithm == "BTARC"):
                answer = csp.backtracking_search(ken, inference=csp.mac)
            
            return answer

if __name__ == "__main__":

    # x, y = runner(3, "BT")
   
    size, cliq = generation(7)
    ken = Kenken(size, cliq)
    assignment = csp.backtracking_search(ken, inference=csp.mac)
   
