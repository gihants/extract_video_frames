# extract_video_frames
This is a simple opencv-python script to extract images from video frames:

##Requirements:
- python 3+
- opencv3+

##usage
- clone the repository: 
    ```sh
    $ git clone https://github.com/gihants/extract_video_frames.git
    ```
- run the python script with the required arguments:
-- argument "-i", "--input": path to input video file (required)
-- argument "-o", "--output": name of the output folder (required)
-- argument "-s", "--skip": number of initial frames to skip (optional)
-- argument "-f", "--frames": number of frames to extract (optional)

    example #1: 
    ```sh
     $ python extract_video_frames.py -i VID_20200826_110451.mp4 -o extracted_directory 
    ```
    example #2: 
    ```sh
     $ python extract_video_frames.py -i VID_20200826_110451.mp4 -o extracted_directory -s 10 -f 100
    ```


