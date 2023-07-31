import numpy as np
import cv2
from glob import glob

def calibrate_camera(img_path ,chessboard_size=(9,6)):

    obj_points = []
    img_points = []
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    objp = np.zeros((chessboard_size[0] * chessboard_size[1], 3), np.float32)
    objp[:,:2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)

    images = glob(img_path + '/*.png')

    for image in images:
        img = cv2.imread(image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, corners = cv2.findChessboardCorners(gray, chessboard_size,
cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK +
cv2.CALIB_CB_NORMALIZE_IMAGE)
        if ret:
            obj_points.append(objp)
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            img_points.append(corners2)

            img = cv2.drawChessboardCorners(img, chessboard_size, corners2, ret)

        cv2.imshow('img', img)
        cv2.waitKey(500)

    cv2.destroyAllWindows()

    #카메라 캘리브레이션을 진행
    ret, camera_matrix, distortion_coefficients, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)

    return ret, camera_matrix, distortion_coefficients, rvecs, tvecs

if __name__ == "__main__":
    #체커보드 이미지가 저장된 폴더
    img_path = './calib_img'
    ret, camera_matrix, distortion_coefficients, rvecs, tvecs = calibrate_camera(img_path)

    if ret:
        print("Camera Matrix : \n", camera_matrix)
        print("\nDistortion Coefficients : \n", distortion_coefficients)

        #카메라 캘리브레이션 .npz저장 위치설정
        np.savez("../params/camera_calibration.npz", camera_matrix=camera_matrix,
distortion_coefficients=distortion_coefficients, rvecs=rvecs, tvecs=tvecs)