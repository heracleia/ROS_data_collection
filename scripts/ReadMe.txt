Script Description

depthListener.py
    - Subscriber node to listen to depth data from both the cameras
    - Will synchornize the data using message filter and record in rosbag

imageListener.py
    - Subscriber node to record raw image data(rgb data) from both the cameras
    - Will synchornize the data using message filter and record in rosbag

museStreamer.py
    - Will resolve the muse bluetooth stream and publish it on the EEG topic.

museListener.py
    - Will subscribe to the muse stream topic and record data to a rosbag

raw_nuro_conv.py
    - Muse streamer will record raw muse data.
    - raw_nuro_conv.py will convert raw data to alpha,beta... values
    - Currently only works for 1 electrode

utils.py
    - Helper functions for raw_nuro_conv.py
======================================================================================================================================================
1. Before running make sure the above mentioned scripts are added to cMake of the project
2. Added the EEG message type to cMake

======================================================================================================================================================
1. Launch camera publisher nodes by the following command
 'roslaunch realsense2_camera rs_camera.launch camera:=camera_type serial_no:= CameraSerialNumber filters:=pointcloud'

 - Replace the CameraSerialNumber with the serial number of camera (can be found in the camera_serials.txt file)
 - If connecting new camera whos serial number is not in the file connect the camera using above command without the 'camera' and 'serial_no'
    it will display the camera serial number once connected.
 - camera_type should be either 'front_cam' or 'side_cam'.
 - Dont change change camera type as it will cause issues with topic name.


2. Record data from camera
 'rosrun project_name depthListener.py'
 'rosrun project_name imageListener.py'

 - depthListener will record data from both cameras using pointcloud filter.
 - imageListener will record rgb image data from both cameras.


3. Recording data from MUSE

    Step1: Make sure you have muselsl installed on your system
    Step2: Use comman 'muselsl stream --address YOUR_DEVICE_ADDRESS'
    Step3: If roscore is running move to Step4 else use command 'roscore'
    Step4: In a new terminal execute 'rosrun project_name museStreamer.py'
    Step5: In a new terminal execute 'rosrun project_name museListener.py'

4. To convert raw muse data to alpha beta values run raw_nuro_conv.py script (check rosbag name and path in code).
