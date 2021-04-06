from PIL import ImageGrab
import numpy as np
import cv2
import time
import keys as k

keys = k.Keys()

def pathing(minimap):
    lower = np.array([100, 130, 100])
    upper = np.array([150, 255, 255])

    hsv = cv2.cvtColor(minimap, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower, upper)

    matches = np.argwhere(mask==255) # array of matches pixels that are white on the mini map
    
    mean_y = np.mean(matches[:,1]) # indexes of the Y values that match the white pixels
    target = minimap.shape[1] / 2 # the center of the screen

    error = target - mean_y # the difference between the white values and the target value
    print(error)

    keys.directMouse(-1 * int(error * 1.7), 0)

    cv2.imshow("cv2screen", mask)
    cv2.waitKey(5)

for i in range(5): # just some time until things start running
    print(i)
    time.sleep(1)

keys.directKey("w")

for i in range(40000):
    img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    img_np = np.array(img)
    screen = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

    # we wanna grab the region of the minimap on the screen
    minimap = screen[650:900, 60:310]
    miniminimap = screen[690:780, 140:230]

    pathing(miniminimap)

    if(i % 10 == 0):
        keys.directKey("LSHIFT")

    if(i % 12 == 0):
        keys.directKey("LSHIFT", keys.key_release)

    # screen = cv2.resize(screen, (960, 540))
    # cv2.imshow("cv2screen", miniminimap)
    # cv2.waitKey(5)
keys.directKey("w", keys.key_release)
cv2.destroyAllWindows()