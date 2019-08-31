# Function to print a "beam" pattern of the given width
def printBeam(width):
    print('+' + (' -' * width), end = ' ')


# Function to print a "post" pattern of the given width
def printPost(width):
    print('|' + ('  ' * width), end = ' ')


# Function to print the requested number of beam columns (with the given width)
def printBeams(columns, width):
    for c in range(columns):
        printBeam(width)
    print('+')


# Function to print the requested number of post columns (with the given width)
def printPosts(columns, width):
    for c in range(columns):
        printPost(width)
    print('|')


# Function to print a complete grid row with the desired number of columns and the given cell width and height
def printRow(columns, width, height):
    printBeams(columns, width)
    for h in range(height):
        printPosts(columns, width)


# Function to print a complete grid with default values for the number of rows, columns, and cell width and height
def printGrid(rows = 2, columns = 2, width = 4, height = 4):
    for r in range(rows):
        printRow(columns, width, height)
    printBeams(columns, width)


# Alternate function to print a grid of a desired size (Always prints a 2x2 grid with variable cell size)
def printGridSize(size):
    printGrid(2, 2, size // 2, size // 2)


# Alternate function to print a grid of a desired size (square) and cell size
def printGridSizes(gridSize, cellSize):
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
