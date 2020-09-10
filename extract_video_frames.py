import argparse
import cv2
import os
    
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, type=str, help="path to input video file")
ap.add_argument("-o", "--output", required=True, type=str, help="output directory name")
ap.add_argument("-skip", "--skip", default = 0, type=int, help="number of initial frames to skip")
ap.add_argument("-frames", "--frames", default = -1, type=int, help="number of frames to skip")
args = vars(ap.parse_args())

video_file = args["input"]
output_folder = "./" + args["output"]
skip = args["skip"]
frames = args["frames"]


if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
vidcap = cv2.VideoCapture(video_file)
success,image = vidcap.read()
count = 0
skipping = 0
while success:
    if (frames >= 0) and (count > frames + skip):
        break
    if skipping >= skip:
        if count < 10:
            cv2.imwrite(output_folder + "/frame000%d.jpg" % count, image)     # save frame as JPEG file       
        elif count < 100:
            cv2.imwrite(output_folder + "/frame00%d.jpg" % count, image)     # save frame as JPEG file
        elif count < 1000:
            cv2.imwrite(output_folder + "/frame0%d.jpg" % count, image)     # save frame as JPEG file
        else:
            cv2.imwrite(output_folder + "/frame%d.jpg" % count, image)     # save frame as JPEG file
        
    success,image = vidcap.read()
    print('Extracted frame {}'.format(str(count)))
    count += 1
    skipping +=1