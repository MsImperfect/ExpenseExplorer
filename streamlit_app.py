import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key = "AIzaSyAMUiuF6JdUAQm_msW7bqAX7cmrpDwAUoM")

model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input_text, image_data, prompt):
    response = model.generate_content([input_text, image_data[0], prompt])
    return response.text


def input_image_details(uploadede_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()  #retriving binary data from the image
        image_parts = [
            {
                "mime_type" : uploaded_file.type,
                "data" : bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file was uploaded")  #here we are raising file not found error and like we are going to display 'no file was uploaded'

st.set_page_config(page_title = "Invoice Generator")
st.sidebar.header("ExpenseExplorer")
#all the below lines are tp
st.sidebar.write("Made by CobraZZ")
st.sidebar.write("Powered by google gemini ai")
st.header("Expense Explorer ")
st.subheader("Manage your expenses with us")
#streamlit has cool and easy functions plZ check out
input = st.text_input("What do you want me to do?", key = "input")
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])  #used to upload files and type basically means what types are supported


image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "Uploaded Image", use_column_width = True)

submit = st.button("Let's Go")

#pls make your own promt and bro next time u use gemini make sure u call it expert(Devjams trauma)
input_prompt = """
You are an expert in reading invoices. We are going to upload an image of an invoices abd you will have to answer any type
of questions that the user asks you. You have to greet the user first. Make syre to keep the fonts uniform and the items list in a point wise format.
At the end, make sure to repeat the name of our appp "Expense Explorer" and ask the user to use it again.
"""

if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("Here's what you need to know")
    st.write(response)
