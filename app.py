import streamlit as st
import pandas as pd
import pickle

# ---------- PAGE ----------
st.set_page_config(layout="wide")

# ---------- MODEL ----------
model = pickle.load(open("model.pkl","rb"))

# ---------- LOGIN SESSION ----------
if "login" not in st.session_state:
    st.session_state.login=False


# ====================================================
# LOGIN PAGE
# ====================================================

if not st.session_state.login:

    st.markdown("""

<style>

header,footer {visibility:hidden;}
#MainMenu {visibility:hidden;}

.stApp{

background:

linear-gradient(rgba(0,0,0,.75),
rgba(0,0,0,.85)),

url("https://images.unsplash.com/photo-1580281657527-47f249e0bfc4?auto=format&fit=crop&w=2000&q=80");

background-size:cover;
background-position:center;
}


.login-box{

background:rgba(255,255,255,.12);

backdrop-filter:blur(20px);

padding:35px;

border-radius:18px;

box-shadow:0 15px 45px rgba(0,0,0,.7);

text-align:center;

color:white;

}

div.stButton > button{

width:100%;

padding:12px;

border-radius:12px;

background:

linear-gradient(45deg,#00c6ff,#0072ff);

color:white;

font-weight:600;

border:none;

}

</style>

""",unsafe_allow_html=True)


    # CENTER LOGIN CARD
    col1,col2,col3=st.columns([2,1,2])

    with col2:

        st.markdown('<div class="login-box">',
        unsafe_allow_html=True)

        st.image("assets/hospital.png",width=220)

        st.markdown("### ApexCare Medical Centre")

        user=st.text_input("Username")

        pwd=st.text_input("Password",
        type="password")

        if st.button("Login"):

            if user=="admin" and pwd=="1234":

                st.session_state.login=True

                st.rerun()

            else:

                st.error("Invalid Login")

        st.markdown("</div>",
        unsafe_allow_html=True)

    st.stop()


# ====================================================
# SIDEBAR MENU
# ====================================================

st.sidebar.image("assets/doctor.png",
width=90)

st.sidebar.write("Dr MohanKrishna")

page=st.sidebar.radio(

"Navigation",

["Dashboard",
"Diagnosis",
"Reports",
"Settings"]

)

# ====================================================
# DASHBOARD
# ====================================================

if page=="Dashboard":

    st.title("ApexCare Medical Centre Dashboard")

    st.markdown("""

<style>

.card{

padding:28px;

border-radius:18px;

text-align:center;

color:white;

box-shadow:0 10px 35px black;

}

.green{background:#16a34a;}

.red{background:#dc2626;}

.blue{background:#2563eb;}

.purple{background:#7c3aed;}

</style>

""",unsafe_allow_html=True)

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

    "Treatment":["Cardiac Monitoring",
    "Medication"]

    })

    st.dataframe(df,
    use_container_width=True)

    st.success(
    "Predict heart disease risk using AI Model from Diagnosis Page")


# ====================================================
# DIAGNOSIS
# ====================================================

elif page=="Diagnosis":

    st.title("❤️ Heart Disease Check")

    age=st.number_input("Age",1,100)

    bp=st.number_input("Blood Pressure",50,200)

    chol=st.number_input("Cholesterol",100,400)

    if st.button("Predict Heart Risk"):

        prediction=model.predict([[age,bp,chol]])[0]

        if prediction==1:

            st.error(
            "High Risk — Patient has higher chance of heart disease")

        else:

            st.success(
            "Low Risk — Patient condition looks stable")


# ====================================================
# REPORTS
# ====================================================

elif page=="Reports":

    st.title("Patient Treatment Reports")

    df=pd.DataFrame({

    "Name":["Ravi Kumar","Anita Devi",
    "Suresh Reddy","Meena Sharma",
    "Priya Nair"],

    "Age":[54,39,61,45,33],

    "Status":[
    "High Risk","Stable",
    "High Risk","Stable",
    "Stable"],

    "Treatment":[

    "Cardiac Monitoring",

    "Medication",

    "ICU Observation",

    "Regular Checkup",

    "Diet Monitoring"]

    })

    st.dataframe(df,
    use_container_width=True)


# ====================================================
# SETTINGS
# ====================================================

elif page=="Settings":

    st.title("Account Settings")

    st.subheader("Doctor Profile")

    st.text_input(
    "Doctor Name",
    "Dr MohanKrishna")

    st.text_input(
    "Email",
    "mohankrishna@email.com")

    st.text_input(
    "Hospital",
    "ApexCare Medical Centre")

    if st.button("Save Profile"):

        st.success("Profile Saved")

    st.subheader("Notification")

    st.checkbox("Email Alerts",True)

    st.checkbox("High Risk Patient Alerts",True)

    st.checkbox("Weekly Diagnosis Report")
