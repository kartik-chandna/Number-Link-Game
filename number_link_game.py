import random

class Board:
    def __init__(self,size):
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.delta = [[-1, 0],[0,-1],[1,0],[0,1]]
        self.visited = [[ False for _ in range(self.size)] for _ in range(self.size)]
        
    def count_boxes(self):
        self.count = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == -2:
                    pass
                else:
                    self.count += 1
    
    def initialize_board(self):
        self.path_num = 1
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    self.board[i][j] = -2
                    if self.create_path(i,j,self.path_num, 1):
                        self.board[i][j] = self.path_num
                        self.path_num += 1
        self.count_boxes()
        
    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == -2:
                    print('X', end = ' ')
                elif self.board[i][j] < 0:
                    print('.', end = ' ')
                else:
                    print(str(self.board[i][j]), end = ' ')
            print()
            print()
                        
    def create_path(self, i, j, path_num, path_length):
        if random.choice([num for num in range(0,self.size)]) == 0:
            if path_length> 1:
                self.board[i][j] = path_num
                return True
            return False
        
        random.shuffle(self.delta)
        for deltax,deltay in self.delta:
            if self.is_valid_idx(i+deltax,j+deltay) and self.board[i+deltax][j+deltay] == 0:
                self.board[i+deltax][j+deltay] = -1
                return self.create_path(i+deltax,j+deltay, path_num, path_length+1)
        if path_length> 1:
            self.board[i][j] = path_num
            return True
        return False
        
    def is_valid_idx(self, i, j):
        return 0<=i<self.size and 0<=j<self.size

    def check_path(self, path):
        if len(path) > 0:
            val = self.board[path[0][0]][path[0][1]]
            if val <= 0 or val != self.board[path[-1][0]][path[-1][1]]:
                return False
            for i in range(1, len(path)):
                if (not self.is_neighbour(path[i-1], path[i])):
                    return False
                if i != len(path) - 1 and self.board[path[i][0]][path[i][1]] != -1:
                    return False
                self.board[path[i][0]][path[i][1]] = val
        return True
            
    def is_neighbour(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        if (abs(x1-x2) == 1 and abs(y1-y2) == 0) or (abs(x1-x2) == 0 and abs(y1-y2) == 1):
            return True
        return False

    def play(self):
        count = 0
        for _ in range(self.path_num-1):
            print('Enter 1: To input the path')
            print('Enter 2: To exit')
            num = input()

            if num != '1':
                break
            
            print('Enter the path: ')
            inputs = list(input().split(','))
            arr = []
            for inp in inputs:
                arr.append(list(map(int, inp.split())))

            count += len(arr)
            if not self.check_path(arr):
                self.print_board()
                print('SORRY!!  YOU LOSE')
                return
            elif count == self.count:
                self.print_board()
                print('***** YOU WIN *******')
                return
            self.print_board()
        print('SORRY!!  YOU LOSE')
    
if __name__ == '__main__':
    size = int(input('Enter the size of the board: '))
    b = Board(size)
    b.initialize_board()
    b.print_board()
    b.play()
