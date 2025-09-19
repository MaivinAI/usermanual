# 4K Camera System Documentation

## Overview

The Maivin Camera system provides advanced 4K video processing capabilities through a sophisticated tiling architecture. This document explains how the 4K functionality works, including video capture, processing, encoding, and streaming.

## Architecture

### Core Components

1. **Camera Capture**: Captures 4K video (3840x2160) from the camera device
2. **Tile Processing**: Divides 4K video into 4 separate 1080p tiles
3. **Parallel Encoding**: Each tile is encoded independently using H.264
4. **Streaming**: Tiles are published as separate video streams via Zenoh

### 4K Tiling System

The system implements a 2x2 tiling approach where a 4K source (3840x2160) is divided into four 1080p tiles:

```
┌─────────────┬─────────────┐
│  Top Left   │  Top Right  │
│  (1920x1080)│  (1920x1080)│
├─────────────┼─────────────┤
│ Bottom Left │Bottom Right │
│  (1920x1080)│  (1920x1080)│
└─────────────┴─────────────┘
```

## Implementation Details

### Tile Position Enum

```rust
enum TilePosition {
    TopLeft,
    TopRight,
    BottomLeft,
    BottomRight,
}
```

Each tile position defines:
- **Crop Parameters**: Source coordinates and dimensions for cropping
- **Output Dimensions**: Fixed at 1920x1080 for each tile

### Crop Calculation

The `get_crop_params()` method calculates the source region for each tile:

```rust
fn get_crop_params(&self, source_width: u32, source_height: u32) -> (u32, u32, u32, u32) {
    let source_tile_width = source_width / 2;
    let source_tile_height = source_height / 2;
    
    match self {
        TilePosition::TopLeft => (0, 0, source_tile_width, source_tile_height),
        TilePosition::TopRight => (source_tile_width, 0, source_tile_width, source_tile_height),
        TilePosition::BottomLeft => (0, source_tile_height, source_tile_width, source_tile_height),
        TilePosition::BottomRight => (source_tile_width, source_tile_height, source_tile_width, source_tile_height),
    }
}
```

### Video Processing Pipeline

#### 1. Camera Capture
- Captures 4K video frames from camera device
- Supports YUYV format
- Configurable mirror settings (none, horizontal, vertical, both)
- Target FPS: 30 FPS

#### 2. Tile Distribution
When `h264_tiles` is enabled:
- Creates 4 separate encoding threads
- Each thread processes one tile position
- Uses bounded channels (capacity: 3) for frame distribution
- Implements frame dropping when channels are full to prevent blocking

#### 3. Video Encoding

**VideoManager with Crop Support**:
```rust
VideoManager::new_with_crop(
    FourCC(*b"H264"),
    output_width: i32,      // 1920
    output_height: i32,     // 1080
    crop_rect: (x, y, w, h), // Tile-specific crop region
    bitrate: H264Bitrate,
    target_fps: Option<i32>
)
```

**Encoding Process**:
1. **Direct Encoding**: Uses `encode_direct()` for efficient processing
2. **Crop Region**: Automatically crops the source image to tile dimensions
3. **H.264 Encoding**: Hardware-accelerated encoding using VSL encoder
4. **Bitrate Control**: Configurable bitrate settings (5-100 Mbps)

#### 4. Frame Rate Management

- **Camera FPS**: 30 FPS target
- **Tile FPS**: Configurable (default: 15 FPS)
- **Frame Interval**: Calculated as `1000ms / tile_fps`
- **Frame Dropping**: Skips encoding if insufficient time has passed

### Configuration Options

#### Command Line Arguments

```bash
# Enable 4K tile streaming
--h264-tiles

# Configure tile topics (default: rt/camera/h264/tl tr bl br)
--h264-tiles-topics "rt/camera/h264/tl rt/camera/h264/tr rt/camera/h264/bl rt/camera/h264/br"

# Set tile frame rate (default: 15 FPS)
--h264-tiles-fps 15

# Set H.264 bitrate
--h264-bitrate auto|mbps5|mbps25|mbps50|mbps100

# Camera resolution (should be 4K for tiles)
--camera-size 3840 2160

# How to Run
sudo ./edgefirst-camera --h264-tiles --h264-tiles-fps 30 --camera-size 3840 2160 --stream-size 3840 2160
```

#### Environment Variables

```bash
export H264_TILES=true
export H264_TILES_FPS=15
export H264_BITRATE=auto
export CAMERA_SIZE="3840 2160"
```

### Streaming Architecture

#### Zenoh Integration

