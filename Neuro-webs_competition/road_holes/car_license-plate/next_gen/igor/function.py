from PIL import Image
from yolov5.detect import run
import os
import cv2
import numpy as np
from pylab import rcParams


def get_text(images, path, reader):
    strok = []

    try:
        for img in images:
            # image = Image.open(path + img) # данная переменная понадобиться в работе API для вывода обрезанной картинки
            # tests
            image_path = path+img
            # image = cv2.imread(image_path, 0)
            # th = image.copy()
            # th[th<200] = 0
            # bbox = np.where(th>0)
            # y0 = bbox[0].min()
            # y1 = bbox[0].max()
            # x0 = bbox[1].min()
            # x1 = bbox[1].max()
            # image = image[y0:y1, x0:x1]
            # equ = cv2.equalizeHist(image)
            # blur = cv2.GaussianBlur(equ, (5, 5), 1)
            # th2 = 60 # this threshold might vary!
            # equ[equ>=th2] = 255
            # equ[equ<th2]  = 0
            # rcParams['figure.figsize'] = 8, 16
            # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # edges = cv2.Canny(gray_image, 50, 150, apertureSize=3)
            # contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            # largest_contour = max(contours, key=cv2.contourArea)
            # x, y, w, h = cv2.boundingRect(largest_contour)
            # number_image = image[y:y+h, x:x+w]
            # angle = cv2.minAreaRect(largest_contour)[-1]
            # if angle < -45:
            #     angle = -(90 + angle)
            # else:
            #     angle = -angle
            # rows, cols, _ = number_image.shape
            # rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
            # rotated_image = cv2.warpAffine(number_image, rotation_matrix, (cols, rows), flags=cv2.INTER_LINEAR)
            # gray_image = rotated_image
            # smoothed_image = cv2.GaussianBlur(image, (5, 5), 0)
            # gray_image = cv2.cvtColor(smoothed_image, cv2.COLOR_BGR2GRAY)
            # _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            # img_text = reader.readtext(binary_image)
            # img_text = reader.readtext(equ, allowlist='A, B, E, K, M, H, O, P, C, T, y, X, 1,2,3,4,5,6,7,8,9,0, А, В, Е, К, М, Н, О, Р, С, Т, У, Х') # считываем текст с картинки 
            img_text = reader.readtext(image_path, allowlist='A, B, E, K, M, H, O, P, C, T, y, X, 1,2,3,4,5,6,7,8,9,0, А, В, Е, К, М, Н, О, Р, С, Т, У, Х') # считываем текст с картинки 
            # tests
            # img_text = reader.readtext(f'{path}{img}') 
                                    #    allowlist='A, B, E, K, M, H, O, P, C, T, y, X, 1,2,3,4,5,6,7,8,9,0') # считываем текст с картинки
    except:
        image = Image.open('C:/Users/igorv/Desktop/proffessionals_plates_license/my_tests/lipatnikova/B/Untitled.png') 
        img_text=[(0, 'Текст не найден', 0)]

    final_text = ""

    for _, text, __ in img_text: # проходим по всему распознанному тексту
        final_text += text + ' ' # сохраняем текст с одной картинки в одну переменную
    strok.append(final_text) # добавляем в общий список картинок
    return strok[0], image
    # return strok[0], image # возвращаем картинку и данные по распознанному тексту

def get_foto(link):
    # если папка существует то происходит следующее:
    try:
        path_foto = str(run(weights= 'C:/Users/igorv/Desktop/proffessionals_plates_license/my_tests/lipatnikova/yolov5/runs/train/exp36/weights/best.pt', source= link, save_crop= True, project='C:/Users/igorv/Desktop/proffessionals_plates_license/my_tests/lipatnikova/B/crop_foto' )) + '/crops/plate/' # отправляем полученный путь в модель, находим объект обрезаем и возвращаем путь до обрезанной папки
        """
        weights - веса нашей обученной модели 
        source - ресурс, ссылка на картинку или папку
        save_crop - параметр отвечающий за сохранение обрезанного фрагмента фото, на котором нашли объект
        project - путь куда будет сохраняться вся информация во время обнаружения объектов
        """
        imgs = os.listdir(path_foto)   # считываем картинки в папке
        return imgs, path_foto
    # если же папки не существует происходит это:
    except:
        return 'no', 'no'