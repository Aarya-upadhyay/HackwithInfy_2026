def gridChallenge(grid):
    n = len(grid)
    
    # sort rows
    for i in range(n):
        grid[i] = ''.join(sorted(grid[i]))
    
    m = len(grid[0])
    
    # check columns
    for col in range(m):
        for row in range(1, n):
            if grid[row][col] < grid[row-1][col]:
                return "NO"
    
    return "YES"
