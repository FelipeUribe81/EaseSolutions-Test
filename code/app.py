# import numpy as np

class challenge():
    
    def __init__(self) -> None:
        self.n, self.m, self.matrix = self.read_file()
        self.moves = {'up': [-1, 0], 'down':[1, 0], 'right':[0, 1], 'left':[0, -1]}
        self.edge = {'up': 0, 'down':self.n, 'right':self.m, 'left':0}
        self.path = []
        
        
    def read_file(self):
        input = open('../input/4x4.txt','r')
        matrix = []
        
        for i, line in enumerate(input.readlines()):
            row = []
            if i == 0:
                n, m = (line.strip('\n').split(' '))
            else:
                [row.append(int(number)) for number in line.strip('\n').split(' ')]
                matrix.append(row)

        return int(n), int(m), matrix

    def movement(self, i, j, actual, path = []):
        for move, value in self.moves.items():
            count = 0
            if (move == 'up' and i+value[0] >= self.edge[move] or move == 'down' and i+value[0] < self.edge[move] or move == 'right' and j+value[1] < self.edge[move] or move == 'left' and j+value[1] >= self.edge[move]):
                if (self.matrix[i+value[0]][j+value[1]] < self.matrix[i][j]):
                    print(f'actual: {actual}')
                    print(self.matrix[i+value[0]][j+value[1]])
                    count +=1
                    self.movement(i+value[0],j+value[1], self.matrix[i+value[0]][j+value[1]], self.path)
        print(count)
                

    def search(self):
        for i in range(self.n):
            for j in range(self.m):
                app.movement(i, j, self.matrix[i][j])

    
if __name__ == "__main__":
    app = challenge()
    app.search()
    #   print(app.n, app.m, app.matrix)
    