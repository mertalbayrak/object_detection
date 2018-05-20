import urllib.request
import cv2
import numpy as np
import os

# Dataset'i url üzerinden indirilip, belirli bir düzen üzerine dosyaya kaydediliyor.
# Örnek kaydetme: neg/1.jpg
def store_raw_images():
    neg_images_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04335693'
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()

    if not os.path.exists('neg'):
        os.makedirs('neg')

    picture_number = 1

    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            # Örnek kaydetme: neg/1.jpg
            urllib.request.urlretrieve(i, "neg/"+ str(picture_number)+ '.jpg')
            # Kaydedilen resim siyah beyaz renge dönüştürülüyor. 
            image = cv2.imread("neg/"+str(picture_number)+'.jpg', cv2.IMREAD_GRAYSCALE)
            # Kaydedilen resim yeniden boyutlandırılıyor.
            resize_image = cv2.resize(image, (100, 100))
            # Resim yeni rengi ve boyutu ile tekrardan dosyaya kaydediliyor.
            cv2.imwrite("neg/"+str(picture_number)+'.jpg', resize_image)
            picture_number += 1

        except Exception as e:
            print(str(e))

def find_crash_image():
    for file_type in ['neg']:
        for image in os.listdir(file_type):
            for crash in os.listdir('data/crash_image'):
                try:
                    
                    current_image_path = str(file_type) + '/' + str(image)
                    crash = cv2.imread('data/crash_image/'+str(crash))
                    question = cv2.imread(current_image_path)
                    # Url'den hatalı inmiş olan resimler, 
                    # örnek hatalı bir resim ile xor işleminden geçiyor ve hatalı resim siliniyor.
                    if crash.shape == question.shape and not(np.bitwise_xor(crash, question).any()):
                        print('Broken image')
                        print(current_image_path)
                        os.remove(current_image_path)
                    
                except Exception as e:
                    print(str(e))


def create_pos_n_neg():
    for file_type in ['neg']:
        for image in os.listdir(file_type):
            if file_type == 'neg':
                # neg dosyanın içindeki resimler kullanılarak bg.txt dosyası oluşturuluyor.
                # bg.txt -> Resim bilgilerinin tutulduğu txt.
                line = file_type+'/'+image+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)
            elif file_type == 'pos':
                line = file_type+'/'+image+ '1 0 0 50 50\n'
                with open('info.dat', 'a') as f:
                    f.write(line)

#store_raw_images()
#find_crash_image()
#create_pos_n_neg()
