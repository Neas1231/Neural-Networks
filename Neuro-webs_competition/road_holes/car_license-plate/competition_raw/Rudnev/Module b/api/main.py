import streamlit as st
st.header('Приложение для распознавания автомобильных номеров')
# Заносим сюда наши функции использование которых было расписано до этого в Report.ipynb
def take_picture(path):
    import cv2
    img = cv2.imread(path)
    return img
def predicts(img):
    import torch
    import easyocr
    # Кропп изображения
    model = torch.hub.load('./yolov5', 'custom', path='./yolov5/runs/train/exp6/weights/last.pt' ,source='local')# Обозначение модели кропа детекции изображений
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

path = st.text_input('Введите путь к изображению: ') # Форма для ввода пути к изображению
if path:
    st.write('Вот что мы получили: ', path) # Оповещения для пользователя
    try:    # Получение изображения
        img = take_picture(path)
        st.image(img)
    except:
        st.write("Не получилось загрузить фото, попробуйте другой путь или файл")
    # Получение результата распознавания
    try:
        result = predicts(img)
        st.write('В ходе распознавания мы получи такой результат:')
        for res in result:
            st.write(res)
    except:
        st.write('Не получилось распознать на картинке лицензию')
