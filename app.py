import streamlit as st
import pandas as pd
import pickle
from PIL import Image
import os
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="ApexCare Medical Centre", layout="wide")

# ---------------- LOAD MODEL SAFELY ----------------
try:
    model = pickle.load(open("model.pkl", "rb"))
except:
    model = None

# ---------------- LOAD IMAGES SAFELY ----------------
def load_image(path):
    if os.path.exists(path):
        return Image.open(path)
    return None

hospital_logo = load_image("assets/hospital.png")
doctor_img = load_image("assets/doctor.png")

# ---------------- BACKGROUND FUNCTION ----------------
def set_background(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{data}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """, unsafe_allow_html=True)

set_background("assets/medical-bg.jpg")

# ---------------- GLOBAL CSS ----------------
st.markdown("""
<style>
.card {
    padding:25px;
    border-radius:18px;
    text-align:center;
    color:white;
    font-size:20px;
    box-shadow:0 10px 30px black;
}
.green{background:#16a34a;}
.red{background:#dc2626;}
.blue{background:#2563eb;}
.purple{background:#7c3aed;}

.result-risk{
background:#ffd6d6;
color:#b00020;
padding:20px;
border-radius:12px;
border-left:6px solid red;
}

.result-safe{
background:#d6ffe5;
color:#006b2c;
padding:20px;
border-radius:12px;
border-left:6px solid green;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
st.set_page_config(layout="wide")

if "login" not in st.session_state:
    st.session_state.login = False

# ---------------- LOGIN PAGE ----------------
if not st.session_state.login:

    st.markdown("""
    <style>

    /* Remove Streamlit default */
    header, footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}

    .stApp {
        background:
        linear-gradient(rgba(0,0,0,.75),
        rgba(0,0,0,.85)),
        url("https://images.unsplash.com/photo-1580281657527-47f249e0bfc4?auto=format&fit=crop&w=2000&q=80");
        background-size: cover;
        background-position: center;
    }

    /* Center container */
    .block-container {
        padding-top: 5rem;
    }

    .login-card {
        width: 380px;
        margin: auto;
        background: rgba(255,255,255,.12);
        backdrop-filter: blur(20px);
        padding: 35px;
        border-radius: 18px;
        box-shadow: 0 15px 45px rgba(0,0,0,.7);
        text-align: center;
        color: white;
    }

    .login-title {
        font-size: 22px;
        font-weight: 600;
        margin-bottom: 20px;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        padding: 12px;
        background: linear-gradient(45deg,#00c6ff,#0072ff);
        color: white;
        font-weight: 600;
        border: none;
    }

    div.stButton > button:hover {
        transform: scale(1.03);
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-card">', unsafe_allow_html=True)

    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Red_Cross.svg/120px-Red_Cross.svg.png", width=120)

    st.markdown('<div class="login-title">ApexCare Medical Centre</div>', unsafe_allow_html=True)

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if user == "admin" and pwd == "1234":
            st.session_state.login = True
            st.rerun()
        else:
            st.error("Invalid Login")

    st.markdown('</div>', unsafe_allow_html=True)

    st.stop()

# ---------------- SIDEBAR ----------------
menu = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Diagnosis", "Reports", "Settings"]
)

if doctor_img:
    st.sidebar.image(doctor_img, width=80)

st.sidebar.write("Dr MohanKrishna")

# ---------------- DASHBOARD ----------------
if menu == "Dashboard":

    st.title("🏥 ApexCare Medical Centre")

    c1, c2, c3, c4 = st.columns(4)

    c1.markdown('<div class="card green">Cases Solved<h2>150</h2></div>', unsafe_allow_html=True)
    c2.markdown('<div class="card red">High Risk<h2>45</h2></div>', unsafe_allow_html=True)
    c3.markdown('<div class="card blue">Stable Patients<h2>105</h2></div>', unsafe_allow_html=True)
    c4.markdown('<div class="card purple">Total Patients<h2>150</h2></div>', unsafe_allow_html=True)

    st.subheader("Recent Patients")

    df = pd.DataFrame({
        "Name": ["Ravi Kumar", "Anita Devi"],
        "Age": [54, 39],
        "Status": ["High Risk", "Stable"],
        "Treatment": ["Cardiac Monitoring", "Medication"]
    })

    st.dataframe(df, use_container_width=True)

# ---------------- DIAGNOSIS ----------------
elif menu == "Diagnosis":

    st.title("❤️ Heart Disease Check")

    age = st.number_input("Age", 1, 100)
    bp = st.number_input("Blood Pressure", 50, 200)
    chol = st.number_input("Cholesterol", 100, 400)

    if st.button("Predict Heart Risk"):

        if model is None:
            st.error("Model file not found. Please upload model.pkl")
        else:
            try:
                pred = model.predict([[age, bp, chol]])[0]

                if pred == 1:
                    st.markdown("""
                    <div class="result-risk">
                    <h3>High Risk</h3>
                    Patient has higher chance of heart disease.
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="result-safe">
                    <h3>Low Risk</h3>
                    Patient condition looks stable.
                    </div>
                    """, unsafe_allow_html=True)

            except:
                st.error("Prediction error. Check model format.")

# ---------------- REPORTS ----------------
elif menu == "Reports":

    st.title("Patient Treatment Reports")

    df = pd.DataFrame({
        "Name": ["Ravi Kumar","Anita Devi","Suresh Reddy","Meena Sharma","Priya Nair"],
        "Age": [54,39,61,45,33],
        "Status": ["High Risk","Stable","High Risk","Stable","Stable"],
        "Treatment": [
            "Cardiac Monitoring",
            "Medication",
            "ICU Observation",
            "Regular Checkup",
            "Diet Monitoring"
        ]
    })

    st.dataframe(df, use_container_width=True)

# ---------------- SETTINGS ----------------
elif menu == "Settings":

    st.title("Account Settings")

    name = st.text_input("Doctor Name", "Dr MohanKrishna")
    email = st.text_input("Email", "mohankrishna@email.com")
    hospital = st.text_input("Hospital", "ApexCare Medical Centre")

    if st.button("Save Profile"):
        st.success("Saved Successfully")

    st.checkbox("Email Alerts", True)
    st.checkbox("High Risk Patient Alerts", True)
    st.checkbox("Weekly Diagnosis Report")

