# object_detection
Object Detection using Python(3.6) and OpenCV

Training Cascade oluşturmak için gerekli işlemler:

opencv_createsamples -img example.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle -0.5 -maxzangle 0.5 -num 880

bacground image kullanılarak positive image üretmek için gerekli kod.

-img [image] -> Pozitif resim oluşturmak için kullanacağı ana resim.

-bg bg.txt -> Resmin dosya konumu ve ismini içeren txt.

-info info/info.lst -> İşlem sonucu oluşacak resimlerin (sayi, x koordinat, y koordinat, genişlik, yükseklik) bilgilerini içerecek olan dosya.

-num [number] -> negatif resim sayısı.

-----------------------------------------------------------------------------------------------

opencv_createsamples -info info/info.lst -num 880 -w 20 -h 20 -vec positives.vec

pozitif resimlerin bilgilerinin oluşmasını sağlar.

-----------------------------------------------------------------------------------------------

opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 880 -numNeg 880 -numStages 1 -w 20 -h 20

Burada önceden oluşturuğumuz negatif, pozitif, bg dosyalarını kullanarak antreman yaptırılıyor.

-numPos [number] -> Pozitif resim sayısı.

-numNeg [number] -> Negatif resim sayısı.

-numStages [number] -> Yapılacak işlem sayısı.PS:Ne kadar fazla olursa o kadar uzun sürecektir.
