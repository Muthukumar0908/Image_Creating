import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}
st.title("Create Image:")
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
prompt=st.text_input("enter the sentance")
if st.button('enter'):
    image_bytes = query({
	"inputs": prompt,
    })
    # You can access the image with PIL.Image for example
    import io
    from PIL import Image
    images =Image.open(io.BytesIO(image_bytes))
    st.image(images)