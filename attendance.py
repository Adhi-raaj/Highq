import cv2
import os
import pandas as pd
from datetime import datetime
#Load the xml file for frontal face detection
face_cascade = cv2.CascadeClassifier("C:\Users\23ad1\Desktop\HighQ\haarcascade_frontalface_default.xml")

#function to mark attendance in csv file
def markAttendance(name):
    csv_path="C:\Users\23ad1\Desktop\HighQ\Attendance.csv"
    df = pd.read_csv(csv_path) if os.path.exists(csv_path) else pd.DataFrame(columns=['Name', 'Time'])
    
    # If this name is not already marked, add it with timestamp
    if name not in df['Name'].values:
        now = datetime.now()
        dtString = now.strftime('%H:%M:%S')
        # Append new row and save CSV
        df = pd.concat([df, pd.DataFrame([[name, dtString]], columns=['Name', 'Time'])], ignore_index=True)
        df.to_csv(csv_path, index=False)
        print(f'✅ Attendance marked for {name} at {dtString}')
#webcam start code
cap = cv2.VideoCapture(0)
attendance_marked = False  # Flag to check if attendance is already marked

while True:
    # Read frame from webcam
    success, img = cap.read()
    # Convert to grayscale for face detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        # Draw rectangle around the detected face
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
        # Put name text above the rectangle
        cv2.putText(img, "Akshat", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        # Mark attendance for the detected face
        markAttendance("Akshat")
        attendance_marked = True  # Update flag to true

    # Display the webcam feed with rectangles
    cv2.imshow('Webcam', img)
# ✅ If attendance was marked, wait for 5 seconds and then exit
    if attendance_marked:
        print("✅ Face detected! Closing in 5 seconds...")
        cv2.waitKey(5000)
        break

    # ✅ Allow manual exit by pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ✅ Release resources after finishing
cap.release()
cv2.destroyAllWindows()
