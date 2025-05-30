import streamlit as st
from gtts import gTTS
import os

st.title("🎙️ Arabic Text-to-Speech App")

# Input text
text = st.text_area("أدخل جملة باللغة العربية", "مرحباً بكم في هذا المشروع الصوتي.")

# On button click
if st.button("🔊 توليد الصوت"):
    if text.strip():
        tts = gTTS(text, lang='ar')
        tts.save("output.mp3")
        st.audio("output.mp3", format="audio/mp3")
    else:
        st.warning("الرجاء إدخال نص أولاً.")
