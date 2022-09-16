#!/usr/bin/env python
import rospy
from va_project.msg import EEGMsg 
import rosbag


def callback(data):
    bag.write('EEG/Raw',data)


def listener():
    global bag


    rospy.init_node('eeg_listener', anonymous=True)
    rospy.Subscriber("eeg_publisher", EEGMsg, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    while not rospy.is_shutdown():
        bag = rosbag.Bag('EEG_Raw.bag','w')
        listener()
    
    bag.close()