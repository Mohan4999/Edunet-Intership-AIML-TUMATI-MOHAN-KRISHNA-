import streamlit as st
import pandas as pd
import pickle
from PIL import Image

# ---------- PAGE ----------
st.set_page_config(layout="wide")

# ---------- LOAD MODEL ----------
model = pickle.load(open("model.pkl","rb"))

# ---------- IMAGES ----------
hospital_logo = Image.open("hospital.png")
doctor_img = Image.open("doctor.png")

# ---------- CSS ----------
st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background:
linear-gradient(rgba(5,20,30,.9),
rgba(5,20,30,.95)),
url("medical-bg.jpg");

background-size:cover;
color:white;
}

.topbar{
display:flex;
justify-content:space-between;
align-items:center;
background:#020617;
padding:15px 40px;
border-radius:12px;
}

.menu{
display:flex;
gap:20px;
}

.card{
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
""",unsafe_allow_html=True)


# ---------- LOGIN ----------
if "login" not in st.session_state:
    st.session_state.login=False

if not st.session_state.login:

    st.image(hospital_logo,width=300)

    st.markdown("## ApexCare Medical Centre")

    user = st.text_input("Username")
    pwd = st.text_input("Password",type="password")

    if st.button("Login"):

        if user=="admin" and pwd=="1234":

            st.session_state.login=True
            st.rerun()

        else:
            st.error("Invalid Login")

    st.stop()


# ---------- NAV ----------
menu = st.sidebar.radio(

"Navigation",

["Dashboard",
"Diagnosis",
"Reports",
"Settings"]

)

st.sidebar.image(doctor_img,width=80)

st.sidebar.write("Dr MohanKrishna")


# ---------- DASHBOARD ----------
if menu=="Dashboard":

    st.title("ApexCare Medical Centre")

    c1,c2,c3,c4=st.columns(4)

    c1.markdown(
    '<div class="card green">Cases Solved<h2>150</h2></div>',
    unsafe_allow_html=True)

    c2.markdown(
    '<div class="card red">High Risk<h2>45</h2></div>',
    unsafe_allow_html=True)

    c3.markdown(
    '<div class="card blue">Stable Patients<h2>105</h2></div>',
    unsafe_allow_html=True)

    c4.markdown(
    '<div class="card purple">Total Patients<h2>150</h2></div>',
    unsafe_allow_html=True)


    st.subheader("Recent Patients")

    df=pd.DataFrame({

    "Name":["Ravi Kumar","Anita Devi"],
    "Age":[54,39],
    "Status":["High Risk","Stable"],
    "Treatment":["Cardiac Monitoring","Medication"]

    })

    st.dataframe(df,use_container_width=True)

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#00c6ff,#0047ff);
    padding:30px;
    border-radius:20px;
    text-align:center;
    margin-top:20px;
    ">
    <h3>Medical Diagnosis</h3>
    Predict heart disease risk using AI Model
    </div>
    """,unsafe_allow_html=True)


# ---------- DIAGNOSIS ----------
elif menu=="Diagnosis":

    st.title("❤️ Heart Disease Check")

    age=st.number_input("Age",1,100)
    bp=st.number_input("Blood Pressure",50,200)
    chol=st.number_input("Cholesterol",100,400)

    if st.button("Predict Heart Risk"):

        pred=model.predict([[age,bp,chol]])[0]

        if pred==1:

            st.markdown("""
            <div class="result-risk">

            <h3>High Risk</h3>

            Patient has higher chance of heart disease.

            </div>

            """,unsafe_allow_html=True)

        else:

            st.markdown("""
            <div class="result-safe">

            <h3>Low Risk</h3>

            Patient condition looks stable.

            </div>

            """,unsafe_allow_html=True)



# ---------- REPORTS ----------
elif menu=="Reports":

    st.title("Patient Treatment Reports")

    df=pd.DataFrame({

    "Name":["Ravi Kumar","Anita Devi",
    "Suresh Reddy","Meena Sharma","Priya Nair"],

    "Age":[54,39,61,45,33],

    "Status":["High Risk","Stable",
    "High Risk","Stable","Stable"],

    "Treatment":[

    "Cardiac Monitoring",
    "Medication",
    "ICU Observation",
    "Regular Checkup",
    "Diet Monitoring"]

    })

    st.dataframe(df,use_container_width=True)



# ---------- SETTINGS ----------
elif menu=="Settings":

    st.title("Account Settings")

    name=st.text_input(
    "Doctor Name",
    "Dr MohanKrishna")

    email=st.text_input(
    "Email",
    "mohankrishna@email.com")

    hospital=st.text_input(
    "Hospital",
    "ApexCare Medical Centre")

    if st.button("Save Profile"):

        st.success("Saved Successfully")

    st.checkbox("Email Alerts",True)

    st.checkbox("High Risk Patient Alerts",True)

    st.checkbox("Weekly Diagnosis Report")