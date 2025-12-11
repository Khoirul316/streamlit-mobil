import pickle
import streamlit as st

model = pickle.load(open('prediksi_harga_mobil.sav', 'rb'))

st.title('Prediksi Harga Mobil Bekas')

year = st.number_input('Input tahun mobil')
mileage = st.number_input('Input km mobil')
tax = st.number_input('Input pajak mobil')
mpg = st.number_input('Input konsumsi BBM mobil')
engineSize = st.number_input('Input Engine Size')

predict = ''

if st.button('Prediksi Harga'):
    predict = model.predict([[year, mileage, tax, mpg, engineSize]])
    st.write('Prediksi harga mobil dalam Ponds: ', predict)
    st.write('Prediksi harga mobil dalam IDR (Juta) : ', predict*19000)
    
