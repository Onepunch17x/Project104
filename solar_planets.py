import cv2

img=cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(20,30),cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"mercury",(85,30),cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"venus",(200,30),cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"earth",(280,30),cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"mars",(365,30),cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"jupiter",(500,30),cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"saturn",(780,30),cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"uranus",(950,30),cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"neptune",(1200,30),cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))

cv2.imshow("output",img)
cv2.imwrite("solar-system.jpg",img)
cv2.waitKey(0)