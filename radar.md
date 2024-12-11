# Radar Module

The Raivin configuration includes an integrated DRVEGRD-169 radar module from SmartMicro Systems.  
The radar module is internally connected to the Raivin which provides power and data communications 
interfaces.  The primary data and control interface is the CAN bus which is used to configure the 
radar and receive the radar point cloud data.  The radar module is also connected through an 
internal gigabit ethernet interface which is used to transmit the low-level radar data cube used by
the RadarExp Fusion Model.

## Specifications

The Raivin uses the SmarMicro DRVEGRD 169 radar module.  The DRVEGRD 169 is a 79GHz radar sensor for multiple automotive applications that features 4D/PxHD technology.

The sensor’s antenna aims at ultra-short, short and medium range applications with a very wide horizontal angular coverage. It features:

- A straight beam with a wide field of view
- Selectable modes: ultra-short-, short-, medium- and long-range mode

## Networking

The radar module is connected to the Raivin using two networking interfaces.  The primary interface
is the can0 interface which is used to configure the radar module and receive the radar point cloud.
This interface is required for the radar module to function.  The secondary interface is the ethernet1
interface which is used to transmit the radar data cube to the Raivin.  This interface is required for
the data fusion model to function, but is not required for the radar module to function in point cloud
mode.  The radar cube generates about 300MB/s of data which is transmitted to the Raivin for processing.

### CAN Configuration

The CAN bus interface is managed through the SystemD networking framework using the configuration file `/etc/systemd/network/can0.network`.  The CAN will be pre-configured by Torizon for Maivin but is covered in this section.

```
[Match]
Name=can0

[CAN]
BitRate=500K
```

The `can0` interface is configured for 500kbps.  The radarpub service manages the radar configuration and reading of the point-cloud data over CAN and publishing the results over Zenoh.  Refer to the radarpub service for details.


### Ethernet Configuration

The radar module streams the low-level radar data cube over an ethernet interface which is internally connected to the Raivin's ethernet1 interface.  The connection is managed as network1 using the NetworkManager configuration `/etc/NetworkManager/system-connections/network1.nmconnection`.

```
[connection]
id=network1
type=ethernet
interface-name=ethernet1

[ethernet]

[ipv4]
address1=192.168.11.17/24
method=manual

[ipv6]
method=disabled

[proxy]
```

