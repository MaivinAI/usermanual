# Radar Module
The Raivin configuration includes an integrated [DRVEGRD-169 radar module][radar] from [smartmicro][smart].  The radar module is internally connected to the Raivin which provides power and data communications interfaces.  The primary data and control interface uses the CAN bus protocol.  The radar module is also connected through an internal Gigabit Ethernet interface which is used to transmit the [radar data cube][cube] used by the RadarExp Fusion model.

## Specifications
The DRVEGRD 169 radar module is a 79GHz radar sensor for multiple automotive applications that features 4D/PxHD technology.  The sensor’s antenna aims at ultra-short, short and medium range applications with a very wide, horizontal angular coverage of 140°.  A full set of the radar module specifications can be found [here][radar].

## Networking

The radar module is connected to the Raivin using two networking interfaces.  The primary interface is the `can0` interface which is used to configure the radar module and receive the radar point-cloud.  This interface is required for to control the radar module.  The secondary interface is the `ethernet1` interface which is used to transmit the radar data cube data to the Raivin.  This interface is required to provide input to the RadarExp Fusion model, but is not required for the radar module to function in point-cloud mode.  The radar data cube generates about 300Mb/s of data which is transmitted to the Raivin for processing.

### CAN Configuration

The CAN bus interface is managed through the systemd networking framework using the configuration file `/etc/systemd/network/can0.network`.  The CAN bus interface will be pre-configured by Torizon for Maivin but is covered in this section.

```
[Match]
Name=can0

[CAN]
BitRate=500K
```

The `can0` interface is configured for 500kbps.  The Radar Publishing Service manages the radar configuration and reading of the point-cloud data over CAN and publishing the results over Zenoh.  Refer to the [Radar Publishing Service](./radar.md) for details.


### Ethernet Configuration

The radar module streams the low-level radar data cube over an ethernet interface which is internally connected to the Raivin's `ethernet1` interface.  The connection is managed as `network1` using the NetworkManager configuration available at `/etc/NetworkManager/system-connections/network1.nmconnection`.

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

[radar]: https://www.smartmicro.com/automotive-radar/drvegrd-line#c20151
[smart]: https://www.smartmicro.com/
[cube]: https://www.mathworks.com/help/phased/gs/radar-data-cube.html