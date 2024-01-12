This is the readme.txt file for the RBE 100X Final Project
How to get the robot running:
Go to the main.py file, and create new paths following the conventions outlined inside. There you can declare any blocked nodes per path, as well as the destination and source nodes. 

Once complete, upload the code to the XRP, and turn on the robot.

To test locally, or troubleshoot, run "main.py" in the terminal. Executing other files will result in errors

Detailed Breakdown of the Codebase:

The robot is organized as a finite state machine with the following states:
1. START
2. PATH_GEN
3. EXECUTING
4. END

During the start state, the robot will simply set the variable path_index to 1, and then await the USER BUTTON to be pressed on the XRP, which will set the robot's state to the PATH_GEN state. 
There are as many paths as are inputting into main.py, this just defines the starting path option. 
Once in the PATH_GEN state, the robot will run dijstra.py for path 1, and compile the instructions, which are either turn commands or drive commands. Specifically, there are the following commands: turn_left, turn_right (which turn 90 degrees respectively), and drive_forward. 

The list of inductions is formatting as the next node to go to. This is beneficial because it provides an ease of comparing where the robot is to where it is trying to go. Because it can tell the direction its to be traveling in, it can relate it's current heading to its future heading and move accordinly. 
The algorithm for generating the instructions is as follows:
    If there is a change in X or Y direction from the current node to the next node (the robot starts at the starting node), then there is a drive_forward command issued.
    If there is a change in X (or Y) followed by a change in Y (or X), then there is a turn command issued. The direction or count is depending on the current heading of the robot. 

The turn command algorithm is always the first comparison to be made, before the robot is issued any other commands. This is to always correctly orient the robot to drive forwards in the right direction. This means the robot's initial heading is required.

Once this instruction set is generated, the robot's state is set to EXECUTING.

In the EXECUTING state, the robot iterates through each step in the instruction set, and executes them according. 

On the drive forward command, the robot uses a PID loop to stay on the line of the grid. This is ideal because the robot can adapt to any inconsistencies in the grid and still stay on path. This is compared to something based on encoders, where straight to the robot may not actually be straight in the context of the grid. The ending condition for the drive_forward command is when an intersection is detected, which immediately stops the loop telling the robot to drive forward.
This also prevents the need for any "debouncing" of the intersection detection, because the normal conditions for an intersection being detected are unrealistic while simply driving straight.

On turn commands, the robot only moves one of the wheels, to achieve a turn radius. This is ideal because the robot turns such that the line follower will always be directed towards the line which is it's next path. The precise angle the turn command will issue is less than 90 degrees, so if there is error, the drive forward command can correct and keep the robot on the correct path. 

This is opposed to driving forward until an intersection is detected, then moving a set distance with encoders so the turn center is over the intersection, then turning 90 degrees, which could steer the robot in any direction with error.

When the instruction set is complete, if the final path has not been completed, the robot will set it's path_number+=1, and set it's state to PATH_GEN, where it generates the next path's instruction set, and repeat for n number of paths. 

If the final path has been completed, the robot will set it's state to END

In the END state, the robot will blink a light indicating that it finished the number of paths required. 

