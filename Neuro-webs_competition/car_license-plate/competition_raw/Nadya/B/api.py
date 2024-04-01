import streamlit as st
from function import get_foto, get_text
from easyocr import Reader

def main():
    # пишем подсказку
    st.write('У вас есть возможность загрузить фотографии в модель как по ссылке, так и загрузив саму фотографию. \n При вводе строки и загрузки фотографии, поиск будет проходить по ссылке, то есть при загрузки фотографии следует очистить строку с ссылкой или путём. ')
    # записываем путь или ссылку к фотографии или фотографиям
    link = st.text_input('Введите путь (ссылку)')
    # пишем подсказку
    st.write('Если вы хотите загрузить фотографию, загружайте её из папки C:/Users/Participant/Desktop/Lipatnikova/B/')
    # записываем фотографию
    foto = st.file_uploader = ('Загрузить фотографию')
    # пишем подсказку
    st.write('Если оба поля заполнены, то поиск будет проходить по первому полю.')
    # если поле с фотографией заполнено забираем имя файла и получаем путь к нему
    if foto:
        foto = 'C:/Users/Participant/Desktop/Lipatnikova/B/' + foto.name
    # кнопка
    button = st.button('Распознать')
    # если кнопку нажали
    if button:
        # загружаем модель для считывания текста
        reader = Reader(['en',], gpu = True)
        # получаем фотографии и путь к ним
        if link:
            img, path = get_foto(link)
        elif foto:
            img, path = get_foto(foto)
        # получаем результат распознавания и фотографию
        text, image = get_text(img, path, reader)
        # выводим фотографию
        st.image(image)
        # выводим результат распознавания
        st.write('Результат распознавания: ', text)

main()