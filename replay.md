# MCAP Replay Service

## Overview
The Replay Service allows users to play back previously recorded MCAP files, enabling detailed analysis of MCAP data. This service provides flexible playback options and integrates with live fusion and model data for comprehensive testing and validation.

### How It Works
The Replay Service offers:
- Playback of recorded MCAP files
- Hybrid mode combining recorded and live data
- Real-time status monitoring
- Seamless integration with live system operations

## Using the Replay Feature

### Starting Playback
In the Web UI:
1. Navigate to the MCAP page: `https://<hostname>/mcap`
![MCAP replay options](static/replay_visualization.png){align=center}
2. Locate your desired MCAP file in the file list
3. Click the "Play" button (▶️) next to the file
4. In the playback options dialog, choose your preferred settings:
   - Fusion Source: Choose between Live or MCAP data
   - Model Source: Choose between Live or MCAP data
   ![MCAP replay options](static/replay_options.png){align=center}
5. Click "Start" to begin playback

### Playback Controls
During playback:
- The currently playing file will be highlighted and marked as "Now Playing"
   ![MCAP replay options](static/replay_mode.png){align=center}
- Toggle the "Live Feed" switch to return to live system data
![MCAP replay options](static/replay_to_live_mode.png){align=center}
- Click the stop button (⏹️) on the playing file to end playback
```{note}
When a file is playing, you cannot play another file until you stop the current playback.
```

### Hybrid Mode
The replay feature supports a hybrid mode where you can:
- Play back recorded sensor data while using live fusion and/or model data
![MCAP replay options](static/replay_options.png){align=center}
- Use recorded data for some systems while maintaining live data for others
- Mix and match recorded and live data sources based on your testing needs

# Status Monitoring

## System Status Bar

### Overview
The status bar provides real-time information about your system's operational state and service health.

### Status Indicators

#### Mode Indicator
Located in the top-right corner, the mode indicator shows:
- **Live Mode** (Green): System is operating with live data
- **Replay Mode** (Blue): System is playing back an MCAP file
- **Degraded Mode** (Amber): Some services are not operating optimally
- **Critical Mode** (Red): Critical services are not functioning

#### Recording Indicator
A pulsing red circle appears when:
- The system is actively recording
![MCAP replay options](static/recorder_running.png){align=center}

### Service Status
Click the information (ℹ️) button to view detailed service status:
- Individual service states (Running/Stopped)
![MCAP replay options](static/system_status.png){align=center}
- Quick overview of system health

