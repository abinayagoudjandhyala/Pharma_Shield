
import streamlit as st
from PIL import Image
from image_model import analyze_image

st.set_page_config(page_title="Fake Medicine Detector", layout="centered")
st.title("💊 Fake Medicine Detector")

st.markdown("Upload a **medicine image** to check if it's real or fake:")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    result, reason = analyze_image(image)

    if result == 1:
        st.error(f"❌ FAKE MEDICINE\n\n{reason}")
    else:
        st.success(f"✅ REAL MEDICINE\n\n{reason}")
else:
    st.info("Please upload an image to begin.")
