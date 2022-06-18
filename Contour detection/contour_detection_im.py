import cv2 as cv

img = cv.imread('C:\\Users\\amine\\Desktop\\codings\\Final\\img\\simu2.jpg')
print('image found')
print(img.shape)
h=img.shape[0]
w=img.shape[1]
result = img.copy()
result = cv.resize(result, (640, 484))
# Remove noise from the image
blurred = cv.GaussianBlur(result,(7,7),0)
img_gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(img_gray, 95, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
thresh = 255-thresh #The function findContours describes the contour of areas consisting of ones. The areas in which you are interested are black, though.    contours, _  = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
contours, _  = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    #____________________________
        #Straight Bounding Rectangl
        # Get the bounding rectangle
            
print("Number of Contours Returned: {}".format(len(contours)))
clength=format(len(contours))
clength=int(clength)
contour = contours[:]
yellowCL=[]
ss=0
for contour in contours:
    x, y, w, h = cv.boundingRect(contour)
            # Draw the rectangle around the object.
            #green=cv.rectangle(result, (x, y), (x+w, y+h), (0, 255, 0), 3)
            #print (green)
                
    f=10
    xy=x-f
    yy=y-f
    wy=w+f
    hy=h+f
    yellow = cv.rectangle(result, (xy, yy), (x+wy, y+hy), (0, 255, 255), 3)
    #print (yellow)
                
    yellowContour=([xy, yy],[x+wy, y+hy])
    print("\n yellowContour = ",yellowContour)                  
                
    yellowCL.insert(ss, yellowContour)
    ss += 1
    #____________________________
    #cv.drawContours(result, contours[:], -1, (0, 255, 0), 5)
    #print("Number of Contours Returned: {}".format(len(contours)))

print("yellowCL = ",yellowCL)

#____________________________
#store the coutours on a list
print("Number of Contours Returned: {}".format(len(contours)))
#thresh = cv.resize(thresh, (640, 484))
frameshape=result.shape
print(frameshape)
cv.imshow("Shapes", result)    
cv.imshow("THRESH", thresh)
cv.waitKey()
cv.destroyAllWindows()
