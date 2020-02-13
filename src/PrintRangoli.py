import string

def printBoard(board): 
    for row in board:
        for char in row:
            print(char, end = '')
        print("")
        
def print_rangoli(size):
    width = 4 * size - 3
    height = size + size -1
    board = [['-' for i in range(0, width)] for i in range(0, height)]
    
    medium_row = int((height - 1) / 2)
    medium_column = int((width - 1) / 2)
    
    for index in range(size):
        character = string.ascii_letters[index]
        east_column = medium_column + 2*index
        west_column = medium_column - 2*index
        for internal_index in range(index + 1):
            board[medium_row - internal_index][west_column + 2*(internal_index)] = character
            board[medium_row - internal_index][east_column - 2*(internal_index)] = character
            board[medium_row + internal_index][west_column + 2*(internal_index)] = character
            board[medium_row + internal_index][east_column - 2*(internal_index)] = character

    printBoard(board)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)