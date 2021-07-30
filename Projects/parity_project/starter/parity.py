import csv


def load_grid(csv_file_path):
    """Loads data from a csv file.

    Args:
        csv_file_path: string representing the path to a csv file.
    Returns:
        A list of lists, where each sublist is a line in the csv file.
    """
    data = []

    with open(csv_file_path, mode = 'r', encoding = "utf-8") as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=",")
        for line in csv_reader:
            data.append(line)
    return data


# print(load_grid('tests/grids/medium_grid.csv'))

def add_column(grid):
    """Adds a new column to a grid. For each row, if there is an even
    number of X characters, a O is added to the row, otherwise a X is added
    to the row.

    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.

    Returns:
        The same grid, with a new column added.
    """
    count_x = 0 
    count_O = 0
    new_column = []
    # print(grid)
    for row in grid:
        # print(row)
        for char in row:
        #count the number of x's
            if char == 'X':
                count_x += 1
            else:
                count_O+= 1
        if count_x%2 == 0:
            new_column.append('O')
        else:
            new_column.append('X')
        
        for item in new_column:
            row.append(item)

        # print(count_x)
    # print(new_column)
    return type(grid)

#returning none at the end??
    
# grid = load_grid('tests/grids/medium_grid.csv')
# x = add_column(grid)
# print(x)

def add_row(grid):
    """Adds a new row to a grid. For each column, if there is an even
    number of X characters, a O is added to the column, otherwise a X is added
    to the column.

    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.

    Returns:
        The same grid, with a new row added.
    """
#transpose the grid
    grid = map(list, zip(*grid))
    count_x = 0 
    count_O = 0
    new_row = []
    # print(grid)
    for row in grid:
        # print(row)
        for char in row:
        #count the number of x's
            if char == 'X':
                count_x += 1
            else:
                count_O+= 1
        if count_x%2 == 0:
            new_row.append('O')
        else:
            new_row.append('X')
        
        for item in new_row:
            row.append(item)

    # print(count_x)
    # print(new_row)
    # print(grid)
#     return grid
    
# grid = load_grid('tests/grids/medium_grid.csv')
# print(add_row(grid))


def flip_cell(x_pos, y_pos, grid):
    """Prompts the user to choose a cell to swap from X to O (or vice versa).

    Arguments:
        x_pos: An integer representing the x coordinate of the cell.
        y_pos: An integer representing the y coordinate of the cell.
        grid: A list of lists, where each sublist represents a row in a grid.

        In the following grid:
            a b
            c d
        These are the coordinates of each letter:
            a = x: 0, y: 0
            b = x: 1, y: 0
            c = x: 0, y: 1
            d = x: 1, y: 1

    Returns:
        The same grid, with a cell switched.
    """

    #CURRENT ANSWER

    #check current grid position
    print(grid[y_pos][x_pos])

    #flip the cell
    if grid[y_pos][x_pos] == 'X':
        #is this the correct way to reassign a position ??
        grid[y_pos][x_pos] == 'hello'
    else:
        grid[y_pos][x_pos] == 'goodbye'

    #check if the cell is flipped
    print(grid[y_pos][x_pos])

    # return grid 

    
grid = load_grid('tests/grids/medium_grid.csv')
flip_cell = flip_cell(0,1,grid)
print(flip_cell)


def find_flipped_cell(grid):
    """Determines which cell/cell in the grid was flipped.

    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.

    Returns:
        A list containing the coordinates of the cell with the flipped cell.
        In the following grid:
            a b
            c d
        These are the coordinates of each letter:
            a = (0, 0)
            b = (1, 0)
            c = (0, 1)
            d = (1, 1)
        If 'a' was the flipped letter, this function would return: [0, 0]
    """
    #LOGIC
    #counts number of x's and o's in input grid
    #adds a column and row -> counts number of x's and o's in each column
    #use flip cell function to flip a cell
    #counts the number of x's and o's again
    #the row/column that is different to the original count is the flipped cell

