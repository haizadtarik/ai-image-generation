import requests
from PIL import Image
from io import BytesIO
import base64
import logging as log
import streamlit as st
import sys

@st.cache
def generate_image(prompt, cli_args):
    if len(cli_args) > 1:
        base_url = sys.argv[1]
        response = requests.post(f'{base_url}/generate/{prompt}')
    else:
        response = requests.post(f'http://0.0.0.0:8080/generate/{prompt}')
    if response.ok:
        log.info('Image succesfully generated')
    else:
        log.error(f'Error: {response}')
    image_binary = BytesIO(base64.b64decode(response.json()['generated image']))
    return image_binary

if __name__ == "__main__":
    st.subheader('Image generation using Stable Diffusion v2.1')
    prompt = st.text_input('Enter your prompt here:')
    if prompt != '':
        binary_image = generate_image(prompt,sys.argv)
        st.image(Image.open(binary_image), width=500)
        st.download_button(label="Download",data=binary_image,file_name=f'{prompt}.jpeg',mime="image/png")
        
    