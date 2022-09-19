import glob
import os
from multiprocessing import Pool, cpu_count
from typing import Dict

import click
import cv2


def extract_frames_single_video(
    video_file: str, output_folder: str, skip: int, skip_beg: int, frames: int
):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    vidcap = cv2.VideoCapture(video_file)
    success, image = vidcap.read()
    count = 0
    skipping_beginnng = 0
    frame_instance = 0
    while success:
        if (frames >= 0) and (count > frames + skip):
            break
        if skipping_beginnng < skip_beg:
            break
        if frame_instance == skip:
            frame_instance = 0
            video_file_name = os.path.splitext(os.path.basename(video_file))[0]
            file_name = f"{output_folder}/{video_file_name}_frame{count:05d}.jpg"
            # file_name = f"{output_folder}/test.jpg"
            cv2.imwrite(file_name, image)
        else:
            frame_instance += 1

        success, image = vidcap.read()
        print("Extracted frame {}".format(str(count)))
        count += 1
        skipping_beginnng += 1


def extract_frames_single_video_worker(extract_params: Dict):
    video_file = extract_params["video_file"]
    output_folder = extract_params["output_folder"]
    skip = extract_params["skip"]
    skip_beg = extract_params["skip_beg"]
    frames = extract_params["frames"]

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    vidcap = cv2.VideoCapture(video_file)
    success, image = vidcap.read()
    count = 0
    skipping_beginnng = 0
    frame_instance = 0
    while success:
        if (frames >= 0) and (count > frames + skip):
            break
        if skipping_beginnng < skip_beg:
            break
        if frame_instance == skip:
            frame_instance = 0
            video_file_name = os.path.splitext(os.path.basename(video_file))[0]
            file_name = f"{output_folder}/{video_file_name}_frame{count:05d}.jpg"
            # file_name = f"{output_folder}/test.jpg"
            cv2.imwrite(file_name, image)
        else:
            frame_instance += 1

        success, image = vidcap.read()
        print("Extracted frame {}".format(str(count)))
        count += 1
        skipping_beginnng += 1


@click.group()
def cli():
    pass


@cli.command(name="extract_single_video")
@click.option(
    "--video_file", type=str, help="Path of the video file to extract frames from"
)
@click.option(
    "--output_folder",
    type=str,
    help="Path of the output directory to extract frames into",
)
@click.option(
    "--skip",
    type=int,
    default=10,
    help="Number of frames to skip / frames per sampling point",
)
@click.option(
    "--skip_beg",
    type=int,
    default=-1,
    help="Number of frames to skip at the begining of the video",
)
@click.option(
    "--frames",
    type=int,
    default=-1,
    help="Total number of frames to extract from the video",
)
def extract_single_video(
    video_file: str, output_folder: str, skip: int, skip_beg: int, frames: int
):
    extract_frames_single_video(video_file, output_folder, skip, skip_beg, frames)


@cli.command(name="extract_video_directory")
@click.option(
    "--video_directory",
    type=str,
    help="Path of the directory containing video files to extract frames from",
)
@click.option(
    "--output_folder",
    type=str,
    help="Path of the output directory to extract frames into",
)
@click.option(
    "--skip",
    type=int,
    default=10,
    help="Number of frames to skip / frames per sampling point",
)
@click.option(
    "--skip_beg",
    type=int,
    default=-1,
    help="Number of frames to skip at the begining of the video",
)
@click.option(
    "--frames",
    type=int,
    default=-1,
    help="Total number of frames to extract from the video",
)
def extract_video_directory(
    video_directory: str, output_folder: str, skip: int, skip_beg: int, frames: int
):
    video_files = glob.glob(f"{video_directory}/*.mp4")
    extract_params = [
        {
            "video_file": video_file,
            "output_folder": output_folder,
            "skip": skip,
            "skip_beg": skip_beg,
            "frames": frames,
        }
        for video_file in video_files
    ]
    pool = Pool(cpu_count() - 1)
    pool.map(extract_frames_single_video_worker, extract_params)


@cli.command(name="wel")
def welcome():
    click.echo("Welcome")


if __name__ == "__main__":
    cli()
