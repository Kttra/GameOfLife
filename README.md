# GameOfLife
A program that simulates Conway's Game of Life. Written in python.
The Game of Life is a ceullular automated mathematical game with complex behavior.
The program first determines the next generation based on the cells that are alive given a grid. The grid can either be inputted manually or given though a txt file.

**How the game works**
-------------------------
The game is played on a rectangular grid. Each square on the grid can be either empty
(represented by a 0) or occupied by a living cell (represented by a 1). At 
the start, you can specify empty and occupied cells. Then the game will run
automatically afterwards. In each generation, the next generation is calculated. A new cell is 
born on an empty cell if it is surrounded by exactly three occupied neighbor cells. A 
cell dies of overcrowding if it is surrounded by four or more living neighbors. It dies
of loneliness if it is surrounded by zero or only one living neighbor. A neighbor is defined as an occupant 
of an adjacent cell to the left, right, top, or bottom or in a diagonal direction

**Animated**
----------------------
![Animated_Hwss](https://user-images.githubusercontent.com/100814612/159607577-d8de4a03-be3b-4c67-83fa-d50afcde8d2c.gif)
![Game_of_life_pulsar](https://user-images.githubusercontent.com/100814612/159607584-8bbe169a-e646-4abb-baae-58610507b770.gif)
![I-Column](https://user-images.githubusercontent.com/100814612/159607688-28d14766-9ff2-4335-a1b8-d4bf7ac301e0.gif)
![Game_of_life_animated_glider](https://user-images.githubusercontent.com/100814612/159607803-749185e9-6175-45fa-a584-07763d5d97d0.gif)


**Grid Example**
-------------------------
```
Grid = [[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0],
 [0, 1, 1, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]]
 
x = nextGen(grid)
[[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0], 
 [0, 1, 0, 1, 0, 0, 0],
 [0, 0, 1, 1, 0, 0, 0], 
 [0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]]
 
y = nextGen(x)
[[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 1, 0, 0, 0],
 [0, 1, 0, 1, 0, 0, 0], 
 [0, 0, 1, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]]
  
  z = nextGen(y)
[[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0], 
 [0, 0, 1, 1, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]]

```
**Txt File Example**
-------------------------
```
life()
Enter input file name: test.txt
How many new generations would you like to print? 5

Generation: 0
. . . . . . . 
. . . . . . . 
. . . * . . . 
. . . . * . . 
. . * * * . . 
. . . . . . . 

Generation: 1
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . * . * . . 
. . . * * . . 
. . . * . . . 

Generation: 2
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . . * . . 
. . * . * . . 
. . . * * . . 
Generation: 3
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . * . . . 
. . . . * * . 
. . . * * . . 

Generation: 4
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . . * . . 
. . . . . * . 
. . . * * * . 

Generation: 5
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . * . * . 
. . . . * * . 

Would you like to save the latest generation? ('y' to save): y
Enter destination file name: test2.txt

Saving data to test7.txt
```
