import cv2
import time
import os

ip = os.environ.get('tapo_510w_ip')
# camera account username you created in Tapo app
user = os.environ.get('tapo_510w_username')
password = os.environ.get('tapo_510w_password')
rtsp = f"rtsp://{user}:{password}@{ip}:554/stream1"

cap = cv2.VideoCapture(rtsp)     # may be slow to connect first time
time.sleep(1.0)                  # let connection warm up
ret, frame = cap.read()
cap.release()
if not ret:
    raise SystemExit(
        "Failed to grab frame — check RTSP URL, credentials or model support.")
cv2.imwrite("snapshot.jpg", frame)
print("Saved snapshot.jpg")
