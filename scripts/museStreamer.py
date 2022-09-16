#!/usr/bin/env python
from pylsl import StreamInlet, resolve_stream
import rospy
from va_project.msg import EEGMsg 
 
def talker():
    # first resolve an EEG stream on the lab network
    print("looking for an EEG stream...")
    streams = resolve_stream('type', 'EEG')

    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])

    
    pub = rospy.Publisher('eeg_publisher', EEGMsg,queue_size=256)
    rospy.init_node('museStreamer', anonymous=True)
    r = rospy.Rate(256) #10hz
    
    while not rospy.is_shutdown():
        sample,timestamp = inlet.pull_sample()
        msg = EEGMsg()
        msg.alpha = sample[2]
        msg.beta = sample[3]
        msg.theta = sample[1]
        msg.delta = sample[0]
        msg.timeStamp = timestamp
        
        # rospy.loginfo(msg)
        pub.publish(msg)
        

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:pass