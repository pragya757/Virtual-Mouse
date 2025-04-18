# AI-Powered Hand Gesture and Eye Control System

A sophisticated computer control system that combines hand gesture recognition and eye tracking for intuitive human-computer interaction. Control your computer naturally using hand movements and eye gestures.

## 🌟 Features

### Hand Controls
- 👆 **Cursor Mode**: Control mouse cursor with index finger
- 🤏 **Volume Control**: Adjust system volume using thumb-index pinch
- ☝️ **Scroll Mode**: Smooth scrolling with finger movements
- 🖱️ **Click Actions**: 
  - 👍 Left click: Thumb to palm
  - 🤙 Right click: Pinky to palm
### Eye Controls
- 👁️ **Gaze Control**: Move cursor with eye movement
- 😉 **Wink Actions**:
  - Double blink: Left click
  - Left wink: Right click

## 🎮 Detailed Control Guide

### Hand Gesture Modes
1. **Normal Mode (N)**
   - Make a fist to reset to normal mode
   - All fingers closed: [0,0,0,0,0]

2. **Cursor Mode**
   - Show all fingers: [1,1,1,1,1]
   - Move index finger to control cursor
   - Bring thumb close to palm for left click
   - Bring pinky close to palm for right click

3. **Volume Control**
   - Show thumb and index: [1,1,0,0,0]
   - Increase distance between fingers to increase volume
   - Decrease distance to lower volume

4. **Scroll Mode**
   - Show index finger only: [0,1,0,0,0]
   - Move up/down to scroll
   - Two fingers for faster scrolling

5. **Eye Control Mode**
   - Show thumb, index, and pinky: [1,1,0,0,1]
   - Look around to move cursor
   - Blink both eyes for left click
   - Wink left eye for right click

## 💻 System Requirements

- Windows 10/11
- Python 3.7 or higher
- Webcam with minimum 720p resolution
- 4GB RAM minimum
- Intel i3/AMD equivalent or better processor
- Good lighting conditions
- Clear background (preferably)

## ⚡ Performance Tips

1. **Lighting Setup**
   - Ensure well-lit environment
   - Avoid backlighting
   - Avoid direct sunlight on camera

2. **Camera Position**
   - Place camera at eye level
   - Maintain 50-70cm distance
   - Keep hands within frame
   - Center your face for eye tracking

3. **Gesture Tips**
   - Make clear, distinct hand gestures
   - Keep movements steady
   - Avoid rapid hand movements
   - Keep hand parallel to camera

4. **Eye Tracking Tips**
   - Face camera directly
   - Avoid wearing reflective glasses
   - Make deliberate blink actions
   - Keep head relatively still

5. **Background**
   - Use solid color background if possible
   - Avoid moving objects behind you
   - Clear workspace around tracking area

## 🚀 Quick Start

1. Install required packages:
```bash
pip install opencv-python mediapipe numpy pyautogui pycaw comtypes
```
