# Python 2/3 uyumluluk
from __future__ import print_function
import cv2
import numpy as np

clothes_cascade = cv2.CascadeClassifier('data/my_cascade.xml')

while True:
    # Resim yükleniyor.
	image = cv2.imread("ex.jpg")
	# Yüklenen resim siyah beyaz renge dönüştürülüyor.
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	clothes = clothes_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(70,150),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
	for (x,y,w,h) in clothes:
    	# Ekranda çizilen dikdörtgen üzerine açıklama yazılıyor.
		cv2.putText(image, "Kiyafetler", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1, cv2.LINE_AA)
		cv2.rectangle(image, (x,y), (x+w, y+h), (255, 0, 0), 2)
	
	# Resim yakalanmış hali ile ekranda gösteriliyor.
	cv2.imshow("Video", image)
	k = cv2.waitKey(30)
	if k == 27:		# Çıkış için ESC.
		break

cv2.destroyAllWindows()