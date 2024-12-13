# Foxglove Studio

## Overview
This guide explains how to play back MCAP files captured using the Raivin Dataset Recorder on a PC using Foxglove Studio. Foxglove Studio is an open-source application from the ROS (Robot Operating System) ecosystem that supports playback for MCAP recordings.

## Prerequisites
- [Foxglove Studio][foxglove] installed on your PC (Windows, Linux, or Mac)
  - The EdgeFirst Plug-in is required for certain Maivin topics
- MCAP recording from your Raivin
- MCAP file transferred to your PC

## Getting Started

### Installing EdgeFirst Plugin

1. Download the `edgefirst.detect-VERSION.foxe` Foxglove Extension (.foxe) file from [Github](https://github.com/MaivinAI/foxglove-edgefirst/releases/latest).

2. Open Foxglove Studio

3. Uninstall any existing versions of the EdgeFirst Detect plugin
   - Open the user settings on the top right of the window and click Extensions.
     
     ![Foxglove Settings](static/foxglove_setting.png){align=center}
   
   - Click the EdgeFirst Detect plugin

     ![Foxglove Settings](static/foxglove_extenstion_view.png){align=center}

   - Click "Uninstall"

     ![Foxglove Settings](static/foxglove_install_extenstion.png){align=center}

4. Open the Foxglove Extension file in Foxglove Studio. This can be done one of two ways:
   - Double-click on the downloaded .foxe file.
   - Drag and Drop the .foxe file onto the Foxglove Studio window.

5. There should be a popup that says the extension successfully installed.

6. Close Foxglove Studio and restart it.

7. Open the user settings on the top right of the window and click Extensions (As Shown in the screenshot above).
   - A local extension called EdgeFirst Detect should be available
   - Clicking the plugin will bring up details about it

### Installing Foxglove Layout
1. [Download the Raivin Foxglove Layout](https://support.deepviewml.com/hc/en-us/article_attachments/24761835729293)
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

### Viewing /detect/boxes2d Messages

1. Record a MCAP file that has the `/detect/boxes2d` message in it. See Maivin Dataset Recording for details

2. Play the MCAP file in Foxglove Studio. See Playback MCAP with Foxglove Studio for details.

3. The `/detect/boxes2d` message should appear under the list of valid image annotations

   ![Foxglove Settings](static/foxglove_detect_plugin_view.png){align=center}

4. Enable the Image annotations `/detect/boxes2d` by clicking the eye icon. This will draw boxes around the detected objects.

### Viewing /detect/mask Messages

1. Record a MCAP file that has the `/detect/mask` message in it. See Maivin Dataset Recording for details

2. Play the MCAP file in Foxglove Studio. See Playback MCAP with Foxglove Studio for details.

3. The `/detect/mask` message should appear under the list of valid image annotations

   ![Foxglove Settings](static/foxglove_segment_plugin_view.png){align=center}

4. Enable the Image annotations `/detect/boxes2d` by clicking the eye icon. This will draw a mask overlay on top of the camera stream.
   
   ![Foxglove Settings](static/foxglove_segmentation_view.png){align=center}

5. To view the masks directly without overlaying, the Topic for the image panel can be changed to the `/detect/mask` topic.
   
   ![Foxglove Settings](static/foxglove_topic_selection.png){align=center}

6. This will draw the Mask directly onto the Image Panel.
   
   ![Foxglove Settings](static/foxglove_segmentation_mask.png){align=center}

### Viewing /radar/cube Messages

1. Record a MCAP file that has the `/radar/cube` message in it. See Maivin Dataset Recording for details

2. Play the MCAP file in Foxglove Studio. See Playback MCAP with Foxglove Studio for details.

3. In the image panel, the `/radar/cube` topic should appear under the list of valid image topics
   
   ![Foxglove Settings](static/foxglove_radar_mask.png){align=center}

4. Select the `/radar/cube` topic

5. Change the color mode to Color Map, and select Turbo for the color map
   
   ![Foxglove Settings](static/foxglove_radar_msg.png){align=center}

6. Leave the value min and value max on auto

7. You can now see the RadarCube message
   
   ![Foxglove Settings](static/foxglove_final_radar_view.png){align=center}

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

## Troubleshooting

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

## Additional Resources

For more detailed information about Foxglove Studio features, visit:
- [Foxglove Documentation](https://docs.foxglove.dev/docs/introduction/)


[foxglove]: https://foxglove.dev/download