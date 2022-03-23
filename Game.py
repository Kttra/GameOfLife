## Created by Kttra
##
## The Game of Life

import copy

def nextGen(grid):
    '''Takes a list and runs it through the game of life
    Parameter grid expects a list'''
    grid_copy = copy.deepcopy(grid)     ## Copies the grid 
    zero_list = [[]]                
    for i in range(len(grid[0])+2):     ## Creates a border of zeros around the grid copy
        zero_list[0].append(0) 
    grid_copy = grid_copy + zero_list
    grid_copy = zero_list + grid_copy
    for num in range(1,len(grid_copy)):
        grid_copy[num] = grid_copy[num] + [0]
        grid_copy[num] = [0] + grid_copy[num]
    next_Gen = []
    

    for index in range(len(grid)):      ## Creates a new grid for the result/next generation
        next_Gen.append([])


    for i in range(1,len(grid_copy)-1): ## Analyzes the cell's neighbors
        for j in range(1,len(grid_copy[0])-1):
            neighbours = 0
            cell = 0
            if grid_copy[i-1][j-1] == 1:
                neighbours = neighbours + 1
            if grid_copy[i-1][j] == 1:
                neighbours = neighbours + 1
            if grid_copy[i-1][j+1] == 1:
                neighbours = neighbours + 1
            if grid_copy[i][j-1] == 1:
                neighbours = neighbours + 1
            if grid_copy[i][j+1] == 1:
                neighbours = neighbours + 1
            if grid_copy[i+1][j-1] == 1:
                neighbours = neighbours + 1
            if grid_copy[i+1][j] == 1:
                neighbours = neighbours + 1
            if grid_copy[i+1][j+1] == 1:
                neighbours = neighbours + 1


            if grid_copy[i][j] == 1:    ## Checks to see if the cell lives or dies or if a cell is created
                cell = 1
            else:
                cell = 0            
            if (cell == 0 and neighbours == 3):
                next_Gen[i-1].append(1)
            elif (cell == 1 and (neighbours == 2 or neighbours == 3)):
                next_Gen[i-1].append(1)
            else:
                next_Gen[i-1].append(0)
    return next_Gen


## Second half of the program

import os

def life():     
    '''Runs the Game of life through the inputted number of generations
    Gets a list from a .txt file
    Saves the last generation to a .txt file if the user desires''' 
    while True:                         ## Gets the .txt file name
        filename = input("Enter input file name: ")
        try:
            file = open(filename)
            break
        except:
            print("No such file. Try again.")
    while True:
        try:
            num = int(input("How many new generations would you like to print? "))
            break
        except:
            print("Not a valid number.")


    txt_grid = []                       ## Converts the .txt file contents into a list
    row = 0
    for line in file:
        txt_grid.append([])
        for i in range(len(line)):
            try:
                txt_grid[row].append(int(line[i]))
            except:
                pass
        row = row + 1
    print("\nGeneration: 0")
    convert(txt_grid)                   ## Refer to function convert at the bottom
  

    for i in range(1,num+1):            ## Outputs the next generation to the user
        print("\nGeneration:",i)
        txt_grid = nextGen(txt_grid)
        convert(txt_grid)

                                        ## Asks user the name of the file they want to save the last generation to
    save = input("Would you like to save the lastest generation? ('y' to save): ")
    if save == 'y':
        name = input("Enter destination file name: ")
        over_write = True
        while os.path.exists(name) == True:
            over_write = input("Do you want to overwrite that file? ('y' to continue): ")
            if over_write == 'n':
                name = input("Enter destination file name: ")
            elif over_write == 'y':
                break
            else:
                pass
        print("\nSaving data to", name)


        outFile = open(name,"w")        ## Saves and writes the generation into the .txt file
        writestring = ""
        for row in txt_grid:
            for number in row:
                outFile.write(str(number))
            outFile.write("\n")
        outFile.close()
        return None
    else:
        print("End of program.")

    
def convert(txt_grid):  
    '''Converts the 0's and 1's in a grid into "." and "*" repectively
    Parameter txt_grid expects a list
    Prints out the generation to the user'''
    for row in txt_grid:
        for number in row:
            if number == 1:
                print("*",end = " ")
            else:
                print(".",end = " ")
        print("\n");#newline to make formatting look more normal


