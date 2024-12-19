# MCAP Recording Service

## Overview
The Recorder Service enables you to capture and store ROS2 topic data in MCAP format, providing a comprehensive recording solution for your Raivin system. This service acts as a data historian, collecting published topics from various services for later analysis and playback.

### How It Works
When active, the Recorder Service:
- Logs specified topics
- Compiles data into an MCAP-format recording
- Automatically saves the file upon service termination
- Provides real-time recording status

## Using the Recorder

### Starting a Recording
In the Web UI
1. Go to the MCAP recording page: `https://<hostname>/mcap`.
2. Click the "Recording" toggle to begin capturing data
   ```{image} static/mcap_recorder.png
   :alt: MCAP recorder interface
   :align: center
   ```
3. To stop recording, click the "Recording" toggle a second time.

### Managing Recordings
Once a recording is complete, you can see the size in MB and duration in seconds of the captured data on the MCAP page.  You can also get more detailed metadata, such as the topics recorded, by clicking the "Details" button for the MCAP recording.
```{image} static/mcap_detail.png
:alt: MCAP file details
:align: center
```
```{note}
MCAP recording file names are saved in `hostname_YYYY_mm_DD_HH_MM_SS.mcap` format, where:
- _hostname_ is the hostname of the device, e.g. `verdin-imx8mp-071744901`
- _YYYY_mm_DD_ is the zero-padded year, month, and day that the recording was started
- _HH_MM_SS_ is the UTC time the recording start in 24-hour notation
```

Any MCAP recording can be deleted by clicking its "Delete" button and confirming that you wish to delete the button.

### Downloading and Analysis
Click the download button to save the MCAP file to your PC.  You can also use a SSH client to copy files off the Raivin.  Once the MCAP recording is saved on to your PC, you can use an MCAP reader such as [Foxglove Studio](./foxglove.md) to analyze the recorded data.
```{tip}
You can use a SSH client to secure-copy the files from the device.  For example, OpenSSH comes with the `scp` executable that can copy files from the device.  From the above MCAP recording screenshot, we could use `scp` to download the first file with the following invocation:
```bash
scp torizon@verdin-imx8mp-07174490.local:/media/DATA/verdin-imx8mp-07174490_2022_04_28_11_44_13.mcap .
```

## Configuration
The Recorder Service is configurable through a configuration file that specifies:
- Which topics to record
- Location of the recording file
- Recording compression

To modify these settings:
1. Navigate to `https://hostname/config/recorder` in your web browser
2. Update the desired configuration parameters
3. Click the "Save Configuration" button to apply the new settings
```{image} static/mcap_setting.png
:alt: MCAP configuration settings
:align: center
```
You can use the "Search Topics" text box to narrow down the topics you to include or exclude from your MCAP recording.
```{image} static/mcap_radar_topics.png
:alt: MCAP radar topics
:align: center
```