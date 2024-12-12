# Foxglove Plugin

## Introduction
For details on how to record a MCAP file, please see Recording Guide, and for details on how to playback MCAP files on Foxglove, please refer to Foxglove Studio Guide.

The `/detect/boxes2d` stream is the default output stream from the Maivin detection services. Because of the amount of data included within this stream, it is not compatible with the default bounding-box overlay API for Foxglove Studio. The instructions below describe how to install and use a Foxglove Studio extension purpose-built for integrating the `/detect/boxes2d` stream into Foxglove Studio.

Additionally, the `/detect/mask` stream for Segmentation masks is not compatible with the default overlay API for Foxglove Studio. The Foxglove Studio extension will integrate drawing and overlaying the Segmentation mask and allow visualization of the mask.

## Installing the Plugin
1. Download the `edgefirst.detect-1.0.2.foxe` Foxglove Extension (.foxe) file from Github.

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

## Using the plugin

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
