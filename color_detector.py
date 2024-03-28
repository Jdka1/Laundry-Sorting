import cv2
from robot_actions import Robot
import frrpc
import time


def f(x):
    total = 0
    for n in range(1, x+1):
        total += 1/n
    return -float(750 + 30*(1+total))

def check_color(thresh):
    num_white_pixels = cv2.countNonZero(thresh)
    num_black_pixels = thresh.size - num_white_pixels

    if num_black_pixels > num_white_pixels:
        print('dark clothes')
        return 'dark'
    else:
        print('light clothes')
        return 'light'


robot = frrpc.RPC('192.168.58.2')

arm = Robot(robot=robot)


for i in range(50,70):
    depth = f(i)
    print(i)
    print(depth)
    arm.grab_clothes(depth=depth)
    arm.hold_to_camera()

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    height, width, _ = frame.shape
    margin = (150, 250) # y, x
    cropped = frame[margin[0]:height-margin[0], margin[1]:width-margin[1]]
    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 105, 255, cv2.THRESH_BINARY)

    if check_color(thresh) == 'light':
        arm.move_to_light_pile()
    else:
        arm.move_to_dark_pile()

    cap.release()
    time.sleep(1)


# cv2.destroyAllWindows()

