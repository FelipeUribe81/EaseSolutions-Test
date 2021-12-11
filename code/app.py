# import numpy as np

from os import path


class challenge:
    def __init__(self) -> None:
        self.n, self.m, self.map = self.read_file()
        self.path = ''
        # self.moves = {"up": [-1, 0], "down": [1, 0], "right": [0, 1], "left": [0, -1]}
        # self.edge = {"up": 0, "down": self.n, "right": self.m, "left": 0}
        self.moves = [0, 1, 0, -1, 1, 0, -1, 0]
        self.steps = 0
        self.drop = 0
        

    def read_file(self):
        input = open("../input/4x4.txt", "r")
        map = []

        for i, line in enumerate(input.readlines()):
            row = []
            if i == 0:
                n, m = line.strip("\n").split(" ")
            else:
                [row.append(int(number)) for number in line.strip("\n").split(" ")]
                map.append(row)

        return int(n), int(m), map

    def movement(self, i, j, steps, current, path):
        
        for move in range(len(self.moves)//2):
            isValid = i + self.moves[move] >= 0 and i + self.moves[move] < self.n and j + self.moves[move+len(self.moves)//2] >= 0 and j + self.moves[move+len(self.moves)//2] < self.m
            if (isValid and (self.map[i][j]> self.map[i + self.moves[move]][j + self.moves[move+len(self.moves)//2]])):
                step = self.map[i + self.moves[move]][j + self.moves[move+len(self.moves)//2]]
                self.movement(i + self.moves[move], j + self.moves[move+len(self.moves)//2], steps + 1, current, path + f' {step}')

        drop = current - self.map[i][j]
        print(path.split(' '))
        if (steps > self.steps):
            self.steps = steps
            self.drop = drop
            self.path = path

        if (steps == self.steps and self.drop < drop):
            self.drop = drop
            self.path = path

    # def movement(self, i, j, length, actual, path):
    #     move_i = [0, 1, 0, -1]
    #     move_j = [1, 0, -1, 0]
    #     for k in range(4):
    #         inside = i + move_i[k] >= 0 and i + move_i[k] < self.n and j + move_j[k] >= 0 and j + move_j[k] < self.m
    #         # inside = (
    #         #     (move == "up" and i + value[0] >= self.edge[move])
    #         #     or (move == "down" and i + value[0] < self.edge[move])
    #         #     or (move == "right" and j + value[1]) < self.edge[move]
    #         #     or (move == "left" and j + value[1] >= self.edge[move])
    #         # )
    #         if inside and self.map[i][j] > self.map[i + move_i[k]][j + move_j[k]]:
    #             # if ():
    #             neighbor = self.map[i + move_i[k]][j + move_j[k]]
    #             return self.movement(
    #                 i + move_i[k], j + move_j[k], length + 1, actual, path + f'{neighbor}'
    #             )

    #     drop = actual - self.map[i][j]

    #     if length > self.steps:
    #         self.steps = length
    #         self.drop = drop
    #         self.path = path
    #         # self.path = path
    #         # self.drop = drop

    #     if length == self.steps:
    #         if self.drop < drop:
    #             self.drop = drop
    #             self.path = path
    #             # self.drop = drop

    def search(self):
        for i in range(self.n):
            for j in range(self.m):
                if (self.steps) < self.map[i][j]:
                    self.movement(i, j, 1, self.map[i][j], f'{self.map[i][j]}')
        self.path = self.path.replace(' ', '-')


if __name__ == "__main__":
    app = challenge()
    app.search()
    print(app.path)
    # print(app.drop)

    #   print(app.n, app.m, app.map)
