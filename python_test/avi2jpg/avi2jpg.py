import cv2
import sys

class avi2jpg:
    vid = None
    
    def convert(self, video):
        vidcap = cv2.VideoCapture(video)
        success,image = vidcap.read()
        count = 0
        while success:
            framecount = "./frames/{number:06}".format(number=count)
            cv2.imwrite(framecount+".jpg", image)     # save frame as JPEG file      
            success,image = vidcap.read()
            print('Read a new frame: ', success)
            count += 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        "Please give a video as an argument to this program"
    elif(sys.argv[1][-4:]!=".avi"):
        "Please give an .avi video as an argument to this program"
    else:
        converter = avi2jpg()
        converter.convert(sys.argv[1])
