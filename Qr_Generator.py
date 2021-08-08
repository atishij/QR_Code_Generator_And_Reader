import qrcode
import cv2
img = qrcode.make("https://github.com/atishij")
img.save("github.jpg")
d = cv2.QRCodeDetector()
val, points,straight_qrcode = d.detectAndDecode(cv2.imread("github.jpg"))
print(val)