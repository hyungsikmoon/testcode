# 필요한 패키지 import
import imutils # 파이썬 OpenCV가 제공하는 기능 중 복잡하고 사용성이 떨어지는 부분을 보완(이미지 또는 비디오 스트림 파일 처리 등)
import cv2 # opencv 모듈

# 비디오 파일
video = "/home/hs.moon/work/Realtime-object-detection/the_hyundai_1.mp4" # "" 일 경우 webcam 사용

# 저장할 비디오 파일 경로 및 이름
result_path = "the_hyundai_1.mp4_512.avi"

resize_h = 512
resize_w = 512

# 비디오 경로가 제공되지 않은 경우 webcam 사용
if video == "":
    print("[webcam 시작]")
    vs = cv2.VideoCapture(0)

# 비디오 경로가 제공된 경우 video 사용
else:
    print("[video 시작]")
    vs = cv2.VideoCapture(video)

# 비디오 저장 변수
writer = None

# 비디오 스트림 프레임 반복
while True:
    # 프레임 읽기
    ret, frame = vs.read()

    # 읽은 프레임이 없는 경우 종료
    if frame is None:
        break

    # 프레임 resize
    frame = imutils.resize(frame, width=resize_w, height=resize_h)

    pad_w = int((resize_w - frame.shape[1]) / 2.0)
    pad_h = int((resize_h - frame.shape[0]) / 2.0)

    frame = cv2.copyMakeBorder(frame, pad_h, pad_h, pad_w, pad_w, cv2.BORDER_CONSTANT,value=[0,0,0])
    frame = cv2.resize(frame, (resize_w,resize_h))

    # 프레임 출력
    cv2.imshow("frame", frame)
    
    # 'q' 키를 입력하면 종료
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
                                    
    # 저장할 비디오 설정
    if writer is None:
        fourcc = cv2.VideoWriter_fourcc(*"MJPG")
        writer = cv2.VideoWriter(result_path, fourcc, 25, (frame.shape[1], frame.shape[0]), True)

    # 비디오 저장
    if writer is not None:
        writer.write(frame)

# 종료
vs.release()
cv2.destroyAllWindows()
