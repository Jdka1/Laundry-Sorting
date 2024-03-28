import time
from gripper import open_gripper, close_gripper

class Robot:
    def __init__(self, robot, speed=50.0):
        self.speed = speed
        self.robot = robot

        self.J1=[95.442,-101.149,-98.699,-68.347,90.580,-47.174]
        self.P1=[75.414,568.526,338.135,-178.348,-0.930,52.611]
        self.eP1=[0.000,0.000,0.000,0.000]

    def grab_clothes(self, depth):
        open_gripper(self.robot)
        dP1=[300.000,-650.000,depth,0.000,0.000,0.000]
        self.robot.MoveL(self.J1,self.P1,0,0,self.speed,180.0,100.0,-1.0,self.eP1,0,1 ,dP1)
        close_gripper(self.robot)
        time.sleep(0.3)
        self.robot.WaitMs(100)

    def hold_to_camera(self):
        dP1=[300.000,-600.000,200.000,0.000,0.000,0.000]
        self.robot.MoveL(self.J1,self.P1,0,0,self.speed,50.0,100.0,-1.0,self.eP1,0,1 ,dP1)
        self.robot.WaitMs(100)

    def move_to_light_pile(self):
        self.robot.StartJOG(0,1,0,100.0,100.0,100.0)
        time.sleep(2.5)
        self.robot.StartJOG(2,2,0,100.0,100.0,350.0)
        time.sleep(1.5)
        open_gripper(self.robot)
        time.sleep(0.5)
        self.robot.StartJOG(2,2,1,100.0,100.0,350.0)
        time.sleep(2)
        self.robot.StartJOG(0,1,1,100.0,100.0,100.0)
        time.sleep(2.3)

    def move_to_dark_pile(self):
        self.robot.StartJOG(0,1,0,100.0,100.0,180.0)
        time.sleep(4)
        self.robot.StartJOG(2,1,0,100.0,100.0,250.0)
        time.sleep(1.5)
        open_gripper(self.robot)
        time.sleep(0.5)
        self.robot.StartJOG(2,1,1,100.0,100.0,250.0)
        time.sleep(2)
        self.robot.StartJOG(0,1,1,100.0,100.0,180.0)
        time.sleep(4)