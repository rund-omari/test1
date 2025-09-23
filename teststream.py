

import streamlit as st

st.set_page_config(page_title="صوت وصورة", page_icon="🎵")


st.subheader("📷 ")
st.image(r"strawberry.png",)

st.subheader("🎵 ")
st.audio(r"wrong.mp3")

st.write("يمكنك رفع ملفاتك الخاصة بدلاً من الروابط 👇")

uploaded_img = st.file_uploader("ارفع صورة", type=["png", "jpg", "jpeg"])
if uploaded_img:
    st.image(uploaded_img, caption="الصورة المرفوعة")

uploaded_audio = st.file_uploader("ارفع ملف صوت", type=["mp3", "wav"])
if uploaded_audio:
    st.audio(uploaded_audio)


