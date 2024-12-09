.. _radar:

Radar Module
============

The Raivin configuration includes an integrated DRVEGRD-169 radar module from SmartMicro Systems.  
The radar module is internally connected to the Raivin which provides power and data communications 
interfaces.  The primary data and control interface is the CAN bus which is used to configure the 
radar and receive the radar point cloud data.  The radar module is also connected through an 
internal gigabit ethernet interface which is used to transmit the low-level radar data cube used by
the RadarExp Fusion Model.

Specifications
--------------


Networking
----------

The radar module is connected to the Raivin using two networking interfaces.  The primary interface
is the can0 interface which is used to configure the radar module and receive the radar point cloud.
This interface is required for the radar module to function.  The secondary interface is the ethernet1
interface which is used to transmit the radar data cube to the Raivin.  This interface is required for
the data fusion model to function, but is not required for the radar module to function in point cloud
mode.  The radar cube generates about 300MB/s of data which is transmitted to the Raivin for processing.

CAN Configuration
~~~~~~~~~~~~~~~~~


Ethernet Configuration
~~~~~~~~~~~~~~~~~~~~~~


