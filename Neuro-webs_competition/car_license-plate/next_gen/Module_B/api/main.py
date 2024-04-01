import streamlit as st
st.header('Приложение для распознавания автомобильных номеров')
# Заносим сюда наши функции использование которых было расписано до этого в Report.ipynb
def take_picture(path):
    import cv2
    img = cv2.imread(path)
    return img
def predicts(img, detect_model, reader_model):
    # Кропп изображения
    model = detect_model
    reader = reader_model
    results = model(img) # Детекция номеров на изображении
    output = {}
    if not results.xyxy[0].nelement() == 0:
        for i, res in enumerate(results.xyxy):
            print(f'Машина {i+1}:')
            crop_xy = list(map(int,(res.detach().flatten()[0],res.detach().flatten()[1],res.detach().flatten()[2],res.detach().flatten()[3]))) # преобразование результатов детекции в формат xyxy
            img = img[crop_xy[1]:crop_xy[3],crop_xy[0]:crop_xy[2]] # Кропп изображения слайсингом
            # Чтение надписей на изображении
            result = reader.readtext(img) # работа модели по прочтению текста
            # Преобразование результата в понятную форму и вывод результата
            result = [result[i][1] for i in range(len(result))]
            for re in result:
                print(re)
            output[i] = result
        return output
    else:
        print('Номер не распознан')
        return [[False]]
import torch
import easyocr
model = torch.hub.load('./yolov5', 'custom', path='./yolov5/runs/train/exp6/weights/last.pt' ,source='local')# Обозначение модели детекции изображений
reader = easyocr.Reader(['en','ru'],gpu = False) # обозначение модели читающей текст с картинки
path = st.text_input('Введите путь к изображению: ') # Форма для ввода пути к изображению
if path:
    st.write('Вот что мы получили: ', path) # Оповещения для пользователя
    img = take_picture(path)
    st.image(img)
    # Получение результата распознавания
    result = predicts(img,model,reader)
    st.write('В ходе распознавания мы получи такой результат:')
    for res in result.values():
        st.write(''.join(res))
    st.write(result)