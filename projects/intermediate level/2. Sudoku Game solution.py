# using thew backtracking algo.

# board2 = [
#     [7,8,0,4,0,0,1,2,0],
#     [6,0,0,0,7,5,0,0,9],
#     [0,0,0,6,0,1,0,7,8],
#     [0,0,7,0,4,0,2,6,0],
#     [0,0,1,0,5,0,9,3,0],
#     [9,0,4,0,6,0,0,0,5],
#     [0,7,0,3,0,0,0,1,2],
#     [1,2,0,0,0,7,4,0,0],
#     [0,4,9,2,0,6,0,0,7]
# ]

board = [
    [7, 0, 2, 0, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 6, 1, 0, 4],
    [0, 6, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 0, 5, 9, 3, 2],
    [4, 7, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 6, 0, 0],
    [9, 0, 0, 0, 0, 1, 8, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 2, 9],
    [0, 0, 0, 5, 0, 0, 0, 0, 0]
]



def valid(bo_val, num, pos):
    # check row
    for i in range(len(bo_val[0])):
        if bo_val[pos[0]][i] == num and pos[1] != i:
            # print("wrong")                            # For understanding where is the incorrect form
            return False

    # check column
    for i in range(len(bo_val)):
        if bo_val[i][pos[1]] == num and pos[0] != i:
            # print("wrong 2")                          # For understanding where is the incorrect form
            return False
        
    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range (box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo_val[i][j] == num and (i,j) != pos:
                #  print("wrong 3")      # For understanding where is the incorrect form
                return False
    return True


def print_board(bo_val):

    for i in range(len(bo_val)):
        if i%3 == 0 and i != 0:
            print("----------------------")
        for j in range(len(bo_val[0])):
            if j%3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo_val[i][j])
            else:
                print(str(bo_val[i][j]) + " ", end="")


def find_empty(bo_val):
    for i in range(len(bo_val)):
        for j in range(len(bo_val[0])): 
            if bo_val[i][j] == 0:
                return (i, j)
    return None


def solve(bo_val):
    find = find_empty(bo_val)
    if not find:
        return True
    
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo_val, i, (row, col)):
            bo_val[row][col] = i

            if solve(bo_val):
                return True

            bo_val[row][col] = 0

    # print("wrong 4")     # For understanding where is the incorrect form
    return False


print_board(board)
solve(board)
print("----------------------------------")
print("----------------------------------")
print_board(board)
