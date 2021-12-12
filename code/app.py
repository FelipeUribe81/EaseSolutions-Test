# import numpy as np
import sys

class challenge:
    def __init__(self, file:str) -> None:
        self.n, self.m, self.map = self.read_file(file)
        self.path = ''
        """ 
        The following variable is a representation of the movement matrix with the movements being:
        Up: i + (j+1), Down: i + (j-1), Right: (i+1) + j, Left: (i-1) + j

        The coefficient matrix would look like this:

                    u   d  r   l
        row 1 = i : [0, 0, 1, -1]
        row 2 = j : [1, -1, 0, 0]

        To save memory, the variable is represented as a one-dimensional vector.
        """
        self.moves = [0, 0, 1, -1, 1, -1, 0, 0]
        self.steps = 0
        self.drop = 0
        

    def read_file(self, file:str) -> None:
        input = open(f'../input/{file}', 'r')
        map = []

        for i, line in enumerate(input.readlines()):
            if i == 0:
                n, m = line.strip("\n").split(" ")
            else:
                """ 
                A compressed list is used to read the rows and they are added to the list called map.
                """
                row = [int(number) for number in line.strip("\n").split(" ")]
                map.append(row)

        return int(n), int(m), map

    def movement(self, i:int, j:int, steps:int, current:str, path:str):

        """ 
        To read the movements, a range is set corresponding to the number of elements over the total number of rows of the coefficient matrix 
        over the total number of rows of the coefficient matrix.
        """
        for move in range(len(self.moves)//2):
            isValid = i + self.moves[move] >= 0 and i + self.moves[move] < self.n and j + self.moves[move+len(self.moves)//2] >= 0 and j + self.moves[move+len(self.moves)//2] < self.m
            if (isValid and (self.map[i][j]> self.map[i + self.moves[move]][j + self.moves[move+len(self.moves)//2]])):
                """
                The element in the neighboring position is equated in the next variable being the neighbor up, 
                down, right and left according to the iteration.
                """
                step = self.map[i + self.moves[move]][j + self.moves[move+len(self.moves)//2]]
                """
                The possible paths must be evaluated for each node that is visited, so the recursion is performed, and the visited neighbor 
                must also be stored to know the traveled path.
                """
                self.movement(i + self.moves[move], j + self.moves[move+len(self.moves)//2], steps + 1, current, path + f' {step}')


        drop = current - self.map[i][j]
        #print(path.split(' '))
        """
        It is validated if the number of visited is greater than the one set in the global variable, by default, it is set as 0
        and the local number is initialized with 1. 
        """
        if (steps > self.steps):
            self.steps = steps
            self.drop = drop
            self.path = path

        """
        If the global and local quantities coincide, the drop between the initial and final values must be checked.
        """
        if (steps == self.steps and self.drop < drop):
            self.drop = drop
            self.path = path


    def searchPath(self) -> None:
        count = 0
        """
        We go through the matrix in order and one by one evaluating the correct path.
        """
        for i in range(self.n):
            for j in range(self.m):
                """
                In order to avoid going through sections of previously seen roads and to save time and movements, we 
                and to save time and movements, the position smaller than the current size of the path is omitted.
                """
                if (self.steps) < self.map[i][j]:
                    #count += 1
                    self.movement(i, j, 1, self.map[i][j], f'{self.map[i][j]}')
        self.path = self.path.replace(' ', '-')
        #print(count)

if __name__ == "__main__":
    file = sys.argv[1]
    print(file)
    app = challenge(file)
    app.searchPath()
    print(f'The path is: {app.path}\nThe steps and drop are: {app.steps}, {app.drop}')
