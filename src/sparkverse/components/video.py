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
    def setFormat(input):
        """
        set the format of the reccordings
        Parameters:
        input (int):
        input=0 :  format will be .mp4
        input=1 :  format will be .avi
        """
        if input==0:
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    