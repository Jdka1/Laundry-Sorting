def close_gripper(robot):
    robot.SetAO(0,1500.0,1)
    robot.SetAO(1,0.0,1)

def open_gripper(robot):
    robot.SetAO(0,0.0,1)
    robot.SetAO(1,1500.0,1)

