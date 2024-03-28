import frrpc
import time
from gripper import *

robot = frrpc.RPC('192.168.58.2')


# J1=[95.442,-101.149,-98.699,-68.347,90.580,-47.174]
# P1=[75.414,568.526,338.135,-178.348,-0.930,52.611]
# eP1=[0.000,0.000,0.000,0.000]

# dP1=[300.000,-650.000,-600.000,0.000,0.000,0.000]
# robot.MoveL(J1,P1,0,0,20.0,80.0,100.0,-1.0,eP1,0,1 ,dP1)
# robot.WaitMs(100)

open_gripper(robot)

# robot.StartJOG(0,1,0,100.0,100.0,90.0)
# time.sleep(1)
