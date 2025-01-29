# Quick Start
This article will walk you through the Raivin setup and then lead you to resources for using additional features.

## Unboxing
The Maivin/Raivin box contains the following items:
* The Maivin/Raivin vision module
* A five-meter power cable, M12 circular connector (male) to 2.1mm x5.5 barrel adapter (female)
* Box with power adapters
    * Power-adapter with interchangeable plugs.  2.1mm x 5.5mm barrel adapter (male) connector.
    * Interchangeable plugs for the following regions:
        * NEMA 1-15P (Type A) (North America)
        * CEE-7/16 Alternative II "Europlug" (Type C) (Europe)
        * AS/NZS 3112, ungrounded (Type I) (Australia / Oceania)
        * BS 1363 (Type B) (British) wall adapter
* Desktop tripod

## Connecting the Device
If you wish to mount your Raivin to the tripod, it should be done now before connecting any of the other cables.  There are three mount points on the bottom of the device and one on each side.  Screw the tripod into the center bottom mount point.

Next, connect a standard Category 5 network cable (not included) from your shared network into the device.

Optionally, you can connect an antenna to the SMA connecter on the top-right corner of the back of the device to enhance GPS reception.

Chose the proper power adapter plug from your region and connect it to the power cable.  Then connect the M12 connector of the power cable to the connection at the back of the module, making sure to align the tab at the top of the connecter to its corresponding slot.
![M12 connector](static/quickStart-m12.png){align=center}

The device should boot up as soon as it is connected.  A blue light above and to the right of the power connecter should start blinking.
![Raivin Back Picture](static/quickStart-backPic.png){align=center}
*Raivin showing network connection (left), eight-digit ID number (middle), tripod connected (bottom), and power connection with blue status light on (right)*

```{warning}
The Raivin may get hot during operation.  Do not handle while operating.  Temperature can be measured with the `cat /dev/carrier_temp` command, which will output device temperature in millidegree Celsius.
```

## On Boot Up
The Raivin will have an eight-digit number on the back of the device.  This is the ID number.  The hostname of the Raivin will be "verdin-imx8mp-\<id>.local", which is advertised over Multicast Domain Name System (mDMS).  For the steps below, the eight-digit number is "15141029".  The device will have a hostname of `verdin-imx8mp-15141029.local`.  This hostname can be used to connect to the device over SSH and HTTP.
```{tip}
On Windows machines, you will not need to add the '.local' suffix.
```

The Raivin has a web interface that can be connected to via both HTTP and HTTPS by entering `http://verdin-imx8mp-<id>.local`.  On first connection to the web interface, you will get a "Your connection is not private" warning.
![Raivin Main Page Warning](static/quickStart-sslCert.png){align=center}
This is expected and nothing to worry about -- the HTTPS connection needs a SSL certificate which the vision module does not have.  Click the "Advanced" button, and then "Proceed to" link.
![Raivin Advanced Information](static/quickStart-sslAdvanced.png){align=center}

## The Raivin Web Interface
Let's introduce the Raivin web interface and the various pages and functionalities available to the user.

### The Main Page
The Main Page of the Raivin web interface should look as follows:
![Raivin Main Page](static/quickStart-mainPage.png){align=center}

There are five cards on the Main Page that link to the Visualization pages:
- **GPS**: This page displays a map with the current location of the device, along with GPS co-ordinates.
- **IMU**: This page displays the 3D orientation of the device with current pitch, yaw, and roll values.
- **MCAP**: This page contains the visual/radar recordings management interface.
- **Segmentation View**: This page shows the camera with running segmentation and/or detection pipeline.  For Raivins equipped with a radar module, it will also show the radar grid.
- **Occupancy Grid**: (Raivin only) This will show the radar grid.

### The Top Ribbon
The ribbon at the top of the Raivin web interface is available on every page of the web interface.  The following three elements are available on every page of the Raivin web interface.
1. On the left, the "Home" button with the Au-Zone icon, which will return the user to the Main Page.
2. In the middle, the title of the current page.
3. The farthest rightmost button, with the gear icon, is the Settings Buttons and will take you to the [Settings Page](./configuration.md).

On the right side of the ribbon, we have a grouping of two indicators an a dropdown menu.  These items are only shown on the Main Page and the pages clicked from the five cards on the Main Page.  These elements, from left to right, are:

4. The Recording Indicator, shown as a red circle when recording from the sensors.
5. The State and Status (S&S) indicator.
6. The Status Information Dropdown button.

### State and Status
Mousing over the S&S field will give a brief summary of any problems.
![Dropdown reporting good](static/quickStart-statusDropDownGood.png){align=center}
*Everything is good!*
![Dropdown reporting bad](static/quickStart-statusDropDownDegraded.png){align=center}
*The Radar Publishing service is down.*

There are three operational states for the Raivin, describing if the user as the set the Raivin to display the live sensor feeds, recorded sensor feeds, or neither.  Those states are:
1. **Live Mode**: The Raivin is displaying the live camera and radar module feeds.
2. **Replay Mode**:  The Raivin is displaying the recorded services
3. **Stopped**:  The Raivin is not displaying any feeds, live or recorded.

How to set these operational states is described in the [Recording section](./recording.md).

There are two status types for the Raivin:
1. **Active**: All relavent services for a state are up.  This will show up as reporting the state in green text in a light-green button.
2. **Degraded**: At least one service is not up.  This will show up as reporting the state in brown text in a yellow button.  It will also include the word "Degraded" after the operational state.

Clicking on the Information icon will get you a listing of the current services, including a "Configure Services" link to the "Service Status" page.
![Service List](static/quickStart-services.png)

## The Visualization Pages
These pages contain the user-facing functionality of the vision module.

### The Segmentation Page
The Segmentation page shows camera overlain with the current visual model output.  For Raivin modules, this will also includes the occupany grid at the bottom.
![IMU Page](static/quickStart-segmentation.png){align=center}
White points is unmatched, raw data from the radar; green points are raw data matched to segmentation masks.

### The Occupancy Page (Raivin-only)
The Occupancy Page shows the raw, radar data, coloured by radar cross-section (RCS) size.
![IMU Page](static/quickStart-occupancy.png){align=center}

### The GPS Page
The GPS page shows an interactive map centered on the device's location.
![GPS Page](static/quickStart-gps.png){align=center}
This should be familiar to anyone who has used standard map web interfaces.  The map can be moved by dragging with left-mouse button (or touch with a touchscreen-enabled device).  The "+" and "-" buttons on the left will zoom-in and zoom-out on the map.  The "Refresh" button will re-center the map on the device's location.  The latitude and longitude are also reported on the web interface.

### The IMU Page
The IMU page shows the device's orientation in 3D.
![IMU Page](static/quickStart-imu.png){align=center}
My physically moving the device, it's virtual counterpart should move the same way.  Roll, pitch, and yaw values are reported.  If the device's virtual orientation does not match the physical orientation, keep the device's bottom flat and hit the "Reset Orientation" button.

### The MCAP Recording Page
The MCAP Recording Page manages the device's operational state as well as the current recordings on the device.
![MCAP Page](static/quickStart-mcap.png){align=center}
More information for this page can be found in the [Recording section](./recording.md).
