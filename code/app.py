# import numpy as np

class challenge():
    
    def __init__(self) -> None:
        self.n, self.m, self.matrix = self.read_file()
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
    
if __name__ == "__main__":
    app = challenge()
    print(f'n: {app.n}, m: {app.m}')
