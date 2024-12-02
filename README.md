# Automated Video Transcription, Segmentation, and GIF Creation

This project automates the process of **transcribing videos**, **segmenting them** based on meaningful timestamps, and creating **GIFs** with styled captions. The tool intelligently analyzes video content, segments it, and generates visually appealing GIFs with captions. It's a powerful tool for content creators, educators, and anyone looking to create engaging video snippets.



## Features

- **Automated Video Transcription**: Uses Whisper AI to transcribe spoken content from video files into text.
- **Video Segmentation**: Automatically segments the video into meaningful sections based on speech pauses and sentence boundaries, without including silent parts.
- **GIF Creation**: Creates GIFs from video segments with styled captions that align with the video content.
- **Custom Styling for Captions**: GIF captions can be styled for better visual appeal.
- **Automatic Workflow**: From transcription to GIF generation, everything is handled automatically.



## How It Works

1. **Transcription**: The tool transcribes the entire video into text using Whisper, a state-of-the-art speech recognition model.
2. **Segmentation**: The video is segmented based on meaningful speech boundaries, ensuring each segment corresponds to a complete sentence (with no silent parts).
3. **GIF Creation**: For each segment, a GIF is created with captions based on the transcribed text. The GIFs are styled with custom captions to make them more engaging.



## Installation

### Prerequisites

- Python 3.7 or later
- Required Python libraries:
  - `whisper`
  - `moviepy`
  - `argparse`

To install the required libraries, run:

```bash
pip install -r requirements.txt
