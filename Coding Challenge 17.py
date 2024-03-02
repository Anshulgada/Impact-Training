"""
Robot movement in a grid:

Description:
You are given a great representing a robot’s movement with obstacles and boundaries. The robot starts at position (0,0) in the grid, facing upwards. The grid is represented by a string containing characters, U, D, L, R and X, where:
U represents moving up
D represents moving down.
L represents moving left. 
R represents moving right. 
X represents an obstacle that robot cannot move through.
Your task is to determine the final position of the robot after following the movement specified in the grid, taking into account the obstacles and boundaries. Assume that each movement results in a 1-step displacement and the robot cannot move to a position occupied by an obstacle or outside the boundaries of the grid.
Write a function final_position(grid:str, rows:int, cols:int) -> Tuple[int, int] that takes The great string number of rows and number of columns as input and returns the final position of the robot as a couple of two integers, representing the X coordinate and Y coordinates, respectively.

Example:
Grid: “UDDLLRUUUDUURUDDUULLDRRRR”
Rows:5
Columns:5

In the given example:
U moves the robot 1 step up. 
D moves the robot 1 step down. 
L moves the robot 1 step left. 
R moves the robot 1 step right. 
After following the movement specified in the grid, the robot ends up at position (4, 4).

Constraints:
The great string will consist only of characters U, D, L, R and X.
The final position of the robot will always be within the range of the grid. 
The robot cannot move to a position occupied by the obstacle X. 
The robot cannot move outside the border of the grid, which is represented by the given number of rows and columns.

Sample input:
1. UDDLLRUUUDUURUDDUULLDRRRR        -->  Grid String
2. 5                                -->  Rows
3. 5                                -->  Columns
4. 2                                -->  Num of Obstacles
5. 2 2                              -->  Coordinates of obstacle 1
6. 3 3                              -->  Coordinates of obstacle 2
Sample Output:
Final position of the robot: (2, 3)

Explanation:
First line is the grid string. 
Second line is the number of rows. 
Third line is the number of columns.
Fourth line is the number of obstacles. 
And from 5th line onwards are the obstacle coordinates.

The coordinates are distilled in a 0-indexed format where the first number represents the X-coordinate (column). And the second number represents the Y-coordinate (row) with (0, 0) being the original starting position.
"""

def final_position(grid, rows, cols, obstacles):

    x, y = 0, 0  # Starting position

    for move in grid:

        if move == 'U' and y < rows - 1 and (x, y + 1) not in obstacles:
            y += 1

        elif move == 'D' and y > 0 and (x, y - 1) not in obstacles:
            y -= 1

        elif move == 'L' and x > 0 and (x - 1, y) not in obstacles:
            x -= 1

        elif move == 'R' and x < cols - 1 and (x + 1, y) not in obstacles:
            x += 1

        elif move == 'X':
            continue  # Obstacle encountered, do not move

    return x, y

if __name__ == "__main__":

    # Input for grid, rows, and columns
    grid = input()
    rows= int(input())
    cols = int(input())

    # Input obstacle coordinates
    obstacle_count = int(input())
    obstacles = [tuple(map(int, input().split())) for _ in range(obstacle_count)]

    # Get the final position
    final_pos = final_position(grid, rows, cols, obstacles)

    # Print the final position
    print(f"Final position of the robot: {final_pos}")