#!/usr/bin/env python
from __future__ import print_function

import rospy
import message_filters
from sensor_msgs.msg import PointCloud2
import rosbag


SCAMD = "/side_cam/depth/color/points"
FCAMD = "/front_cam/depth/color/points"




def callback(scamData,fcamData):
    
    bag.write('sideCamDepth', scamData)
    bag.write('frontCamDepth', fcamData)

def subscriber():
    global bag
    rospy.init_node("depth_subscriber",anonymous=True)
    

    sideCam = message_filters.Subscriber(SCAMD,PointCloud2)
    frontCam = message_filters.Subscriber(FCAMD,PointCloud2)

    synchronizer = message_filters.ApproximateTimeSynchronizer([sideCam,frontCam],30,1,allow_headerless=False)

    synchronizer.registerCallback(callback)

    # Keeps python running until node is stopped
    rospy.spin()
    bag.close()
if __name__ == '__main__':
    while not rospy.is_shutdown():
        bag = rosbag.Bag("TestBagDepth.bag",'w')

        subscriber()

    bag.close()