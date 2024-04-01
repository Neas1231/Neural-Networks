import unittest
from easyocr import Reader
from function import get_foto, get_text
reader = Reader(['en',], gpu = False)

class TestGetResult(unittest.TestCase):
    """Функция получения результата"""
    # тест с обработкой корректных данных и корректного ответа
    def test_text_one(self):
        self.assertEqual(get_text('22_10_2014_13_45_7_929.jpg', 'C:/Users/Participant/Desktop/lipatnikova/B/Data/images/test/', reader)[0], 'T 353Ep154 RUSE (d HOBOCHEMPCK-JAAA 0 (383) 334-7070, 216-11-16')
    # тест с обработкой некорректных данных и корректного ответа
    def test_text_two(self):
        self.assertEqual(get_text('no', 'no', reader), 'Текст не найден')
    """Функция отправки фото"""
    # тест с обработкой корректных данных и корректного ответа
    def test_foto_one(self):
        self.assertEqual(get_foto('C:/Users/Participant/Desktop/lipatnikova/B/Data/images/test/23 (2).jpg'), (['23 (2).jpg'], 'C:/Users/Participant/Desktop/lipatnikova/B/crop_foto/exp1'))
    # тест с обработкой некорректных данных и корректного ответа
    def test_foto_two(self):
        self.assertEqual(get_foto('no'), (['no', 'no']))

if __name__ == "__main__":
  unittest.main()
