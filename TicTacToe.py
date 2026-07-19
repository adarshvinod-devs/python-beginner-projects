import os
os.system("cls")
grid = [" "," "," "," "," "," "," "," "," ",]

combo = [[0,1,2],[3,4,5],[6,7,8],
         [0,3,6],[1,4,7],[2,5,8],
         [0,4,8],[2,4,6]]

winstatus = False

def clear():
  #print("\033[H", end="")
  os.system("cls")

def print_grid():
  print(f" {grid[0]}|{grid[1]}|{grid[2]} ")
  print("-------")
  print(f" {grid[3]}|{grid[4]}|{grid[5]} ")
  print("-------")
  print(f" {grid[6]}|{grid[7]}|{grid[8]} ")

def check_winX():
  for i in combo:
    if grid[i[0]] == grid[i[1]] == grid[i[2]] == "X":
      os.system("cls")
      print_grid()
      print("Player 1 wins!!!")
      global winstatus
      winstatus = True

def check_winO():
  for i in combo:
    if grid[i[0]] == grid[i[1]] == grid[i[2]] == "O":
      os.system("cls")
      print_grid()
      print("Player 2 wins!!!")
      global winstatus
      winstatus = True
      
def drawX(mark):
    grid[mark - 1] = "X"
    print_grid()

def drawO(mark):
    grid[mark- 1 ] = "O"
    print_grid()

      
print_grid()

for i in range(9):
  if i % 2 == 0:
    mark = int(input("Player 1: Choose your grid [1 - 9]: "))
    while True:
      if grid[mark -1] == " ":
        clear()
        drawX(mark)
        check_winX()
        break
      else:
        mark = int(input("Player 1: Choose a valid grid [1 - 9]: "))
        os.system("cls")
        print_grid()
       
  else:
     mark = int(input("Player 2: Choose your grid [1 - 9]: ")) 
     while True:
      if grid[mark -1] == " ":
        clear()
        drawO(mark)
        check_winO()
        break
      else:
        mark = int(input("Player 2: Choose a valid grid [1 - 9]: "))
        os.system("cls")
        print_grid()

  if winstatus:
    break 
  elif not winstatus and i == 8:
    print("Draw")