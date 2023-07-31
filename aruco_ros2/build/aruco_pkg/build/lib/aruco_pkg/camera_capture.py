import cv2
import os

def main():
    #webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("cannot open webcam")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    #캠쳐 파일 저장 위치 설정
    save_path = './calib_img/'
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    
    img_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Image", frame)

        #c를 누르면 캠쳐
        if cv2.waitKey(1) & 0xFF == ord('c'):
            img_count += 1
            img_name = os.path.join(save_path, f"captured_image{img_count}.png")
            cv2.imwrite(img_name, frame)
            print(f"{img_name}image is saved!")

        #q를 누르면 꺼지게
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()