- **Publisher per Tile**: Each tile has its own Zenoh publisher
- **Topic Structure**: 
  - `rt/camera/h264/tl` - Top Left tile
  - `rt/camera/h264/tr` - Top Right tile  
  - `rt/camera/h264/bl` - Bottom Left tile
  - `rt/camera/h264/br` - Bottom Right tile

#### Message Format

Each tile stream publishes `FoxgloveCompressedVideo` messages:

```rust
FoxgloveCompressedVideo {
    header: Header {
        stamp: Time { sec, nanosec },
        frame_id: "camera_optical_topleft", // Tile-specific frame ID
    },
    format: "h264",
    data: Vec<u8>, // H.264 encoded video data
}
```

### Performance Optimizations

#### 1. Parallel Processing
- **4 Independent Threads**: Each tile processed in separate thread
- **Thread Names**: `h264_tile_topleft`, `h264_tile_topright`, etc.
- **Tokio Runtime**: Each thread runs its own async runtime

#### 2. Memory Management
- **DMA Buffer Sharing**: Efficient zero-copy operations
- **Bounded Channels**: Prevents memory buildup during slow encoding
- **Frame Dropping**: Graceful handling of encoding bottlenecks

#### 3. Hardware Acceleration
- **G2D Integration**: Hardware-accelerated image processing
- **VSL Encoder**: Hardware H.264 encoding
- **Direct Encoding**: Bypasses unnecessary conversions

#### 4. Dynamic Crop Updates
- **Source Size Detection**: Monitors camera resolution changes
- **Crop Region Updates**: Automatically adjusts crop parameters
- **Runtime Adaptation**: Handles resolution changes without restart

### Error Handling

#### Channel Management
```rust
fn try_send(tx: &Sender<(Image, Timestamp)>, img: Image, ts: Timestamp, _name: &str) {
    match tx.try_send((img, ts)) {
        Ok(_) => {},
        Err(_) => {
            // Silently drop frames when channels are full
            // Prevents log spam during high load
        }
    }
}
```

#### Encoding Errors
- **VideoManager Creation**: Fails gracefully with detailed error messages
- **Encoding Failures**: Logged per tile with position information
- **Publishing Errors**: Individual tile failures don't affect others

### Monitoring and Debugging

#### Tracy Profiling
- **Frame Marks**: Visual frame boundaries in Tracy
- **Bitrate Plotting**: Real-time bitrate monitoring
- **Performance Metrics**: Encoding time and throughput

#### Logging
- **Structured Logging**: Tile-specific log spans
- **Error Tracking**: Detailed error messages with context
- **Performance Warnings**: FPS monitoring and alerts

### Usage Examples

#### Basic 4K Tile Streaming
```bash
./edgefirst-camera \
  --h264-tiles \
  --camera-size 3840 2160 \
  --h264-bitrate mbps25 \
  --h264-tiles-fps 15
```

#### Custom Topic Configuration
```bash
./edgefirst-camera \
  --h264-tiles \
  --h264-tiles-topics "camera/tl camera/tr camera/bl camera/br" \
  --camera-size 3840 2160
```

#### High Performance Setup
```bash
./edgefirst-camera \
  --h264-tiles \
  --h264-bitrate mbps50 \
  --h264-tiles-fps 30 \
  --camera-size 3840 2160 \
  --tracy  # Enable profiling
```

### Integration with ROS/Foxglove

The system is designed for seamless integration with ROS and Foxglove Studio:

1. **Foxglove Studio**: Can subscribe to individual tile topics
2. **Multi-View Layout**: Display all 4 tiles simultaneously
3. **Synchronized Playback**: All tiles share the same timestamp
4. **Independent Control**: Each tile can be controlled separately

### Troubleshooting

#### Common Issues

1. **Low FPS Warnings**
   - Check camera resolution settings
   - Verify hardware encoding support
   - Monitor system resources

2. **Encoding Failures**
   - Ensure 4K camera resolution is set
   - Check bitrate settings
   - Verify G2D hardware support

3. **Channel Full Errors**
   - Reduce tile FPS if encoding is slow
   - Increase system performance
   - Check for memory issues

#### Performance Tuning

1. **Bitrate Selection**
   - `auto`: Let encoder decide (recommended)
   - `mbps25`: Good balance for most use cases
   - `mbps50`: High quality, requires more bandwidth

2. **Frame Rate Optimization**
   - Lower tile FPS reduces CPU usage
   - Higher tile FPS improves smoothness
   - Balance based on application requirements

3. **System Resources**
   - Monitor CPU usage across all threads
   - Ensure sufficient memory for buffers
   - Check hardware encoding availability

This documentation provides a comprehensive overview of the 4K camera system's architecture and implementation. The tiling approach enables efficient processing and streaming of high-resolution video while maintaining performance and flexibility.
