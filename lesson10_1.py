import streamlit as st

if st.button("say Hello!",key="myButton"):
    st.write("wht hello there")
else:
    st.write("goodbye")