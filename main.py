import cv2
import dlib
import time
import streamlit as st
from scipy.spatial.distance import euclidean
from PIL import Image
import pandas as pd

# Initialize Dlib face detector and shape predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Blink Detection Constants
BLINK_THRESHOLD = 4.5
BLINK_COUNT_TARGET = 3
TIME_LIMIT = 7

def midpoint(p1, p2):
    return (p1.x + p2.x) // 2, (p1.y + p2.y) // 2

def get_eye_ratio(eye_points, facial_landmarks):
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))
    hor_line_length = euclidean(left_point, right_point)
    ver_line_length = euclidean(center_top, center_bottom)
    return hor_line_length / ver_line_length if ver_line_length != 0 else 0

# Streamlit UI Enhancements
st.set_page_config(page_title="Blink Detection System", page_icon="👀", layout="centered")
st.title("🔍 Blink Detection System")
st.write("CAPTCHA Refinig tool to detect human and bot using blinking pattern.")
from PIL import Image; import streamlit as st
img = Image.open("/home/avroop_rakehop/Desktop/CAPTCHA/pbl-2/PBL-working/interface-img.jpg").resize((500, 500))
col1, col2, col3 = st.columns([1,2,1]); col2.image(img)

start_button = st.button(" Start Blink Detection")

if start_button:
    st.warning("Please ensure your face is well-lit and fully visible in the camera.")
    cap = cv2.VideoCapture(0)
    blink_count = 0
    blink_detected = False
    start_time = time.time()
    
    frame_placeholder = st.empty()
    status_placeholder = st.empty()
    time_placeholder = st.empty()
    blink_placeholder = st.empty()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture frame from webcam. Please check your camera.")
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        
        for face in faces:
            landmarks = predictor(gray, face)
            left_eye_ratio = get_eye_ratio([36, 37, 38, 39, 40, 41], landmarks)
            right_eye_ratio = get_eye_ratio([42, 43, 44, 45, 46, 47], landmarks)
            blink_ratio = (left_eye_ratio + right_eye_ratio) / 2
            
            if blink_ratio < BLINK_THRESHOLD:
                if not blink_detected:
                    blink_count += 1
                    blink_detected = True
            else:
                blink_detected = False
        
        elapsed_time = time.time() - start_time
        
        frame_placeholder.image(frame, channels="BGR", caption="Live Webcam Feed")
        blink_placeholder.write(f"**Blinks Detected:** {blink_count}")
        time_placeholder.write(f"**Time Left:** {TIME_LIMIT - int(elapsed_time)} sec")
        
        if blink_count >= BLINK_COUNT_TARGET:
            status_placeholder.success(" Human Detected! Welcome!")
            break
        elif elapsed_time > TIME_LIMIT:
            status_placeholder.error(" Bot Detected! Please try again.")
            break
        
    cap.release()
    st.info("Blink detection session completed. Refresh to retry.")
# ========== FOOTER ==========
st.markdown('<div class="footer">| AI CAPTCHA Research Project</div>', unsafe_allow_html=True)