import argparse
import whisper
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import TextClip, CompositeVideoClip

# Step 1: Transcribe video and extract timestamps
def transcribe_and_timestamp(video_path):
    model = whisper.load_model("base")
    result = model.transcribe(video_path, word_timestamps=True)
    
    segments = []
    current_sentence = ""
    start_time = None
    
    for segment in result["segments"]:
        for word in segment["words"]:
            if not start_time:
                start_time = word["start"]
            
            current_sentence += word["word"] + " "
            if word["word"].endswith((".","!","?")):  # End of a sentence
                segments.append({
                    "start": start_time,
                    "end": word["end"],
                    "text": current_sentence.strip()
                })
                current_sentence = ""
                start_time = None

    print("Transcription and timestamping completed!")
    return segments

# Step 2: Create video segments
def segment_video(video_path, segments):
    video = VideoFileClip(video_path)
    for i, segment in enumerate(segments):
        start = segment["start"]
        end = segment["end"]
        output_filename = f"segment_{i}.mp4"
        subclip = video.subclip(start, end)
        subclip.write_videofile(output_filename, codec="libx264")
        print(f"Segment {i} saved: {segment['text']}")

# Step 3: Create GIFs with stylish captions
def create_gifs_with_captions(segments):
    for i, segment in enumerate(segments):
        video_clip = VideoFileClip(f"segment_{i}.mp4")
        text = segment["text"]
        
        # Stylish captions
        txt_clip = TextClip(
            text,
            fontsize=48,
            font='Arial-Bold',
            color='white',
            stroke_color='black',
            stroke_width=3,
            size=(video_clip.size[0] - 40, None),
            align="center",
            method="caption"
        ).set_position("bottom").set_duration(video_clip.duration)
        
        # Combine text with video
        video_with_text = CompositeVideoClip([video_clip, txt_clip])
        
        # Export as GIF
        gif_path = f"gif_{i}.gif"
        video_with_text.write_gif(gif_path, fps=10)
        print(f"GIF saved: {gif_path}")

# Main function
def main():
    parser = argparse.ArgumentParser(description="Automated Video-to-GIF Tool")
    parser.add_argument("video", help="Path to the video file")
    
    args = parser.parse_args()
    
    # Step 1: Transcription and timestamping
    segments = transcribe_and_timestamp(args.video)
    
    # Step 2: Segment video dynamically
    segment_video(args.video, segments)
    
    # Step 3: Create GIFs with captions
    create_gifs_with_captions(segments)

if __name__ == "__main__":
    main()
