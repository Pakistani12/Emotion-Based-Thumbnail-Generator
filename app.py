

import streamlit as st
import cv2
import numpy as np
import os
import tempfile
from fer import FER
from PIL import Image


emotion_detector = FER()

st.title("Emotion-Based Thumbnail Generator")
st.write("Upload a video to extract thumbnails based on detected emotions.")


uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov", "mkv"])

if uploaded_file:
    temp_dir = tempfile.TemporaryDirectory()  
    video_path = os.path.join(temp_dir.name, uploaded_file.name)

   
    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())

    
    cap = cv2.VideoCapture(video_path)
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    st.write(f"Video uploaded: {uploaded_file.name}")
    st.write(f"Frame Rate: {frame_rate} FPS")
    st.write(f"Total Frames: {total_frames}")

    
    target_emotions = st.multiselect(
        "Select emotions to extract thumbnails:",
        ["angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"]
    )
    
    if st.button("Process Video"):
        st.write("Processing video... Please wait.")
        extracted_frames = []
        frame_count = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            # Process every 10th frame (adjustable for performance)
            if frame_count % 10 == 0:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                emotions = emotion_detector.detect_emotions(frame_rgb)
                
                if emotions:
                    # Extract dominant emotion
                    top_emotion = max(emotions[0]['emotions'], key=emotions[0]['emotions'].get)
                    
                    if top_emotion in target_emotions:
                        # Convert frame to PIL image
                        image = Image.fromarray(frame_rgb)
                        extracted_frames.append((image, frame_count))
            
            frame_count += 1
        
        cap.release()  # Ensure video is released before cleanup
        st.write(f"{len(extracted_frames)} thumbnails extracted.")

        
        for idx, (img, frame_no) in enumerate(extracted_frames):
            st.image(img, caption=f"Frame {frame_no}", use_column_width=True)
            
            thumbnail_path = os.path.join(temp_dir.name, f"thumbnail_{idx}.jpg")
            img.save(thumbnail_path)
            
            with open(thumbnail_path, "rb") as f:
                st.download_button(
                    label=f"Download Thumbnail {idx+1}",
                    data=f.read(),
                    file_name=f"thumbnail_{idx}.jpg",
                    mime="image/jpeg"
                )

   
    temp_dir.cleanup()

