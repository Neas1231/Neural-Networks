import unittest
from glob import glob
import random
def take_picture(path):
    import cv2
    img = cv2.imread(path)
    return img
def predicts(img):
    import torch
    import easyocr
    # Кропп изображения
    model = torch.hub.load('../yolov5', 'custom', path='../yolov5/runs/train/exp6/weights/last.pt' ,source='local')# Обозначение модели кропа детекции изображений
    results = model(img) # Детекция номеров на изображении
    if not results.xyxy[0].nelement() == 0:
        crop_xy = list(map(int,(results.xyxy[0].detach().flatten()[0],results.xyxy[0].detach().flatten()[1],results.xyxy[0].detach().flatten()[2],results.xyxy[0].detach().flatten()[3]))) # преобразование результатов детекции в формат xyxy
        img = img[crop_xy[1]:crop_xy[3],crop_xy[0]:crop_xy[2]] # Кропп изображения слайсингом
        # Чтение надписей на изображении
        reader = easyocr.Reader(['en','ru'],gpu = False) # обозначение модели читающей текст с картинки
        result = reader.readtext(img) # работа модели по прочтению текста
        # Преобразование результата в понятную форму и вывод результата
        result = [result[i][1] for i in range(len(result))]
        for res in result:
            print(res)
        return result
    return 'Номер не распознан'
class TestTakePicture(unittest.TestCase):
    def setUp(self):
        self.picture = take_picture
        self.func = predicts

    def test1(self):
        files = glob('../Result_A/licenses/images/*')
        self.func(self.picture(files[random.randint(0, len(files))]))

    def test2(self):
        files = glob('../Result_A/licenses/images/*')
        self.func(self.picture(files[random.randint(0, len(files))]))

    def test3(self):
        files = glob('../Result_A/licenses/images/*')
        self.func(self.picture(files[random.randint(0, len(files))]))

if __name__ == '__main__':
    unittest.main()