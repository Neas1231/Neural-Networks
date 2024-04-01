import cv2
import streamlit as st
import torch
import numpy as np
import easyocr
from PIL import Image

def predictions(img):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./best.pt')
    preds = model(img)
    if not preds.xyxy[0].nelement() == 0:
        results = list(map(lambda x: int(round(x, 0)), preds.xyxy[0][0].detach().cpu().numpy()))
        img = img[results[1]:results[3], results[0]:results[2]]

        reader = easyocr.Reader(['en', 'ru'], gpu=True)
        _, text, __ = reader.readtext(img)[0]
        return text


st.header("Программа для распознавания номеров авто")
img_file_buffer = st.camera_input("Сделайте фото если возможно")
st.write("Либо")
uploaded_file = st.file_uploader("Загрузите изображение")
if img_file_buffer is not None:
    img = np.array(Image.open(img_file_buffer))
    pred = predictions(img)
    st.write('Результат:')
    st.write(pred)
try:
    if uploaded_file is not None:
        img = np.array(Image.open(uploaded_file))
        pred = predictions(img)
        st.write('Результат:')
        st.write(pred)
except:
    st.write('Что-то пошло не так :(')
