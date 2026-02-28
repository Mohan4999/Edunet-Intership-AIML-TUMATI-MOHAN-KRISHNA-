import streamlit as st
import pandas as pd
import pickle
import base64
import os
from PIL import Image

st.set_page_config(layout="wide")

# ---------- LOAD IMAGE ----------
def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg = get_base64("assets/medical-bg.jpg")
    
# ---------------- PAGE ----------------
st.set_page_config(layout="wide")

model = pickle.load(open("model.pkl","rb"))

st.set_page_config(layout="wide")

if "login" not in st.session_state:
    st.session_state.login = False

# =================================================
# LOGIN PAGE
# =================================================

if not st.session_state.login:

    logo = get_base64("assets/hospital.png")

    st.markdown(f"""
    <style>
    header, footer {{visibility:hidden;}}
    #MainMenu {{visibility:hidden;}}

    .stApp {{
        background:
        linear-gradient(rgba(0,0,0,.65),
        rgba(0,0,0,.75)),
        url("data:image/jpg;base64,{bg}");
        background-size:cover;
        background-position:center;
        background-repeat:no-repeat;
    }}

    .block-container {{
        padding-top:120px;
        max-width:100%;
    }}

    div[data-baseweb="input"] > div {{
        border-radius:12px;
    }}

/* PERFECT CENTER LOGIN BUTTON */

div.stButton {{
    display:flex;
    justify-content:center;
    align-items:center;
}}

div.stButton > button {{
    width:240px;
    padding:14px 0;
    font-size:18px;
    border-radius:14px;
    background:linear-gradient(90deg,#00c6ff,#0072ff);
    color:white;
    font-weight:600;
    border:none;
    margin-top:20px;
}}
/* Hover Effect */
div.stButton > button:hover {{
    transform:scale(1.05);
    box-shadow:0 8px 20px rgba(0,114,255,0.6);
}}

    .logo-box {{
        display:flex;
        justify-content:center;
        margin-bottom:15px;
    }}

    .login-logo {{
        width:180px;
        border-radius:15px;
    }}
    /* Improve label visibility */
/* Clean Label Styling */
label {{
    color: white !important;
    font-size: 20px !important;   /* Bigger text */
    font-weight: 800 !important;
    background: none !important;  /* REMOVE black box */
    padding: 0 !important;
}}
    /* Input field styling */
div[data-baseweb="input"] input {{
    background-color: rgba(255,255,255,0.95) !important;
    color: black !important;
    font-size: 16px !important;
    font-weight: 500;
    border-radius: 12px !important;
}}
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([3,2,3])

    with col2:
        st.markdown(f"""
        <div class="logo-box">
            <img src="data:assets/hospital.png;base64,{logo}" class="login-logo">
        </div>
        """, unsafe_allow_html=True)
        st.markdown(
            "<h2 style='text-align:center;color:white;font-weight:600;margin-bottom:20px;'>ApexCare Medical Centre</h2>",
            unsafe_allow_html=True
        )

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login", key="login_btn"):
            col1, col2, col3 = st.columns([2,2,2])
            with col2:
                    if username == "admin" and password == "1234":
                        st.session_state.login = True
                        st.rerun()
                    else:
                        st.error("Invalid Login")
        st.stop()
# =================================================
# DASHBOARD PAGE
# =================================================
import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(layout="wide")

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"


# ---------------- GLOBAL STYLE ----------------
/* REMOVE STREAMLIT HEADER + SPACE */
header{
display:none !important;
height:0px !important;
}

/* REMOVE DEFAULT TOP GAP */
section.main > div{
padding-top:0rem !important;
}

/* APP BACKGROUND */

.stApp{
background: radial-gradient(circle at top left,#0f2027,#203a43,#2c5364);
}

/* Push content below navbar */
.block-container{
margin-top:70px !important;   /* navbar height match */
padding-top:0rem !important;
max-width:92%;
margin-left:auto;
margin-right:auto;

}

/* -------- NAVBAR -------- */

.navbar{
position:fixed;
top:0;
left:0;
height:70px;
width:100%;
display:flex;
justify-content:space-between;
align-items:center;
padding:0px 60px;
background:#000000;
z-index:9999;
box-shadow:0 8px 25px rgba(0,0,0,.8);
}
/* Logo Name */

.nav-left{

display:flex;
align-items:center;
gap:15px;
font-size:26px;
font-weight:700;
color:#00d4ff;
}

/* Right Profile */

.nav-right{

display:flex;
align-items:center;
gap:18px;

font-size:16px;
font-weight:600;

color:white;

}

.avatar{

width:42px;
height:42px;

border-radius:50%;

background:linear-gradient(135deg,#00c6ff,#0072ff);

display:flex;
align-items:center;
justify-content:center;

}

/* NAV BUTTONS */

div.stButton > button{

background:transparent !important;
border:none !important;

color:#cccccc !important;

font-size:17px;
font-weight:500;

padding:8px 18px;

border-radius:25px;

}

div.stButton > button:hover{

background:linear-gradient(90deg,#00c6ff,#0072ff) !important;

color:white !important;

}

/* Cards */

.card{

padding:30px;

border-radius:18px;

text-align:center;

color:white;

box-shadow:0 10px 30px rgba(0,0,0,.5);

}

</style>
""",unsafe_allow_html=True)


