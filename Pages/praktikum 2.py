import streamlit as st
from PIL import Image
import cv2
import numpy as np
import copy

def main():
    st.title("Praktikum 2 OPERATOR ARITMATIK")
    with st.container():
        # task 0
        st.header('Task 0')
        foto = st.file_uploader("UPLOAD FOTO ",['png','jpg','jpeg'])
        label = st.file_uploader("UPLOAD LABEL",['png','jpg','jpeg'])
        # foto = cv2.imread('imgs/aku.JPG')
        # foto = cv2.cvtColor(foto, cv2.COLOR_BGR2RGB)
        # label = cv2.imread('imgs/label.png')
        # label = cv2.cvtColor(label, cv2.COLOR_BGR2RGB)
        if foto is not None and label is not None:
            st.image(foto, 'Ini Foto')
            st.image(label, 'Ini Label')
            foto = convertImage(foto)
            label = convertImage(label)
            label = cvResizeImage(foto, label)
            labelInverse = numpyInverseImage(label)
            st.image(labelInverse, 'Ini Label Inverse')

            st.subheader('Operasi Aritmatik Citra')
            tab1, tab2, tab3, tab4 = st.tabs(["ADD", "MIN", "MAX", "SUBTRACT"])
            with tab1:
                st.image(addImage(foto, labelInverse))
            with tab2:
                st.image(minImage(foto, label))
            with tab3:
                st.image(maxImage(foto, labelInverse))
            with tab4:
                st.image(subImage(foto, labelInverse))
            st.subheader('CATATAN')
            st.write('1. IMAGE PERTAMA adalah membuat citra baru dari 2 gambar yaitu foto dan label.  proses penggabungan keduanya ialah diambil minimum. sedangkan untuk foto akan diambil semua karena minimum dan untuk label akan diambil text karena berwarna hitam atau nilai 0')
            st.write('2. IMAGE KEDUA membuat citra baru dari gabungan 2 image yaitu foto dan labelInverse dengan maximum. Lalu, kenapa menggunakan label inverse? karena jika menggunakan label bukan inverse maka akan diambil warna putih latar dari label sehingga menutupi foto.')
            st.write('3. IMAGE KETIGA adalah proses membuat citra dari hasil kurang 2 image yaitu foto dan labelInverse. jika hasil kurang lebih kecil dari 0 maka akan dianggap 0 yaitu menjadi hitam.')

            st.header('TASK 1 OPERASI BITWISE CITRA')
            tab11, tab12, tab13 = st.tabs(["AND", "OR", "XOR"])
            with tab11:
                st.image(bitwiseAndImage(foto, label), 'Foto vs Label')
                st.image(bitwiseAndImage(foto, labelInverse), 'Foto vs LabelInverse')
            with tab12:
                st.image(bitwiseOrImage(foto, label), 'Foto vs Label')
                st.image(bitwiseOrImage(foto, labelInverse), 'Foto vs LabelInverse')
            with tab13:
                st.image(bitwiseXorImage(foto, label), 'Foto vs Label')
                st.image(bitwiseXorImage(foto, labelInverse), 'Foto vs LabelInverse')
            
            st.subheader('Image Blur')
            st.image(blurImage(foto, (10,10)))
                

def convertImage(img):
    nparr = np.fromstring(img.getvalue(), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def addImage(img1, img2):
    img = cv2.add(img1, img2)
    return img

def subImage(img1, img2):
    img = cv2.subtract(img1, img2)
    return img

def maxImage(img1, img2):
    img = cv2.max(img1, img2)
    return img

def minImage(img1, img2):
    img = cv2.min(img1, img2)
    return img

def numpyInverseImage(img):
    img = 255 - img
    return img

def cvInverseImage(img):
    img = cv2.bitwise_not(img)
    return img

def cvResizeImage(img1, img2):
    height, width, channels = img1.shape
    img2 = cv2.resize(img2, (width, height))
    return img2

def bitwiseAndImage(img1, img2):
    img = cv2.bitwise_and(img1, img2)
    return img

def bitwiseOrImage(img1, img2):
    img = cv2.bitwise_or(img1, img2)
    return img

def bitwiseXorImage(img1, img2):
    img = cv2.bitwise_xor(img1, img2)
    return img

def blurImage(img, ksize):
    img = cv2.blur(img, ksize)
    return img

if __name__ == '__main__':
	main()