import streamlit as st
import pickle 
import helper


model = pickle.load(open('model.pkl','rb'))

st.header('Duplicate Statement\'s Detection')

q1 = st.text_input('Enter Statement 1')
q2 = st.text_input('Enter Statement 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.header('Same Statement')
    else:
        st.header('Different Statement')