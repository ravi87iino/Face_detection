import cv2
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# cascade1 = cv2.CascadeClassifier("haarcascade_eye.xml")
vd = cv2.VideoCapture(0)
# use of variable address for connecting mobile camera for generating url we have to download ipwebcam app.
address = "https://192.168.0.116:8080"

vd.open(address)
while True:
  _,img = vd.read()
  gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  faces = cascade.detectMultiScale(gray_img,scaleFactor = 1.2,minNeighbors = 5,minSize = (50,50))
  
  for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
  
  cv2.imshow("detected faces",img)
  if cv2.waitKey(1) & 0Xff == ord('q'):
    break
vd.release()
cv2.destroyAllWindows()
