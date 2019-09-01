def printBeam(width):
    """
    Function to print a single column of the beam pattern for a grid cell

    :param width:   Width of the grid cell
    """
    print('+' + (' -' * width), end = ' ')


def printPost(width):
    """
    Function to print a single column of the post pattern for a grid cell

    :param width:   Width of the grid cell
    """
    print('|' + ('  ' * width), end = ' ')


def printBeams(columns, width):
    """
    Function to print the given number of columns of the beam pattern for grid cells

    :param columns: Number of beam columns to print
    :param width:   Width of the grid cell
    """
    for c in range(columns):
        printBeam(width)
    print('+')


def printPosts(columns, width):
    """
    Function to print the given number of columns of the post pattern for grid cells

    :param columns: Number of post columns to print
    :param width:   Width of the grid cell
    """
    for c in range(columns):
        printPost(width)
    print('|')


def printRow(columns, width, height):
    """
    Function to print the given number of columns of the complete (beam/post) patterns for grid cells (Complete row)

    :param columns: Number of columns to print
    :param width:   Width of the grid cell
    :param height:  Height of the grid cell
    """
    printBeams(columns, width)
    for h in range(height):
        printPosts(columns, width)


def printGrid(rows = 2, columns = 2, width = 4, height = 4):
    """
    Function to print a complete grid of beam/post patterns

    :param rows:    Number of rows in the grid (Defaults to a grid of 2 rows)
    :param columns: Number of columns in the grid (Defaults to a grid of 2 columns)
    :param width:   Width of a grid cell (Defaults to a grid cell width of 4)
    :param height:  Height of a grid cell (Defaults to a grid cell height of 4)
    """
    for r in range(rows):
        printRow(columns, width, height)
    printBeams(columns, width)


# Alternate function to print a grid of a desired size (Always prints a 2x2 grid with variable cell size)
def printGridSize(size):
    """
    Alternate function to print a complete grid of beam/post patterns of a requested size

    :param size:    Determines the size of the grid cell (width and height, grid size is 2x2)
    """
    printGrid(2, 2, size // 2, size // 2)


def printGridSizes(gridSize, cellSize):
    """
    Alternate function to print a complete grid of beam/post patterns of the requested sizes

    :param gridSize:    Determines the size of the grid (rows and columns, grid is always square)
    :param cellSize:    Determines the size of the grid cell (width and height, grid cell is always square)
    """
    printGrid(gridSize, gridSize, cellSize, cellSize)


# Test cases for the grid functions above

# Print a grid of the default size (2x2 grid with a 4x4 cell size)
printGrid()

# Print a couple of grids with the alternate function to specify grid cell size (2x2 grids)
printGridSize(3)
printGridSize(9)

# Print a couple of grids with the second alternate function to specify both grid and cell size
printGridSizes(3, 4)
printGridSizes(4, 2)

# Print a couple of grids with the function that takes all the grid arguments (Row, Columns, Width, Height)
printGrid(3, 4, 6, 4)
printGrid(5, 5, 2, 2)
