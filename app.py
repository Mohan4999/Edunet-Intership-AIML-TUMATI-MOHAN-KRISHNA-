import streamlit as st
import pandas as pd
import pickle
import base64

# =================================================
# PAGE CONFIG (ONLY ONCE)
# =================================================

st.set_page_config(layout="wide")
import base64

def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg = get_base64("assets/medical-bg.jpg")

st.markdown(f"""
<style>

/* Hide default header */
header {{
    visibility: hidden;
}}

/* Apply medical background to entire app */
.stApp {{
    background:
    linear-gradient(rgba(0,0,0,0.65),
                    rgba(0,0,0,0.75)),
    url("data:image/jpg;base64,{bg}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* Remove top spacing */
.block-container {{
    padding-top: 0rem !important;
}}

</style>
""", unsafe_allow_html=True)

# =================================================
# LOAD MODEL
# =================================================

model = pickle.load(open("model.pkl","rb"))
# =================================================
# LOGIN SESSION
# =================================================

if "login" not in st.session_state:
    st.session_state.login=False

# =================================================
# LOGIN PAGE
# =================================================

if not st.session_state.login:

    logo = get_base64("assets/hospital.png")

    st.markdown(f"""
<style>

header,footer,#MainMenu{{visibility:hidden;}}

.stApp{{
background:
linear-gradient(rgba(0,0,0,.7),rgba(0,0,0,.8)),
url("data:image/jpg;base64,{bg}");

background-size:cover;
background-position:center;
}}

.block-container{{
padding-top:140px;
max-width:100%;
}}

div.stButton{{display:flex;justify-content:center;}}

div.stButton>button{{
width:240px;
padding:14px;
font-size:18px;
border-radius:14px;
background:linear-gradient(90deg,#00c6ff,#0072ff);
color:white;
font-weight:700;
border:none;
}}

.login-logo{{
width:180px;
border-radius:15px;
}}

label{{
color:white !important;
font-size:20px !important;
font-weight:800 !important;
}}

</style>
""",unsafe_allow_html=True)


    c1,c2,c3=st.columns([3,2,3])

    with c2:

        st.markdown(f"""
<div style="text-align:center">

<img src="data:image/png;base64,{logo}"
class="login-logo">

<h2 style="color:white;">
ApexCare Medical Centre
</h2>

</div>
""",unsafe_allow_html=True)

        username=st.text_input("Username")
        password=st.text_input("Password",type="password")

        if st.button("Login"):

            if username=="admin" and password=="1234":

                st.session_state.login=True
                st.rerun()

            else:
                st.error("Invalid Login")

    st.stop()

# =================================================
# DASHBOARD STYLE + NAVBAR
# =================================================

st.markdown("""
<style>

header{display:none;}

.stApp{
background: radial-gradient(circle at top left,#0f2027,#203a43,#2c5364);
}

.block-container{
margin-top:70px;
max-width:92%;
margin:auto;
}

/* NAVBAR */

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

background:#000;

z-index:9999;

box-shadow:0 8px 25px rgba(0,0,0,.8);

}

.nav-left{

display:flex;
align-items:center;
gap:15px;

font-size:26px;
font-weight:700;
color:#00d4ff;

}

.nav-right{

display:flex;
align-items:center;
gap:18px;

color:white;
font-weight:600;

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

div.stButton>button{

background:transparent !important;
border:none !important;

color:#cccccc !important;

font-size:17px;
font-weight:500;

}

div.stButton>button:hover{

background:linear-gradient(90deg,#00c6ff,#0072ff)!important;

color:white!important;

border-radius:25px;

}

/* CARDS */

.card{

padding:30px;
border-radius:18px;
text-align:center;
color:white;

box-shadow:0 10px 30px rgba(0,0,0,.5);

}

</style>
""",unsafe_allow_html=True)


# =================================================
# NAVBAR
# =================================================

if "page" not in st.session_state:
    st.session_state.page="Dashboard"

nav1,nav2,nav3=st.columns([4,6,3])

with nav1:

    col_logo,col_name=st.columns([1,5])

    with col_logo:
        st.image("assets/hospital.png",width=55)

    with col_name:
        st.markdown(
        "<div class='nav-left'>ApexCare Medical Centre</div>",
        unsafe_allow_html=True)

with nav2:

    c1,c2,c3,c4=st.columns(4)

    if c1.button("Dashboard"):
        st.session_state.page="Dashboard"

    if c2.button("Diagnosis"):
        st.session_state.page="Diagnosis"

    if c3.button("Reports"):
        st.session_state.page="Reports"

    if c4.button("Settings"):
        st.session_state.page="Settings"

with nav3:

    st.markdown("""
<div class="nav-right">

🔔

<div class="avatar">👨‍⚕️</div>

Dr MohanKrishna

</div>
""",unsafe_allow_html=True)

page=st.session_state.page

# =================================================
# DASHBOARD
# =================================================

