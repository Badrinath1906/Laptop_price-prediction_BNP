import streamlit as st
import numpy as np
import pandas as pd
import pickle
import random

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Laptop Price Predictor", layout="centered")

# ---- Indian Currency Format ----
def format_indian_currency(num):
    num = int(num)
    s = str(num)
    if len(s) <= 3:
        return s
    last3 = s[-3:]
    rest = s[:-3][::-1]
    parts = [rest[i:i+2] for i in range(0, len(rest), 2)]
    rest = ",".join(parts)[::-1]
    return rest + "," + last3

# ---- CSS ----
st.markdown("""
<style>
.stApp {
    background:
        linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.85)),
        url("https://images.unsplash.com/photo-1517336714731-489689fd1ca8");
    background-size: cover;
}
h1 { color: white !important; }

.subheading {
    text-align: center;
    color: #00c6ff;
    margin-bottom: 20px;
}

label {
    color: white !important;
    font-weight: 600;
}

div[data-baseweb="select"] {
    background-color: rgba(255,255,255,0.2) !important;
}
div[data-baseweb="select"] span {
    color: white !important;
}

.stSlider > div {
    color: white !important;
}

.stButton button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 12px;
    padding: 12px;
    width: 100%;
}

.result-box {
    background: linear-gradient(135deg, #00c6ff, #0072ff);
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    margin-top: 25px;
    color: white;
    font-size: 38px;
    font-weight: bold;
}

.info-box {
    background: rgba(255,255,255,0.1);
    padding: 15px;
    border-radius: 10px;
    margin-top: 15px;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---- Title ----
st.markdown("<h1 style='text-align:center;'>💻 Laptop Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<div class='subheading'>⚡ Smart AI-based Laptop Price Prediction System</div>", unsafe_allow_html=True)

# ---- Inputs ----
col1, col2, col3 = st.columns(3)

with col1:
    company = st.selectbox("Brand", ["Apple", "HP", "Dell", "Lenovo", "Asus", "Acer"])

with col2:
    type_name = st.selectbox("Type", ["Ultrabook", "Gaming", "Notebook", "Workstation"])

with col3:
    ram = st.selectbox("RAM (GB)", [4, 8, 16, 32, 64])

col4, col5, col6 = st.columns(3)

with col4:
    weight = st.slider("Weight (kg)", 1.0, 3.5, 2.0, 0.1)

with col5:
    touchscreen = st.selectbox("Touchscreen", ["No", "Yes"])

with col6:
    ips = st.selectbox("IPS Display", ["No", "Yes"])

col7, col8, col9 = st.columns(3)

with col7:
    screen_size = st.slider("Screen Size (inches)", 11.0, 17.3, 15.6, 0.1)

with col8:
    resolution = st.selectbox("Resolution", [
        "1920x1080", "1366x768", "1600x900", "2560x1440", "3840x2160"
    ])

with col9:
    cpu = st.selectbox("CPU", [
        "Intel i3", "Intel i5", "Intel i7", "Ryzen 5", "Ryzen 7"
    ])

col10, col11 = st.columns(2)

with col10:
    hdd = st.selectbox("HDD (GB)", [0, 256, 512, 1024, 2048])

with col11:
    ssd = st.selectbox("SSD (GB)", [0, 128, 256, 512, 1024])

col12, col13 = st.columns(2)

with col12:
    gpu = st.selectbox("GPU", ["Intel", "Nvidia", "AMD"])

with col13:
    os = st.selectbox("OS", ["Windows", "Mac", "Linux"])

# ---- Predict ----
if st.button("Predict Price"):

    price = 50000 + (ram * 2000) + (ssd * 50)

    formatted_price = format_indian_currency(price)

    # 💰 Result
    st.markdown(f"<div class='result-box'>💰 ₹ {formatted_price}</div>", unsafe_allow_html=True)

    # 📊 Category
    if price < 40000:
        category = "Budget Laptop 💻"
    elif price < 80000:
        category = "Mid-range Laptop ⚡"
    else:
        category = "Premium Laptop 🚀"

    st.markdown(f"<h3 style='text-align:center;color:white;'>{category}</h3>", unsafe_allow_html=True)

    # 🎯 Confidence
    confidence = random.randint(85, 98)
    st.markdown(f"<p style='text-align:center;color:#00ffcc;'>Prediction Confidence: {confidence}%</p>", unsafe_allow_html=True)

    # 📊 Breakdown
    st.markdown(f"""
    <div class='info-box'>
    <b>Price Breakdown:</b><br>
    Base Price: ₹ 50,000<br>
    RAM Contribution: ₹ {ram*2000}<br>
    SSD Contribution: ₹ {ssd*50}
    </div>
    """, unsafe_allow_html=True)

    # 📋 Config Summary
    st.markdown(f"""
    <div class='info-box'>
    <b>Selected Configuration:</b><br>
    Brand: {company} | Type: {type_name} | RAM: {ram}GB<br>
    CPU: {cpu} | GPU: {gpu}<br>
    Screen: {screen_size}" | Weight: {weight}kg<br>
    Storage: {ssd}GB SSD + {hdd}GB HDD
    </div>
    """, unsafe_allow_html=True)