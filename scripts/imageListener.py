#!/usr/bin/env python
from __future__ import print_function


import rospy
import rosbag
from datetime import date
from datetime import datetime
import message_filters

from sensor_msgs.msg import Image



SCAM = "/side_cam/color/image_raw"
FCAM = "/front_cam/color/image_raw"



def callback(scamData,fcamData):
    bag.write('sideCam', scamData)
    bag.write('frontCam', fcamData)

def subscriber():
    global bag

    rospy.init_node("image_subscriber",anonymous=True)
    

    sideCam = message_filters.Subscriber(SCAM,Image)
    frontCam = message_filters.Subscriber(FCAM,Image)

    synchronizer = message_filters.ApproximateTimeSynchronizer([sideCam,frontCam],30,1,allow_headerless=False)


    synchronizer.registerCallback(callback)


    # Keeps python running until node is stopped
    rospy.spin()
    
if __name__ == '__main__':
    while  not rospy.is_shutdown():
        bag = rosbag.Bag('TestImg.bag','w')
        
        subscriber()

    bag.close()