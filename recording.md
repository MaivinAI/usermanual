# MCAP Recording Service

## Overview
The Recorder Service enables you to capture and store ROS2 topic data in MCAP format, providing a comprehensive recording solution for your Raivin system. This service acts as a data historian, collecting published topics from various services for later analysis and playback.

## How It Works
When active, the Recorder Service:
- Monitors and logs specified topics
- Compiles data into an MCAP file format
- Automatically saves the file upon service termination
- Provides real-time recording status through the WebUI

## Using the Recorder

### Starting a Recording
1. Access the WebUI using your Raivin's Hostname
2. Navigate to the MCAP page
3. Click the "Start Recording" button to begin capturing data

![MCAP Recorder Interface](static/mcap_recorder.png){align=center}

### Managing Recordings
Once a recording is complete, you can:
- View detailed metadata about the recording
- See the size and duration of the captured data
- Check which topics were recorded
- Monitor the recording status

![MCAP File Details](static/mcap_detail.png){align=center}

### Downloading and Analysis
- Click the download button to save the MCAP file to your PC
- Use Foxglove Studio to analyze the recorded data
- Visualize and replay the captured topics
- Share recordings with team members for collaborative analysis

## Configuration
The Recorder Service is configurable through a configuration file that specifies:
- Which topics to record
- Location of the recording file
- Recording compression

To modify these settings:
1. Navigate to `https://hostname/config/recorder` in your web browser
2. Update the desired configuration parameters
3. Save your changes to apply the new settings

![MCAP Configuration Settings](static/mcap_setting.png){align=center}

The topics that will be compiled into the MCAP file are determined through the configuration file as shown above.

