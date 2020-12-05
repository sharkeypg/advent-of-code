import os
import numpy as np

def import_data(rel_path):
    abs_file_path = os.path.join(os.getcwd(), rel_path)
    with open(abs_file_path) as forest_file:
        forest = [line.rstrip() for line in forest_file]
    return forest

def trajectory_one(arr):
    num_trees = 0

    size_y = len(arr)
    size_x = len(arr[1])

    x = 0; y = 0

    while y <= size_y - 1:
        if x+3 > size_x:
            arr = [line + line for line in arr]
            size_x = len(arr[1])
        if arr[y][x] == '#':
            num_trees += 1
        x+=3
        y+=1

    return num_trees

def trajectory_two(arr):

    total_trees = []
    slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

    for slope in slopes:
        num_trees = 0

        size_y = len(arr)
        size_x = len(arr[1])

        x = 0
        y = 0

        while y <= size_y - 1:
            if x + slope[0] > size_x:
                arr = [line + line for line in arr]
                size_x = len(arr[1])
            if arr[y][x] == '#':
                num_trees += 1
            x+=slope[0]
            y+=slope[1]
        total_trees.append(num_trees)

    return np.prod(total_trees)



if __name__ == '__main__':
    forest = import_data('data/day_3_input.txt')
    num_trees = trajectory_one(forest)
    tree_prod = trajectory_two(forest)
    print('The number of trees encountered is ' + str(num_trees))
    print('The product of tree numbers in each slope is ' + str(tree_prod))





