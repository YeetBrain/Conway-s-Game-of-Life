import time
# If a cell is alive, and 2 or 3 of it's neighbours are also alive, the cell remains alive.
# If a cell is alive and it has more than 3 alive neighbours, it dies of overcrowding.
# If a cell is alive and it has fewer than 2 alive neighbours, it dies of loneliness.
# If a cell is dead and it has exactly 3 neighbours it becomes alive again.

#Read coordinates from files
#Make grid, 30x60, make it all dead
#Put O's on graph, - is dead
#Set rules
#Run code

# checks the cell at row i col j in grid

def aliveCheck(count):
  if count == 2 or count == 3:
    
    return True
  else: 
    return False
    
def overCrowdingCheck(count):
  if count > 3:
    
    return True
  else: 
    return False
    
def lonelyCheck(count):
  if count < 2:
    
    return True
  else: 
    return False
    
def resurrectionCheck(count):
  if count == 3:
    
    return True
  else: 
    return False
    
    
def rules(i, j, grid):
  
  count=0
  
  if i != 0 and j != 0 and grid[i-1][j-1] == 'O':
    count+=1
  if i!=0 and j!=len(grid[0])-1 and grid[i-1][j+1] == 'O':
    count+=1
  if i!=0 and grid[i-1][j] == 'O':
    count+=1
  if j!=0 and grid[i][j-1] == 'O':
    count+=1
  if j!=len(grid[0])-1 and grid[i][j+1] == 'O':
    count+=1
  if i!= len(grid)-1 and j!=0 and grid[i+1][j-1] == 'O':
    count+=1
  if i!= len(grid)-1 and grid[i+1][j] == 'O':
    count+=1
  if i!= len(grid)-1 and j!= len(grid[0])-1 and grid[i+1][j+1] =='O':
    count+=1

  return count

def checkCell(i, j, grid):
  cell = grid[i][j]
  count = rules(i, j, grid)
  
  if cell == 'O':
    c1 = aliveCheck(count)
    c2 = overCrowdingCheck(count)
    c3 = lonelyCheck(count)
    
    if c1 == True:
      cell = 'O'
      
    elif c2 == True or c3 == True:
      cell = '-'
      
      
  elif cell == '-': 
    c4 = resurrectionCheck(count)
    
    if c4 == True:
      cell = 'O'
      
  return cell
    
def emptyGrid():
  grid = []
  for i in range(60):
    row = []
    for j in range(60):
      row.append('-')
    grid.append(row)
  return grid
    
def printGrid(grid):
  for row in grid:
    for column in row:
      print(column, end="")
    print("")
# This is the begining of processing the file
set1 = str(input("Please look at the files and type the name of the one you want exactly. Don't forget to include '.in': "))
coordinates = []
f = open(set1)
lines = f.readlines()
lines = [line.strip() for line in lines]
for line in lines:
  line = line.split()
  coordinates.append(line)
  
for coordinate in coordinates:
  coordinate[0] = int(coordinate[0])
  coordinate[1] = int(coordinate[1])

grid = emptyGrid()
  
for coordinate in coordinates:
  x = coordinate[0]
  y = coordinate[1]
  grid[x][y] = 'O'

print("begin")
printGrid(grid)
print(" ")
time.sleep(2)
while True:
  for i in range(60):
    for j in range(60):
      grid[i][j] = checkCell(i, j, grid)
  printGrid(grid)
  time.sleep(0.5)
