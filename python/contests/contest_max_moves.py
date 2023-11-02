def maxMoves(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # Can start from any cell in the first column
    row = 0
    col = 0
    moves = 0
    for col in range(len(grid[0])):
        positions = [0, 0, 0]
        if row - 1 >= 0 and col + 1 < len(grid[0]):
            positions[0] = grid[row - 1][col + 1]
        if col + 1 < len(grid[0]):
            positions[1] = grid[row][col + 1]
        if row + 1 < len(grid) and col + 1 < len(grid[0]):
            positions[2] = grid[row + 1][col + 1]
        max_val = max(positions)
        if max_val == 0 or max_val < grid[row][col]:
            return moves

        col += 1
        row += positions.index(max_val) - 1
        moves += 1
