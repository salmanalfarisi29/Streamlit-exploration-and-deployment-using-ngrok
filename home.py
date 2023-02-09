import streamlit as st
from PIL import Image
def main():
    Original_Image = Image.open("imgs/Salman Alfarisi.jpg")
    img = Original_Image
    st.title("Praktikum 4 PENGOLAHAN CITRA DIGITAL")
    
    st.header("Profile")
    with st.container():
        col1, col2 = st.columns([9,3])
        with col1:
            st.write('Nama', 'SALMAN ALFARISI')
            st.write('NIM', '211511059')
            st.write('PROGRAM STUDI', 'D3 TEKNIK INFORMATIKA')
            st.write('KELAS', '2B')
        with col2:
            st.image(img)
if __name__ == '__main__':
	main()