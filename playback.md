# MCAP Playback Service

## Overview
The Replay Service enables you to replay saved MCAP files, allowing your Raivin to simulate previously recorded messages. When replayed, these messages are interpreted as if they were being received for the first time, providing full visualization capabilities in the WebUI.

### How It Works
The Replay Service:
- Stops the current input services (Camera, Model, NavSat, IMU, Radar Publisher, Fusion)
- Publishes the Zenoh topics in the MCAP recording to simulate the input services, including timings between topic messaging
- Loops recordings automatically
- Uses the current WebUI visualization to display the Replay-published Zenoh topics.

### Benefits
The Replay Service offers several advantages:
- Creates consistent test/debug environments
- Provides full control over input messages
- Enables solution verification with consistent data
- Allows continuous looping of recordings
- Isolates replay data from live inputs

### Limitations
There are important considerations when using the Replay Service:
- Services stopped by the Replay Service must be manually restarted or the device rebooted.
- Multiple Replay Services can run simultaneously but will interfere with each other.  Stop a previous replay before starting a new one.
- All input services are stopped by the Replay Service, regardless of MCAP recording content.  For example, the Camera Service is turned off even if MCAP recording contains no camera data

## Using the Replay Service
The Replay Service can be started using any MCAP recording currently on the Maivin.  We first need to get the name of the MCAP recording we wish to replay and then run the Replay Service with the MCAP recording filename.

### Finding Available Recordings
You can locate available recordings through both the HTTPS GUI and SSH CLI.

- On the GUI:
   1. Go to the MCAP recording page: `https://<hostname>/mcap`.
   2. Confirm the recording `Directory` is `/media/DATA`
   3. Note the recording file name you wish to replay.
      ![MCAP Recorder MCAP list](static/mcap_recorder.png){align=center}
- On the Maivin SSH CLI:
   1. Confirm the current recorder directory location by searching for "STORAGE" option in recording configuration file at `/etc/default/recorder`
      ```bash
      torizon@verdin-imx8mp-15141027:~$ grep STORAGE /etc/default/recorder
      STORAGE = "/media/DATA"
      ```
   2. Get a listing of the recorder directory.
      ```bash
      torizon@verdin-imx8mp-15141027:~$ ls -1 /media/DATA
      verdin-imx8mp-15141027_2024_12_11_22_50_09.mcap
      verdin-imx8mp-15141027_2024_12_11_22_52_21.mcap
      verdin-imx8mp-15141027_2024_12_11_22_54_33.mcap
      verdin-imx8mp-15141027_2024_12_16_21_09_38.mcap
      ```
   3. Note the recording file name you wish to replay.
```{warning}
If the recording directory is not `/media/DATA` or the MCAP recording is otherwise not in the `/media/DATA` directory, the Replay Service will not work.  It is required to copy the MCAP file into the `/media/DATA` directory prior to following the instructions in the next section.
```

### Starting Playback
After getting the filename from the current storage location, the replay the MCAP recording with the following instructions.  Of specific note, do NOT inlcude the .mcap extension when you enter the MCAP recording filename.  From the output above, let's use the `verdin-imx8mp-15141027_2024_12_16_21_09_38.mcap` MCAP recording from the above example.
1. Access your Raivin through SSH
2. Use the following command to start playback:
   ```bash
   sudo systemctl start replay@verdin-imx8mp-15141027_2024_12_16_21_09_38
   ```
