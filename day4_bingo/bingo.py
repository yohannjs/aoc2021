import numpy as np

bingo_test_file = 'test_data.txt'
bingo_real_file = 'input_data.txt'

input_file  = open(bingo_test_file, 'r')
file_content = input_file.readlines()

numbers_drawn = [int(el) for el in file_content[0].split(',')]
bingo_boards_start_line = 3
file_end_line = len(file_content)

bingo_boards = []

while (bingo_boards_start_line < file_end_line):
    bingo_lists = []
    for i in range(5):
        single_bingo_row = file_content[bingo_boards_start_line + i]
        bingo_lists.append(single_bingo_row[:-2].split(' '))
    bingo_boards_start_line += 6
    bingo_boards.append(bingo_lists)

print(bingo_boards[0])