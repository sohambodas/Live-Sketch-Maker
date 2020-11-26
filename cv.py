import cv2

def nothing():
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('Sketch')
cv2.createTrackbar('L','Sketch',0,255,nothing)
cv2.createTrackbar('H','Sketch',0,255,nothing)


while(True):
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    L = cv2.getTrackbarPos('L','Sketch')
    H = cv2.getTrackbarPos('H','Sketch')
    i2 = cv2.Canny(gray, L, H)
    ret,i2 = cv2.threshold(i2, 50, 255,cv2.THRESH_BINARY_INV)
    cv2.imshow("original",img)
    cv2.imshow("Sketch",i2)
    
    if cv2.waitKey(1)== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



"""
 ret,img = cap.read()
    cv2.imshow("bot",img)
    i3 = cv2.(img,60,70)
	img1 = cv2.circle(img,(200,200),100,(255,0,0),5)
	cv2.imshow("bot2", i3)
	if cv2.waitKey(1)==ord('q'):
		break
    """
    