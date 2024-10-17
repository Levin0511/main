import streamlit as st

#seamlit cant press button run , only can run in shell
#streamlit run[file_name].pu

#set the app title
st.title('My first streamlit app')

st.write('Welcome to my first streamlit app')

#Display a btn
st.button('Reset', type="primary")
if st.button("Say hello"):
  st.write("Why hello dernis")
else:
  st.write("Goodbye")
  