import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


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

    plt.title("Title")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")


# This function must be defined so the script will stop when we close the animation window
def on_close(event): 
    plt.close() 




class Robot_Arm():
    def __init__(self):
        self.res = 2 # Precision of our table in number of decimals
        self.theta_0_range = np.arange(0, np.pi/2, 10**-self.res)
        self.theta_1_range = np.arange(0, np.pi/2, 10**-self.res)

        self.IK_table = {}
        self.x_workspace = []
        self.y_workspace = []

        self.make_IK_table()


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




# This is the animation loop 
def main_task(i, arm: Robot_Arm): # The first input is set aside for the current iteration
    
    # The animation needs to execute atleast one iteration to see the restults
    if i > 0:
        input("Press enter to quit")
        plt.close()
        exit()
    

    print("Frame:", i)
    plt.clf() # Clears the figure

    # Plot the workspace
    plt.plot(arm.x_workspace, arm.y_workspace, 'b.')


    # Our goal, dictate endeffector position, get angles 
    coord = (1, 1)
    theta = arm.IK_table[coord]


    # For plotting/simulation, we will feed this back into our FK
    joint_1, joint_2 = arm.FK(theta)
    
    plt.plot([0, joint_1[0], joint_2[0]], [0, joint_1[1], joint_2[1]], 'ro-')
    decorate_plot()
    
    
   

    

## Start of Script -------------------------------------------
## -----------------------------------------------------------

# Create arm object
arm = Robot_Arm()

# Start animation
fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close) 
ani = animation.FuncAnimation(fig, main_task, interval=1000/25, cache_frame_data = False, fargs=(arm,)) # fargs requires a "," even with a single input. Ex: fargs=(x,)
plt.show() # this must follow the animation call for you to actually see the plot







