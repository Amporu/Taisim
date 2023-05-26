"""
info:This module contains a collection of non categorizable functions
autor: Tucudean Adrian-Ionut
date: 22.05.2023
email: Tucudean.Adrian.Ionut@outlook.com
license: MIT
"""
import cv2

#pylint: disable=E1101
class Video:
    """class for reccording data"""
    start_time = 0
    end_time=0
    delta_time=0
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_file = 'output_video.mp4'  # Specify the output file name
    fps = 30.0  # Specify the frames per second (FPS)
    #frame_size = (640, 480)  # Specify the frame size (width, height)
    video_writer = None#cv2.VideoWriter(output_file, fourcc, fps, frame_size)
    recorded=0
    reccording_flag=0
    @staticmethod
    def set_format(format_input):
        """
        set the format of the reccordings
        Parameters:
        input (int):
        format_input=0 :  format will be .mp4
        format_input=1 :  format will be .avi
        """
        if format_input==0:
            Video.fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    @staticmethod
    def set_output_name(output):
        """
        set the format of the reccordings
        Parameters:
        input (int):
        output : file output name
        """
        Video.output_file=output
