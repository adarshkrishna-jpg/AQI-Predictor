import streamlit as st

import pickle
filename='aqi.pkl'
loaded_model=pickle.load(open(filename,'rb'))
filename='scalee.pkl'
loaded_scale=pickle.load(open(filename,'rb'))
st.write("AQI prediction")


PM10=st.number_input("enter PM10(Particular Matter<=10 microns)")
PM2_5=st.number_input("enter PM2.5(Particular Matter<=2.5 microns)")
NO2=st.number_input("enter NO2(Nitrogen Dioxide)")
SO2=st.number_input("enter S02(Sulphur Dioxide)")
CO=st.number_input("enter CO(Carbon Monoxide)")
O3=st.number_input("enter O3(Ozone)")
NH3=st.number_input("enter NH3(Ammonia)")
new=[[PM10,PM2_5,NO2,SO2,CO,O3,NH3]]


predicted_class=loaded_model.predict(loaded_scale.transform(new))
if st.button('predict'):
    st.write(predicted_class)
