# MCAP Playback Service

## Overview
The Replay Service enables you to replay saved MCAP files, allowing your Raivin to simulate previously recorded messages. When replayed, these messages are interpreted as if they were being received for the first time, providing full visualization capabilities in the WebUI.

## How It Works
The Replay Service:
- Loads and plays back MCAP recordings
- Simulates original message timing
- Automatically loops recordings
- Stops other input services to prevent interference
- Provides visualization through the WebUI

## Using the Replay Service

### Starting Playback
1. Access your Raivin through SSH
2. Use the following command to start playback:
   ```bash
   sudo systemctl start replay@filename
   ```
   Note: The filename can be found at `https://hostname/mcap` (exclude the .mcap extension)

### Finding Available Recordings
You can locate available recordings through:
- The WebUI interface as shown below
- Command line: `ls /media/DATA`

![MCAP Files List](static/mcap_recorder.png){align=center}

## Benefits
The Replay Service offers several advantages:
- Creates consistent test/debug environments
- Provides full control over input messages
- Enables solution verification with consistent data
- Allows continuous looping of recordings
- Isolates replay data from live inputs

## Limitations
Important considerations when using the Replay Service:

### Service Management
- Services stopped by the Replay Service must be manually restarted
- Alternatively, restart your Raivin to restore all services

### Concurrent Operations
- Multiple Replay Services can run simultaneously
- Running multiple replays may cause issues
- Stop previous replay before starting a new one

### Service Interruption
- All input services are stopped during replay
- Services are stopped regardless of MCAP content
- Example: Camera Service stops even if MCAP contains no camera data
