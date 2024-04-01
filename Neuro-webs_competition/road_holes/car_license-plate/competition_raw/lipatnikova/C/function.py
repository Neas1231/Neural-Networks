from PIL import Image
from yolov5.detect import run
import os


def get_text(images, path, reader):
    strok = []

    try:
        for img in images:
            image = Image.open(path + img) # данная переменная понадобиться в работе API для вывода обрезанной картинки
            img_text = reader.readtext(f'{path}{img}') # считываем текст с картинки
    except:
        image = Image.open('C:/Users/Participant/Desktop/lipatnikova/B/Untitled.png') 
        img_text=[(0, 'Текст не найден', 0)]

    final_text = ""

    for _, text, __ in img_text: # проходим по всему распознанному тексту
        final_text += text + ' ' # сохраняем текст с одной картинки в одну переменную
    strok.append(final_text) # добавляем в общий список картинок
    return strok[0], image # возвращаем картинку и данные по распознанному тексту

def get_foto(link):
    # если папка существует то происходит следующее:
    try:
        path_foto = str(run(weights= 'C:/Users/Participant/Desktop/lipatnikova/yolov5/runs/train/exp17/weights/best.pt', source= link, save_crop= True, project='C:/Users/Participant/Desktop/lipatnikova/B/crop_foto' )) + '/crops/plate/' # отправляем полученный путь в модель, находим объект обрезаем и возвращаем путь до обрезанной папки
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