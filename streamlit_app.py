import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from streamlit_extras.image_selector import image_selector
from streamlit_extras.image_selector import show_selection
from streamlit_image_coordinates import streamlit_image_coordinates
from streamlit_gsheets import GSheetsConnection

def example():
    "# Click on the image"
    last_coordinates = streamlit_image_coordinates( "https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"
    )


    st.write(last_coordinates)

example()

conn = st.connection ("gsheets", type=GSheetsConnection)
conn.read()
df=conn.read()
st.dataframe(df)