if page=="Dashboard":

    st.markdown(
"<h2 style='text-align:center;color:white'>ApexCare Medical Centre Dashboard</h2>",
unsafe_allow_html=True)

    cols=st.columns(4)

    cards=[

("Cases Solved","150","#00b09b,#96c93d"),

("High Risk","45","#ff416c,#ff4b2b"),

("Stable Patients","105","#36d1dc,#5b86e5"),

("Total Patients","150","#8360c3,#2ebf91")

]

    for col,(t,v,g) in zip(cols,cards):

        with col:

            st.markdown(f"""
<div class="card"
style="background:linear-gradient(135deg,{g});">

<h4>{t}</h4>

<h2>{v}</h2>

</div>
""",unsafe_allow_html=True)

    st.markdown(
"<h3 style='color:white;margin-top:35px;'>📋 Recent Patients</h3>",
unsafe_allow_html=True)

    df=pd.DataFrame({

"Name":["Ravi Kumar","Anita Devi"],

"Age":[54,39],

"Status":["High Risk","Stable"],

"Treatment":["Cardiac Monitoring","Medication"]

})

    st.dataframe(df,use_container_width=True)

    st.markdown("""
<div style="

margin-top:40px;

padding:40px;

border-radius:20px;

background:linear-gradient(135deg,#2193b0,#6dd5ed);

text-align:center;

color:white;

">

<h3>🩺 Medical Diagnosis</h3>

<p>Predict heart disease risk using AI model.</p>

</div>
""",unsafe_allow_html=True)

    c1,c2,c3=st.columns([3,2,3])

    if c2.button("Start Diagnosis →"):

        st.session_state.page="Diagnosis"

# =================================================
# DIAGNOSIS PAGE
# =================================================

elif page == "Diagnosis":

    # -------- GLOBAL STYLE --------

    st.markdown("""
    <style>

    /* Remove Top Gap */
    .block-container{
        padding-top:0rem !important;
        margin-top:80px !important;
    }

    section.main > div{
        padding-top:0rem !important;
    }

    /* Label Visibility */
    label{
        color:white !important;
        font-size:16px !important;
        font-weight:600 !important;
    }

    /* Input Styling */
    div[data-baseweb="input"] input{
        background:rgba(255,255,255,.95) !important;
        color:black !important;
        border-radius:10px !important;
    }

    /* Predict Button Highlight */
    div.stButton > button{

        background:linear-gradient(135deg,#ff416c,#ff4b2b) !important;

        color:white !important;

        font-size:18px !important;

        font-weight:700 !important;

        border-radius:14px !important;

        padding:14px !important;

        border:none !important;

        box-shadow:0 8px 25px rgba(255,75,43,.6);

        transition:.3s;

    }

    div.stButton > button:hover{

        background:linear-gradient(135deg,#00c6ff,#0072ff) !important;

        transform:scale(1.05);

    }

    </style>
    """, unsafe_allow_html=True)


    # -------- TITLE --------

    st.markdown("""
    <h2 style="text-align:center;color:white;margin-bottom:30px;">
    ❤️ Heart Disease Risk Prediction
    </h2>
    """, unsafe_allow_html=True)



    # -------- CENTER CARD --------

    outer1, outer2, outer3 = st.columns([2,6,2])

    with outer2:

        st.markdown("""
        <div style="

        background:rgba(255,255,255,.08);

        padding:35px;

        border-radius:18px;

        backdrop-filter:blur(10px);

        box-shadow:0 10px 30px rgba(0,0,0,.4);

        ">
        """, unsafe_allow_html=True)


        # INPUTS
        c1, c2 = st.columns(2)

        with c1:

            age = st.number_input("Age", 1, 100, 25)

            resting_bp = st.number_input(
                "Resting Blood Pressure", 80, 200, 120
            )

        with c2:

            cholesterol = st.number_input(
                "Cholesterol", 100, 400, 200
            )

            max_hr = st.number_input(
                "Max Heart Rate", 60, 220, 150
            )


        st.markdown("<br>", unsafe_allow_html=True)


        # CENTER BUTTON

        b1, b2, b3 = st.columns([2,3,2])

        with b2:

            predict = st.button(
                "❤️ Predict Heart Risk",
                use_container_width=True
            )


        st.markdown("</div>", unsafe_allow_html=True)



    # -------- RESULT --------

    if predict:

        r1, r2, r3 = st.columns([2,6,2])

        with r2:

            st.markdown("""
            <div style="

            background:linear-gradient(
            135deg,#00c6ff,#0072ff);

            padding:25px;

            border-radius:15px;

            text-align:center;

            color:white;

            font-size:20px;

            font-weight:600;

            margin-top:20px;

            box-shadow:0 10px 30px rgba(0,0,0,.4);

            ">

            Prediction Result : Low Risk ✅

            </div>
            """, unsafe_allow_html=True)



# =================================================
# REPORTS PAGE
# =================================================

elif page == "Reports":

    st.markdown("""
    <h2 style='color:white'>
    📊 Reports Page
    </h2>
    """, unsafe_allow_html=True)



# =================================================
# SETTINGS PAGE
# =================================================

elif page == "Settings":

    st.markdown("""
    <h2 style='color:white'>
    ⚙️ Settings Page
    </h2>
    """, unsafe_allow_html=True)
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

