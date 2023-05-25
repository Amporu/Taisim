"""
info:This module contains the help-bar related functions
autor: Tucudean Adrian-Ionut
date: 17.05.2023
email: Tucudean.Adrian.Ionut@outlook.com
license: MIT
"""
# pylint: disable=too-few-public-methods
import cv2
#pylint: disable=E1101
#pylint: disable=too-many-boolean-expressions
#pylint: disable=too-many-arguments
from ..components.video import Video
class HelpBar():
    """class for controlling HelpBar menu"""
    keys=["Q","H","R","W","A","S","D","T"]
    description=["Quit","Hide/Show",
                 "Reccord",
                 "Move Forward",
                 "Rotate Left",
                 "Move Backward",
                 "Rotate Right",
                 "Enable Trail"]
    font = cv2.FONT_HERSHEY_SIMPLEX
    show = 1
    last_key=-1
    trail_flag=0
    Trail=[]
    @staticmethod
    def enable_trail(player_car,mask):
        """function to enable trail feature"""
        if len(HelpBar.Trail)>=100:
            HelpBar.Trail.pop(0)
        else:
            if (len(HelpBar.Trail)>0 and(HelpBar.Trail[-1][0]!=int(player_car.x_value) or
                (HelpBar.Trail[-1][0]<player_car.x_value+1 and
                HelpBar.Trail[-1][0]>player_car.x_value-1)) and
                (HelpBar.Trail[-1][1]!=int(player_car.y_value) or
                (HelpBar.Trail[-1][0]<player_car.y_value+1 and
                HelpBar.Trail[-1][0]>player_car.y_value-1))):
                HelpBar.Trail.append((int(player_car.x_value),int(player_car.y_value)))
            if len(HelpBar.Trail)==0:
                HelpBar.Trail.append((int(player_car.x_value),int(player_car.y_value)))
        for i in range(0,len(HelpBar.Trail),1):
            cv2.circle(img=mask,center=HelpBar.Trail[i],radius=3,color=(0,255,0),thickness=1)
    @staticmethod
    def showpannel(frame,image,x_pos,y_pos,rotation,accel):
        """
        Help Bar GUI
        Parameters:
        frame (Mat): simulator frame
        image (Mat): blank HelpBar frame
        """

        cv2.putText(img=image,
                    text="HelpBar",
                    org=(12, 20),
                    fontFace=HelpBar.font,
                    fontScale=0.8,
                    color=(9,0,0),
                    thickness=2)
        for i in range(len(HelpBar.keys)):# pylint: disable=C0200
            if HelpBar.last_key==i:
                if i!=2:
                    cv2.rectangle(img=image,
                                  pt1=(10,30+i*40),
                                  pt2=(40,60+i*40),
                                  color=(0,255,0),
                                  thickness=3)
                    cv2.putText(img=image,
                                text=HelpBar.keys[i],
                                org=(20,50+i*40),
                                fontFace=HelpBar.font,
                                fontScale=0.5,
                                color=(0,255,0),
                                thickness=2)
                    cv2.putText(img=image,
                                text=HelpBar.description[i],
                                org=(50,50+i*40),
                                fontFace=HelpBar.font,
                                fontScale=0.5,
                                color=(0,255,0),
                                thickness=2)
            else:
                if i!=2 or Video.recorded!=-1 or Video.recorded==0:
                    cv2.rectangle(img=image,
                                  pt1=(10,30+i*40),
                                  pt2=(40,60+i*40),
                                  color=(255,0,0),
                                  thickness=3)
                    cv2.putText(img=image,
                                text=HelpBar.keys[i],
                                org=(20,50+i*40),
                                fontFace=HelpBar.font,
                                fontScale=0.5,
                                color=(0,0,255),
                                thickness=2)
                    cv2.putText(img=image,
                                text=HelpBar.description[i],
                                org=(50,50+i*40),
                                fontFace=HelpBar.font,
                                fontScale=0.5,
                                color=(0,0,255),
                                thickness=2)
            if HelpBar.trail_flag==1 and i==7:
                cv2.rectangle(img=image,
                              pt1=(40,60+i*40),
                              pt2=(230,30+i*40),
                              color=(0,0,0),
                              thickness=-1)
                cv2.putText(img=image,
                            text=HelpBar.description[i],
                            org=(50,50+i*40),
                            fontFace=HelpBar.font,
                            fontScale=0.5,
                            color=(0,255,0),
                            thickness=2)
            if Video.recorded==-1:
                minutes = int(Video.delta_time // 60)
                seconds = int(Video.delta_time % 60)
                cv2.putText(img=image,
                            text=str(minutes)+"' "+str(seconds)+"''",
                            org=(50,50+80),
                            fontFace=HelpBar.font,
                            fontScale=0.5,
                            color=(0,0,255),
                            thickness=2)
                cv2.circle(img=image,
                           center=(25,125),
                           radius=10,
                           color=(0,0,255),
                           thickness=-1)
                cv2.rectangle(img=image,
                              pt1=(10,30+80),
                              pt2=(40,60+80),
                              color=(0,0,255),
                              thickness=3)
        cv2.putText(img=image,
                    text="Car PROPERTIES",
                    org=(10,380),
                    fontFace=HelpBar.font,
                    fontScale=1,
                    color=(0,0,0),
                    thickness=2)
        cv2.rectangle(img=image,
                      pt1=(10,400),
                      pt2=(310,700),
                      color=(255,0,255),
                      thickness=2)
        cv2.putText(img=image,
                    text="Position",
                    org=(30,430),
                    fontFace=HelpBar.font,
                    fontScale=0.5,
                    color=(255,0,0),
                    thickness=2)
        cv2.putText(img=image,
                    text="X = "+str(x_pos),
                    org=(30,450),
                    fontFace=HelpBar.font,
                    fontScale=0.5,
                    color=(0,0,0),
                    thickness=2)
        cv2.putText(img=image,
                    text="Y = "+str(y_pos),
                    org=(130,450),
                    fontFace=HelpBar.font,
                    fontScale=0.5,
                    color=(0,0,0),
                    thickness=2)
        cv2.putText(img=image,
                    text="Angular Movement",
                    org=(30,470),
                    fontFace=HelpBar.font,
                    fontScale=0.5,
                    color=(255,0,0),
                    thickness=2)
        cv2.putText(img=image,
                    text="angle = "+str(rotation),
                    org=(30,490),
                    fontFace=HelpBar.font,
                    fontScale=0.5,
                    color=(0,0,0),
                    thickness=2)
        cv2.putText(img=image,
                    text="Linear Movement",
                    org=(30,510),
                    fontFace=HelpBar.font,
                    fontScale=0.5,
                    color=(255,0,0),
                    thickness=2)
        cv2.putText(img=image,
                    text="speed = "+str(round(accel,2)),
                    org=(30,530),
                    fontFace=HelpBar.font,
                    fontScale=0.5,
                    color=(0,0,0),
                    thickness=2)#pylint: disable=E1101
        frame=cv2.hconcat([frame,image])#pylint: disable=E1101
        return frame
        