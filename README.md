# CAPTCHA_REFINING_PROJECT
# 👁️ AI-Based Blink Detection CAPTCHA Alternative

This project provides an **AI/ML-powered CAPTCHA alternative** designed to improve accessibility and bot prevention using **facial expression analysis**—specifically **blink detection**—as a form of human verification.

Built as part of our end-semester academic project at SIT, the solution aims to assist platforms like **UIDAI** with more inclusive, real-time authentication methods.

---

## 🧠 Key Features

- 🔍 Real-time blink detection using **Dlib** and **OpenCV**
- ⏱️ User verification based on blink pattern: **3 blinks within 7 seconds**
- 🧑‍🦯 Inclusive design to assist the **visually impaired**
- 💻 Streamlit web interface for a simple user experience

---

## 🛠️ Tech Stack

- Python 3.x  
- Dlib (68 facial landmarks)  
- OpenCV  
- Streamlit  
- SciPy  
- PIL  
- Pandas

---

## 🚀 How It Works

1. User clicks **Start Blink Detection**.
2. The webcam is activated, and Dlib identifies eye landmarks.
3. The **Eye Aspect Ratio (EAR)** is computed per frame to detect blinks.
4. If the user blinks **3 or more times within 7 seconds**, they're classified as **Human**.
5. Otherwise, they're flagged as **Bot**.

---

## 📦 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/blink-captcha-alternative.git
cd
