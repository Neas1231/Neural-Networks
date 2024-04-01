import unittest
from glob import glob
import random
# Обозначение функции для получения фото
def take_picture(path):
    import cv2
    img = cv2.imread(path)
    return img
# Тестирование функции
class TestTakePicture(unittest.TestCase):
    def setUp(self):
        self.func = take_picture # Загрузка функции в тест класс
    # Тест нашей функции на случайных картинках в директории Result_A
    def test1(self):
        files = glob('../Result_A/licenses/images/*')
        self.func(files[random.randint(0, len(files))])
    def test2(self):
        files = glob('../Result_A/licenses/images/*')
        self.func(files[random.randint(0, len(files))])
    def test3(self):
        files = glob('../Result_A/licenses/images/*')
        self.func(files[random.randint(0, len(files))])
if __name__ == '__main__':
    unittest.main()
