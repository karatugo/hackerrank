def get_biggest_region(grid):
    def get_region(i, j, visited=[]):
        region = [(i,j)]
        
        try:
            if grid[i-1][j+1] == 1 and i-1>=0:
                region.append((i-1,j+1))
        except:
            pass
        
        try:
            if grid[i+1][j] == 1:
                region.append((i+1,j))
        except:
            pass
        
        try:
            if grid[i][j+1] == 1:
                region.append((i,j+1))
        except:
            pass
        
        try:
            if grid[i+1][j+1] == 1:
                region.append((i+1,j+1))
        except:
            pass
        
        try:
            if grid[i-1][j+1] == 1 and i-1>=0:
                region.append((i-1,j+1))
        except:
            pass
        
        try:
            if grid[i-1][j] == 1 and i-1>=0:
                region.append((i-1,j))
        except:
            pass

        try:
            if grid[i+1][j-1] == 1 and j-1>=0:
                region.append((i+1,j-1))
        except:
            pass
        
        try:
            if grid[i][j-1] == 1 and j-1>=0:
                region.append((i,j-1))
        except:
            pass
        
        region = list(set(region))
        
        if len(region) > 1:
            for (a,b) in region:
                if not (a,b) in visited:
                    visited.append((a,b))
                    r = get_region(a,b,visited)
                    
                    for e in r:
                        if not e in region:
                            region.append(e)
        
        return region
    
    num_rows = len(grid)
    num_cols = len(grid[0])
    biggest_region = []
    
    
    for j in range(num_cols):
        for i in range(num_rows):
            if grid[i][j] == 1:
                region = get_region(i,j)
                
                if len(region) > len(biggest_region):
                    biggest_region = region

    return len(biggest_region)

n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
print get_biggest_region(grid)
