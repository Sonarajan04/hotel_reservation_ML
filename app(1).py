import streamlit as st
import joblib
#load the saved model
model=joblib.load('model.project')
#creating simple input
st.title('hotel reservation prediction')
arrival_year=st.slider('arrival year',2017,2018)
no_of_children=st.slider('no of children',0,10)
car_parking=st.slider('car parking',0,1)
no_of_weeknights=st.slider('weeknights',0,18)
no_of_weekendnights=st.slider('weekend nights',0,8)
room_type=st.slider('room type',0,7)
lead_time=st.slider('lead time',0,444)
market_segment=st.slider('market segment',0,4)
repeated_guest=st.slider('repeated guest',0,2)
previous_booking_not_cancelled=st.slider('previous booking not cancelled',0,60)
avg_price_per_room=st.slider('avg price per room',0,550,)
special_requests=st.slider('no of special request',0,5)
#make predictions
input=[[arrival_year,no_of_children,car_parking,no_of_weeknights,no_of_weekendnights,
        room_type,lead_time,market_segment,repeated_guest,previous_booking_not_cancelled,
        avg_price_per_room,special_requests]]
model=joblib.load('model.project')
if st.button('Predict'):
   pred=model.predict(input)
   st.write(f'Prediction:{pred}')
