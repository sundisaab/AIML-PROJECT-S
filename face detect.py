import cv2

face_cap =cv2.CascadeClassifier("sample.xml")<----#ADD THE HAARASCODE FILE HERE FRONTALFASE SHEET..
video_cap = cv2.VideoCapture(0)
while True:
   
   ret, video_data = video_cap.read()
   col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
   faces = face_cap.detectMultiScale(
       col,
       scaleFactor=1.1,
       minNeighbors=5,
       minSize=(30,30),
       flags=cv2.CASCADE_SCALE_IMAGE

   )

   
   cv2.imshow("video_live", video_data)
   if cv2.waitKey(10) == ord("a"):
       break

video_cap.release()
