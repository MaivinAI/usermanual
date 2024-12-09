.. _release_notes:

Release Notes
=============

Version 2024Q4
--------------

This is the first official release of the Maivin Perception Platform.

For Maivin users this software release is a major upgrade which unifies the Torizon for Maivin
branches of Raivin and Maivin into a single software release.  As part of this release the version
naming has been updated to follow the YYYYQX.PATCH (YEAR*Q*QUARTER) format instead of using the 
Torizon version number as the base.  The upstream Torizon OS version number is documented in the 
release notes.

This release includes a major update to the web interface of the Maivin Perception Platform.  The new
interface provides a collection of panels that can be used to monitor and control the platform.  The
primary panel for the Maivin is the segmentation view while Raivin provides a combined segmentation
and occupancy grid panel as well as an occupancy grid only panel.

A configuration panel has been added allowing the user to configure various aspects of the platform.
Currently configuration is focused on the EdgeFirst Middleware services but future updates plan to
add networking and other configuration options.

EdgeFirst Models
~~~~~~~~~~~~~~~~

- ModelPack for Detection and Segmentation
- RadarExp Fusion Model

EdgeFirst Packages
~~~~~~~~~~~~~~~~~~

- Camera
- Radarpub
- Model
- Fusion
- IMU
- NavSat
- Recorder
- Playback
- WebUI
- Web Server

System Packages
~~~~~~~~~~~~~~~

- Torizon 6.8.0
- Linux 5.15

Known Issues
~~~~~~~~~~~~
