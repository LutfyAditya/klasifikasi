import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('mobil.sav', 'rb'))

st.title('Klasifikasi Penerimaan Mobil Bekas')

Buying_Price = st.number_input('Harga pertama beli mobil')
Maintenance_Price = st.number_input('Harga perbaikan mobil')
No_of_Doors = st.number_input('Jumlah pintu mobil')
Person_Capacity = st.number_input('Jumlah kursi mobil')
Size_of_Luggage = st.number_input('Ukuran bagasi mobil')
Safety = st.number_input('Tingkat keamanan mobil')

prediksi = ''
if st.button('Hasil Prediksi'):
    prediksi = model.predict([[Buying_Price, Maintenance_Price, No_of_Doors, Person_Capacity, Size_of_Luggage, Safety]])

    if (prediksi [0] == 0):
        prediksi = ('Kondisi mobil ini diterima')
    elif (prediksi  == 1):
        prediksi = ('Kondisi mobil ini dalam keadaan baik')
    elif (prediksi  == 2):
        prediksi = ('Kondisi mobil ini tidak diterima')
    else:
        prediksi = ('Kondisi mobil ini keadaannya sangat baik')
st.success(prediksi)