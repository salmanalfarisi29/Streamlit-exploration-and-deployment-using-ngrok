import streamlit as st
from PIL import Image
import cv2
import numpy as np
import copy
import matplotlib.pyplot as plt

def main():
    st.title("Praktikum 3 HISTOGRAM CITRA")
    with st.container():
        # task 0
        st.header('Task 0')
        img = st.file_uploader("UPLOAD FOTO ANDA",['png','jpg','jpeg'])
        st.subheader('upload dengan format png, jpg atau jpeg')
        if img is not None:
            gray = loadImageGray049(img)
            img = convertImage(img)
            b, g, r = cv2.split(img)
            # calculate histogram
            hist_b = cv2.calcHist([b], [0], None, [256], [0,256])
            hist_g = cv2.calcHist([g], [0], None, [256], [0,256])
            hist_r = cv2.calcHist([r], [0], None, [256], [0,256])
            hist_gray = cv2.calcHist([gray], [0], None, [256], [0,256])

            fig, ax = plt.subplots()
            ax.plot(hist_b, color='blue')
            ax.plot(hist_r, color='red')
            ax.plot(hist_g, color='green')
            ax.plot(hist_gray, color='black')
            # ax.xlim([0, 256])

            average_intensity = np.mean(gray)
            contrast = calculateContrast(img)

            st.subheader('Gambar')
            tab1, tab2 = st.tabs(["sebelum di grayscale", "setelah di grayscale"])
            with tab1:
                st.image(img, 'gambar')
            with tab2:
                st.image(gray, 'setelah di grayscale')

            st.subheader('Histogram')
            st.pyplot(fig)
            st.text_input('Rata-rata', average_intensity)
            st.text_input('Contrast', contrast)

            # task 1
            st.header('TASK 1 EQUALIZATION')
            img_2 = cv2.equalizeHist(gray)
            hist_eq = cv2.calcHist([img_2],[0],None,[256],[0,256])
            fig2, ax2 = plt.subplots()
            ax2.plot(hist_eq)
            st.pyplot(fig2)
            tab11, tab12 = st.tabs(["gambar", "setelah di grayscale"])
            with tab11:
                st.image(imgEqualizationColor049(img), 'gambar')
            with tab12:
                st.image(imgEqualization049(img), 'Setelah di grayscale')


def convertImage(img):
    nparr = np.fromstring(img.getvalue(), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def addImage049(img1, img2):
    img = cv2.add(img1, img2)
    return img

def subImage049(img1, img2):
    img = cv2.subtract(img1, img2)
    return img

def maxImage049(img1, img2):
    img = cv2.max(img1, img2)
    return img

def minImage049(img1, img2):
    img = cv2.min(img1, img2)
    return img

def numpyInverseImage049(img):
    img = 255 - img
    return img

def cvInverseImage049(img):
    img = cv2.bitwise_not(img)
    return img

def cvResizeImage049(img1, img2):
    height, width, channels = img1.shape
    img2 = cv2.resize(img2, (width, height))
    return img2

def bitwiseAndImage049(img1, img2):
    img = cv2.bitwise_and(img1, img2)
    return img

def bitwiseOrImage049(img1, img2):
    img = cv2.bitwise_or(img1, img2)
    return img

def bitwiseXorImage049(img1, img2):
    img = cv2.bitwise_xor(img1, img2)
    return img

def blurImage049(img, ksize):
    img = cv2.blur(img, ksize)
    return img

def loadImageGray049(img):
    nparr = np.fromstring(img.getvalue(), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

def calculateContrast(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    std = np.std(img)
    return std

def imgEqualization049(img):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = cv2.equalizeHist(img)
    return img

def imgEqualizationColor049(img):
    r, g, b = cv2.split(img)
    b = cv2.equalizeHist(b)
    g = cv2.equalizeHist(g)
    r = cv2.equalizeHist(r)
    return cv2.merge([r, g, b])


if __name__ == '__main__':
	main()