import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from simple_path import *

class Robot_Arm():
    def __init__(self):
        self.res = 2 # Precision of our table in number of decimals
        self.theta_0_range = np.arange(0, np.pi, 10**-self.res) # These are our joint limits
        self.theta_1_range = np.arange(0, np.pi, 10**-self.res)

        self.IK_table = {} # IK_table = {(x, y) : (theta_0, theta_1)}
        self.x_workspace = [] # All x values our robot can reach
        self.y_workspace = [] # All y values our robot can reach

        self.path = [] # Path in the task (x, y) space
        self.joint_path = [] # Path in the joint (theta_0, theta_1) space

        # Our robot arm's workspace does not change after we set joint limits
        # So, we can go ahead and build our IK_table
        self.make_IK_table()


    # We can generate a lookup table for our inverse kinematics using our forward version
    # We will loop through all input combinations of theta_0 and theta_1
    def make_IK_table(self):
        for theta_0 in self.theta_0_range:
            for theta_1 in self.theta_1_range:

                _, joint_2 = self.FK((theta_0, theta_1)) # "_" means we don't need that variable

                self.x_workspace.append(joint_2[0])
                self.y_workspace.append(joint_2[1])

                self.IK_table.update({joint_2: (theta_0, theta_1)})


    # Here we define our Forward Kinematics. This will take in joint angles and return joint positions
    def FK(self, theta):

        theta_0, theta_1 = theta # This notation lets us set the elements to variables

        x_joint_1 = np.cos(theta_0)
        y_joint_1 = np.sin(theta_0)

        x_joint_2 = x_joint_1 + np.cos(theta_0 + theta_1)
        y_joint_2 = y_joint_1 + np.sin(theta_0 + theta_1)

        # Our table will have finite precision, so we need to round the entries
        joint_1 = (round(x_joint_1, self.res), round(y_joint_1, self.res))
        joint_2 = (round(x_joint_2, self.res), round(y_joint_2, self.res))

        return joint_1, joint_2 # This packs the variables into a tuple 
    

    # This is a utility method
    def rad_to_deg(self, theta):
        theta_0 = round(theta[0] * 180/np.pi, self.res)
        theta_1 = round(theta[1] * 180/np.pi, self.res)

        return (theta_0, theta_1)
    


    # We can use this function to generate a path for our manipulator to follow
    def make_path(self, source_node, goal_node):
        # Our simple path was set up for a unit grid
        # That is okay because we can arbitrarily scale the grid

        # Multiply by 100 to get a scaled path, divide by 100 to convert back
        scale = 10**self.res

        source_scaled = (int(source_node[0] * scale), int(source_node[1] * scale))
        goal_scaled = (int(goal_node[0] * scale), int(goal_node[1] * scale))

        scaled_path = simple_path_plan(source_scaled, goal_scaled)

        # After we get the path we need to return the nodes to their original scale
        for scaled_node in scaled_path:
            node = (scaled_node[0]/scale, scaled_node[1]/scale)

            # Our IK_table does not contain a complete grid of (x, y) cooridnates 
            # So, we will check to see if the coordinate is in our table before we try to add it to the path
            if node in self.IK_table:
                self.path.append(node)

                # To perform our inverse kinematics, we simply have to lookup the node in our table
                self.joint_path.append(self.IK_table[node]) 





# Functions for animation ------------------------------------------------------------
# ------------------------------------------------------------------------------------

# Commonly, we will put the graph formatting in a function so we can apply it to multiple figures
def decorate_plot():

     # These are our graph limits and step size for ticks
    x_0 = -2.5
    x_1 = 2.5
    h_x = 0.5

    y_0 = 0
    y_1 = 2.5
    h_y = 0.5

    x_range = np.arange(x_0, x_1 + h_x, h_x) # REMEMBER! arange ends one step before the end!
    y_range = np.arange(y_0, y_1 + h_y, h_y)

    plt.grid()
    plt.xlim(x_0, x_1)
    plt.ylim(y_0, y_1)
    plt.xticks(x_range) 
    plt.yticks(y_range)
    plt.gca().set_aspect('equal')

    plt.xlabel("x-axis")
    plt.ylabel("y-axis")


# This function must be defined so the script will stop when we close the animation window
def on_close(event): 
    plt.close()
    exit()




# This is the animation loop 
def main_task(i, arm: Robot_Arm): # The first input is set aside for the current iteration
    
    # The animation needs to execute atleast one iteration to see the restults
    if i == len(arm.path):
        input("Press enter to quit")
        plt.close()
        exit()
    

    print("Frame:", i)
    plt.clf() # Clears the figure

    # Plot the workspace
    plt.plot(arm.x_workspace, arm.y_workspace, 'b.')

    # Plot the path
    # Our path is list of tuples 
    # * is called the upacking operator 
    # Zip is a class that reorders lists and tuples 
    # Ex: zip(*[(1, 2), (3, 4)]) is the equivalent of zip((1,2), (3,4))
    x_path, y_path = zip(*arm.path)
    plt.plot(x_path, y_path, 'k-')


    # Plotting the robot arm
    # Our path is determined outside of this function so we just have to grab the joint angles from our list
    theta = arm.joint_path[i]
    theta_degrees = arm.rad_to_deg(theta)
    print("Theta:", theta_degrees)


    # For plotting/simulation, we will feed this back into our FK
    joint_1, joint_2 = arm.FK(theta)

    plt.plot([0, joint_1[0], joint_2[0]], [0, joint_1[1], joint_2[1]], 'ro-')
    decorate_plot()
    plt.title("Theta: " + str(theta_degrees))
    
    
   

    

## Start of Script -------------------------------------------
## -----------------------------------------------------------

# Create arm object
arm = Robot_Arm() # When we make the object, the constructor will automatically build our IK_table
source_node = (-.5, 0)
goal_node = (-.5, 1.5)

arm.make_path(source_node, goal_node) # The path is not automatic, so we have to call the method directly


# Start animation
fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close) 
ani = animation.FuncAnimation(fig, main_task, interval=1, cache_frame_data = False, fargs=(arm,)) # fargs requires a "," even with a single input. Ex: fargs=(x,)
plt.show() # this must follow the animation call for you to actually see the plot







