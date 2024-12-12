# Foxglove Studio Integration

## Overview
This guide explains how to play back MCAP files captured using the Raivin Dataset Recorder on a PC using Foxglove Studio. Foxglove Studio is an open-source application from the ROS (Robot Operating System) ecosystem that supports playback for MCAP recordings.

## Prerequisites
- Foxglove Studio installed on your PC (Windows, Linux, or Mac)
- MCAP recording from your Raivin
- MCAP file transferred to your PC

## Getting Started

### Installing Foxglove Layout
1. Download the provided Raivin Foxglove Layout (available in Downloads section)
2. Open Foxglove Studio
3. Import the layout through the Layout menu

![Foxglove Layout Import](static/foxglove_layout.png){align=center}

### Layout Features
The default Raivin layout includes:
- Top panel: H.264 camera stream with bounding box overlays
  - Shows detection results (e.g., white boxes around faces when using facedetection model from `/usr/share/detect/facedetect.rtm`)
- Bottom right panel: GPS coordinates map view
  - Interactive map with zoomable blue target showing camera position
- Bottom left panel: IMU sensor readings
  - Can be configured to show real-time plots
- Bottom timeline: Playback controls for navigation

![Foxglove Layout Import](static/foxglove_scene.png){align=center}

## Visualization Features

### Missing Bounding Boxes
The `/detect/boxes2d` stream is the default output stream from the Maivin detection services. Because of the amount of data included within this stream, it is not compatible with the default bounding-box overlay API for Foxglove Studio. To visualize bounding boxes, there are two methods:

1. Use the EdgeFirst Detect Foxglove Plugin Gudie to enable Foxglove to render the `/detect/boxes2d` stream. 
   [Details can be found here][foxglove-plugin]
2. Enable the VISUALIZATION setting in the Maivin detect service and record the `/detect/visualization` topic into the MCAP. The process is detailed below.
   
**How to Enable Visualization**:
   
   a. Enable visualization in detect config:
   ```bash
   sudo vi /etc/default/detect
   # Set VISUALIZATION = "true"
   sudo systemctl restart detect
   ```
   
   b. Add visualization topic to recorder config:
   ```bash
   sudo vi /etc/default/recorder
   # Add /detect/visualization to TOPICS:
   TOPICS = "/imu /gps /camera/info /camera/h264 /detect/info /detect/boxes2d /detect/visualization"
   sudo systemctl restart recorder
   ```

   c. Configure in Foxglove:
   - Select gear icon in top right of camera panel
   - Enable the `/detect/visualization` topic (purple eye icon)
   - Consider enabling "synchronize annotations" for better alignment

   ![Foxglove Layout Import](static/foxglove_det.png){align=center}

### IMU Data Plotting
To create IMU sensor plots:
1. Convert bottom left panel to Plot view
2. Click "Add a Series"
3. Select `rt/imu` as the topic
4. Choose desired parameters (e.g., angular_velocity.x/y/z)
5. Repeat to add additional plot series as needed

![IMU Plot Configuration](static/imu.png){align=center}
![IMU Plot Configuration](static/imu_to_plot.png){align=center}
![IMU Plot Configuration](static/plot.png){align=center}
![IMU Plot Configuration](static/imu_msg.png){align=center}
![IMU Plot Configuration](static/imu_velocity.png){align=center}
![IMU Plot Configuration](static/imu_final_view.png){align=center}

### Viewing Segmentation Masks
The `/detect/mask` stream is the default output stream from the Maivin detection services. Because of the amount of data included within this stream, it is not compatible with the default Image drawing API in Foxglove Studio. To visualize the Segmentation Mask, please use the Foxglove Plugin Guide [See here][foxglove-plugin] for details.

## Additional Resources
For more detailed information about Foxglove Studio features, visit:
- [Foxglove Documentation](https://docs.foxglove.dev/docs/introduction/)

## Downloads
- Maivin 2 Foxglove Layout.json (2 KB) NOT SURE HOW TO ADD THIS?


