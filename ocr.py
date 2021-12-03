from PIL import Image
import pytesseract
import cv2
import os

image = cv2.imread("image.png")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhite) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

filename = "{}.png".format(os.getpid())
cv2.imwrite(filename,blackAndWhite)

text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)


bNWResize=cv2.resize(blackAndWhite, (500, 500))
cv2.imshow("image",image)
cv2.imshow("Output",bNWResize)
cv2.waitKey(0)