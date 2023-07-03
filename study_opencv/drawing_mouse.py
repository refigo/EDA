import cv2
import numpy as np

oldx = -1
oldy = -1

def on_mouse(event, x, y, flags, param):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('Event L Button: %d, %d' % (x, y))
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags == cv2.EVENT_FLAG_LBUTTON:
            print('Event L Button Move: %d, %d' % (x, y))
            cv2.line(img, (oldx, oldy), (x, y), (255,0,0), 4, cv2.LINE_AA)
            oldx, oldy = x, y
            cv2.imshow('image', img)

img = np.ones((480, 640, 3), dtype=np.uint8) * 255 # set all white image

cv2.namedWindow('image')
cv2.setMouseCallback('image', on_mouse, img)

cv2.imshow('image', img)
cv2.waitKey()

cv2.destroyAllWindows()
