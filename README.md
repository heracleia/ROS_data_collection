# ROS_data_collection

## Connecting MUSE S to your machine

1. Install `muselsl` using pip
  `pip3 install muselsl`

2. Download and install the Liblsl binary from here: https://github.com/sccn/liblsl/releases
- Download the \*.deb bionic version

3. To list the MUSE device:
- `muselsl list`

4. Figure out the MAC Address of the MUSE using `bluetoothctl`

5. Once you get the MAC address, from bluetoothctl REPL, trust the device
- `trust <MAC_ADDRESS>`

6. Exit bluetoothctl, restart MUSE and run the following command to stream from MUSE
- `muselsl stream --address <MAC_ADDRESS>`



### NOTE: For this error "TypeError: unsupported operand type(s) for +: 'BleakGATTCharacteristicBlueZDBus' and 'int' ", follow the changes in the commit provided here: https://github.com/alexandrebarachant/muse-lsl/pull/187/commits/c9f805782f3b91c1a954ad4087211e9a33563e4c 