# ---------------- NAVBAR ----------------

nav1,nav2,nav3 = st.columns([4,6,3])

# LEFT (LOGO + NAME)
with nav1:

    col_logo,col_name = st.columns([1,5])

    with col_logo:

        # Works in Streamlit Cloud
        st.image("assets/hospital.png",width=55)

    with col_name:

        st.markdown(
        "<div class='nav-left'>ApexCare Medical Centre</div>",
        unsafe_allow_html=True)


# CENTER NAVIGATION
with nav2:

    c1,c2,c3,c4 = st.columns(4)

    with c1:
        if st.button("Dashboard"):
            st.session_state.page="Dashboard"

    with c2:
        if st.button("Diagnosis"):
            st.session_state.page="Diagnosis"

    with c3:
        if st.button("Reports"):
            st.session_state.page="Reports"

    with c4:
        if st.button("Settings"):
            st.session_state.page="Settings"


# RIGHT PROFILE
with nav3:

    st.markdown("""
    <div class="nav-right">
    🔔
    <div class="avatar">👨‍⚕️</div>
    Dr MohanKrishna
    </div>
    """,unsafe_allow_html=True)



# ---------------- CURRENT PAGE ----------------
page = st.session_state.page


# ===================================================
# DASHBOARD
# ===================================================

if page=="Dashboard":

    st.markdown(
    "<h2 style='text-align:center;color:white;'>ApexCare Medical Centre Dashboard</h2>",
    unsafe_allow_html=True)


    c1,c2,c3,c4 = st.columns(4)

    with c1:

        st.markdown("""
<div class="card" style="background:linear-gradient(135deg,#00b09b,#96c93d);">
<h4>Cases Solved</h4>
<h2>150</h2>
</div>
""",unsafe_allow_html=True)

    with c2:

        st.markdown("""
<div class="card" style="background:linear-gradient(135deg,#ff416c,#ff4b2b);">
<h4>High Risk</h4>
<h2>45</h2>
</div>
""",unsafe_allow_html=True)

    with c3:

        st.markdown("""
<div class="card" style="background:linear-gradient(135deg,#36d1dc,#5b86e5);">
<h4>Stable Patients</h4>
<h2>105</h2>
</div>
""",unsafe_allow_html=True)

    with c4:

        st.markdown("""
<div class="card" style="background:linear-gradient(135deg,#8360c3,#2ebf91);">
<h4>Total Patients</h4>
<h2>150</h2>
</div>
""",unsafe_allow_html=True)


    # -------- RECENT PATIENTS --------

    st.markdown(
    "<h3 style='color:white;margin-top:35px;'>📋 Recent Patients</h3>",
    unsafe_allow_html=True)


    df = pd.DataFrame({

    "Name":["Ravi Kumar","Anita Devi"],
    "Age":[54,39],
    "Status":["High Risk","Stable"],
    "Treatment":["Cardiac Monitoring","Medication"]

    })

    st.dataframe(df,use_container_width=True)


    # -------- DIAGNOSIS CARD --------

    st.markdown("""

<div style="
margin-top:40px;
padding:40px;
border-radius:20px;
background:linear-gradient(135deg,#2193b0,#6dd5ed);
text-align:center;
color:white;
box-shadow:0 10px 30px rgba(0,0,0,.4);
">

<h3>🩺 Medical Diagnosis</h3>

<p>Predict heart disease risk using AI model.</p>

</div>

""",unsafe_allow_html=True)



    # CENTER BUTTON
    col1,col2,col3 = st.columns([3,2,3])

    with col2:

        if st.button("Start Diagnosis →"):

            st.session_state.page="Diagnosis"
# =================================================
# DIAGNOSIS
# =================================================

elif page=="Diagnosis":

    st.title("❤️ Heart Disease Check")

    age=st.number_input("Age",1,100)

    bp=st.number_input("Blood Pressure",50,120)

    chol=st.number_input("Cholesterol",100,240)

    if st.button("Predict Heart Risk"):

        result=model.predict([[age,bp,chol]])[0]

        if result==1:

            st.error("High Risk")

        else:

            st.success("Low Risk")


# =================================================
# REPORTS
# =================================================

elif page=="Reports":

    st.title("Patient Treatment Reports")

    df=pd.DataFrame({

    "Name":["Ravi Kumar","Anita Devi",
    "Suresh Reddy","Meena Sharma","Priya Nair"],

    "Age":[54,39,61,45,33],

    "Status":[
    "High Risk","Stable",
    "High Risk","Stable","Stable"],

    "Treatment":[

    "Cardiac Monitoring",

    "Medication",

    "ICU Observation",

    "Regular Checkup",

    "Diet Monitoring"]

    })

    st.dataframe(df,
    use_container_width=True)


# =================================================
# SETTINGS
# =================================================

elif page=="Settings":

    st.title("Account Settings")

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

        st.success("Saved Successfully")

    st.checkbox("Email Alerts",True)

    st.checkbox("High Risk Alerts",True)

    st.checkbox("Weekly Report")









































































