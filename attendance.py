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