3. Confirm the Replay service is running:
   ```bash
   torizon@verdin-imx8mp-15141027:~$ systemctl status replay@verdin-imx8mp-15141027_2024_12_16_21_09_38
   ● replay@verdin-imx8mp-15141027_2024_12_16_21_09_38.service - Maivin MCAP Replayer Service
   Loaded: loaded (/usr/lib/systemd/system/replay@.service; disabled; vendor preset: disabled)
   Active: active (running) since Wed 2024-12-18 20:50:14 UTC; 12s ago
   Main PID: 7079 (replay)
      Tasks: 21 (limit: 3772)
   Memory: 27.7M
   CGroup: /system.slice/system-replay.slice/replay@verdin-imx8mp-15141027_2024_12_16_21_09_38.service
            └─ 7079 /usr/bin/replay verdin-imx8mp-15141027_2024_12_16_21_09_38.mcap

   Dec 18 20:50:14 verdin-imx8mp-15141027 replay[7079]: [2024-12-18T20:50:14Z INFO  maivin_replay::services] Stopped service imu
   Dec 18 20:50:14 verdin-imx8mp-15141027 replay[7079]: [2024-12-18T20:50:14Z INFO  maivin_replay::services] Stopped service navsat
   Dec 18 20:50:14 verdin-imx8mp-15141027 replay[7079]: [2024-12-18T20:50:14Z INFO  maivin_replay::services] Stopped service model
   Dec 18 20:50:14 verdin-imx8mp-15141027 replay[7079]: [2024-12-18T20:50:14Z INFO  maivin_replay::services] Stopped service camera
   Dec 18 20:50:14 verdin-imx8mp-15141027 replay[7079]: [2024-12-18T20:50:14Z INFO  maivin_replay] Opened Zenoh session
   Dec 18 20:50:14 verdin-imx8mp-15141027 replay[7079]: ERROR: ACCESS UNIT BOUNDARY CHECK
   Dec 18 20:50:14 verdin-imx8mp-15141027 replay[7079]: ERROR: ACCESS UNIT BOUNDARY CHECK
   Dec 18 20:50:14 verdin-imx8mp-15141027 replay[7079]: ERROR: ACCESS UNIT BOUNDARY CHECK
   Dec 18 20:50:14 verdin-imx8mp-15141027 replay[7079]: ERROR: ACCESS UNIT BOUNDARY CHECK
   Dec 18 20:50:14 verdin-imx8mp-15141027 replay[7079]: [2024-12-18T20:50:14Z INFO  maivin_replay::video_decode] Video dimensions are: 1920x1080
   ```
   ```{note}
   The `ACCESS UNIT BOUNDARY CHECK` errors in the above output are noting that the beginning of the h.264 video stream does not have a key frame.  This messages are expected and will not impact the performance of the Replay Service.
   ```
When the Replay Service is running, the outputs on the "Segmentation View" and "Occupancy Grid" pages will now be generated from the MCAP recording file instead of the Maivin hardware.

### Stopping Playback
To stop the Replay Service:
1. Access your Raivin through SSH
2. Use the following command to stop playback.  You must include the file name used to start the Replay service.
   ```bash
   sudo systemctl stop replay@verdin-imx8mp-15141027_2024_12_16_21_09_38
   ```
   ```{tip}
   If you forget the name of the MCAP recording used to invoke the Replay service, you can find the information with the CLI using either `systemctl status | grep replay` or `ps aux | grep replay` commnds.
   ```
3. Confirm the service is stopped:
   ```bash
   torizon@verdin-imx8mp-15141027:~$ systemctl status replay@verdin-imx8mp-15141027_2024_12_16_21_09_38
   ○ replay@verdin-imx8mp-15141027_2024_12_16_21_09_38.service - Maivin MCAP Replayer Service
     Loaded: loaded (/usr/lib/systemd/system/replay@.service; disabled; vendor preset: disabled)
     Active: inactive (dead)

   Dec 18 21:18:50 verdin-imx8mp-15141027 replay[7474]: [2024-12-18T21:18:50Z INFO  maivin_replay::services] Stopped service camera
   Dec 18 21:18:50 verdin-imx8mp-15141027 replay[7474]: [2024-12-18T21:18:50Z INFO  maivin_replay] Opened Zenoh session
   Dec 18 21:18:50 verdin-imx8mp-15141027 replay[7474]: ERROR: ACCESS UNIT BOUNDARY CHECK
   Dec 18 21:18:50 verdin-imx8mp-15141027 replay[7474]: ERROR: ACCESS UNIT BOUNDARY CHECK
   Dec 18 21:18:50 verdin-imx8mp-15141027 replay[7474]: ERROR: ACCESS UNIT BOUNDARY CHECK
   Dec 18 21:18:50 verdin-imx8mp-15141027 replay[7474]: ERROR: ACCESS UNIT BOUNDARY CHECK
   Dec 18 21:18:51 verdin-imx8mp-15141027 replay[7474]: [2024-12-18T21:18:51Z INFO  maivin_replay::video_decode] Video dimensions are: 1920x1080
   Dec 18 21:20:51 verdin-imx8mp-15141027 systemd[1]: Stopping Maivin MCAP Replayer Service...
   Dec 18 21:20:51 verdin-imx8mp-15141027 systemd[1]: replay@verdin-imx8mp-15141027_2024_12_16_21_09_38.service: Deactivated successfully.
   Dec 18 21:20:51 verdin-imx8mp-15141027 systemd[1]: Stopped Maivin MCAP Replayer Service.
   ```
4. Restart the Camera, Model, IMU, Navsat, Radar Publish, and Fusion Services, either through the "Services Status" page in the WebUI at `https://<hostname>/config/services`, rebooting the device, or via the following systemd CLI command:
   ```bash
   sudo systemctl start camera model imu navsat radarpub fusion
   ```
The Replay Service can also be stopped by rebooting the device.