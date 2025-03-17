# Emotion-Based-Thumbnail-Generator
This Streamlit application extracts thumbnails from uploaded video files based on detected facial emotions. The application utilizes the fer library for facial expression recognition and OpenCV for video processing.

## **Features**

- Upload a video file (.mp4, .avi, .mov, .mkv).

- Analyze frames using facial expression recognition.

- Select target emotions to extract thumbnails.

- Download extracted thumbnails.

## **Requirements**

Ensure you have the following dependencies installed:
```sh
pip install streamlit opencv-python numpy fer pillow
```
## **How to Run**

Run the Streamlit application using the command:
```sh
streamlit run app.py
```
## **Usage**

1-Upload a video file.

2-Select target emotions from the dropdown list.

3-Click "Process Video" to extract thumbnails.

4-View and download the generated thumbnails.

## **Supported Emotions**

- Angry

- Disgust

- Fear

- Happy

- Neutral
  
- Surprise

- Sad
## **Technologies Used**

- Python for scripting

- Streamlit for UI

- OpenCV for video processing

- FER for facial emotion detection

- Pillow for image processing


- Surprise
