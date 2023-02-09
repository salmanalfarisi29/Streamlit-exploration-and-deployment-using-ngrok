import streamlit as st
from PIL import Image
import cv2
import numpy as np
import copy

def main():
    st.title("Praktikum 1 Pengolahan Citra")
    with st.container():
        # task 0
        st.header('TASK 0 HAI CITRA')
        img = st.file_uploader("Pilih gambar",['png','jpg','jpeg'])
        st.subheader('SILAHKAN UPLOAD GAMBAR ANDA DIATAS')
        if img is not None:
            st.image(img)
            img = convertImage(img)
            r, g, b = cv2.split(img)
            
            r_dup = copy.deepcopy(r)
            g_dup = copy.deepcopy(g)
            b_dup = copy.deepcopy(b)

            r_dup[:] = 0
            g_dup[:] = 0
            b_dup[:] = 0

            # 1
            st.subheader('HANYA R, G, ATAU B')
            tab1, tab2, tab3 = st.tabs(["RED", "GREEN", "BLUE"])

            with tab1:
                st.image(onlyOne(r))

            with tab2:
                st.image(onlyOne(g))

            with tab3:
                st.image(onlyOne(b))

            # 2
            st.subheader('1 kanal')
            tab1, tab2, tab3 = st.tabs(["RED", "GREEN", "BLUE"])

            with tab1:
                st.image(oneChannel([r, g_dup, b_dup]))

            with tab2:
                st.image(oneChannel([r_dup, g, b_dup]))

            with tab3:
                st.image(oneChannel([r_dup, g_dup, b]))
        
        # Task 1
        st.header('Task 1')
        st.write("Cek nilai piksel citra diatas, kemudian: \nUbah Warna SegiLima menjadi RGB(255,255,0) \nUbah Warna Segitiga menjadi RGB(0,255,255) \nUbah Warna Awan menjadi RGB(255,0,255)")

        img_tantangan = cv2.imread('imgs/tantangan.png')
        img_tantangan = cv2.cvtColor(img_tantangan, cv2.COLOR_BGR2RGB)
        st.image(img_tantangan)

        st.subheader("Hasil Praktikum")
  
        task1 = copy.deepcopy(img_tantangan)
        #segilima
        st.write("SegiLima menjadi RGB(255,255,0)")
        task1[np.where((task1 == [255, 0, 0]).all(axis=2))] = [255, 255, 0]
        st.image(task1)
        #segitiga
        st.write("Ubah Warna Segitiga menjadi RGB(0,255,255)")
        task1[np.where((task1 == [0, 255, 0]).all(axis=2))] = [0, 255, 255]
        st.image(task1)
        #segitiga
        st.write("Ubah Warna Awan menjadi RGB(255,0,255)")
        task1[np.where((task1 == [0, 0, 255]).all(axis=2))] = [255, 0, 255]
        st.image(task1)

def onlyOne(color):
    pil_049 = Image.fromarray(color)
    return pil_049

def oneChannel(var):
    merged = cv2.merge(var)
    pil_049 = Image.fromarray(merged)
    return pil_049


def convertImage(img):
    nparr = np.fromstring(img.getvalue(), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def task1ChangeColor(img):
    img[np.where((img == [255, 0, 0]).all(axis=2))] = [255,255,0]
    img[np.where((img == [0, 255, 0]).all(axis=2))] = [0,255,255]
    img[np.where((img == [0, 0, 255]).all(axis=2))] = [255,0,255]
    return img

if __name__ == '__main__':
	main()