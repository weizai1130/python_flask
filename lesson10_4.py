import streamlit as st

option = st.selectbox(
    "您想要如何聯絡?",
    ("Email","電話","手機")
)

if option == "Email":
    st.write("你選擇Email")
elif option == "電話":
    st.write("你選擇電話")
elif option == "手機":
    st.write("你選擇手機")