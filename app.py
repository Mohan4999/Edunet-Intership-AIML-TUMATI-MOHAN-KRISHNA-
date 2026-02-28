import streamlit as st
import pandas as pd
import pickle
import base64

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
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"
st.set_page_config(layout="wide")
if page == "Dashboard":

    # ALL YOUR DASHBOARD CODE HERE
# ---------- GLOBAL STYLE ----------

st.markdown("""
<style>

/* REMOVE SIDEBAR + HEADER */

[data-testid="stSidebar"]{display:none;}
header{visibility:hidden;}

.block-container{
padding-top:1rem;
max-width:95%;
margin:auto;
}


/* BACKGROUND */

.stApp{
background:linear-gradient(120deg,#0f2027,#203a43,#2c5364);
}


/* NAVBAR */

.navbar{
display:flex;
justify-content:space-between;
align-items:center;
padding:18px 40px;
background:rgba(0,0,0,.75);
border-radius:20px;
margin-bottom:40px;
color:white;
box-shadow:0px 8px 25px rgba(0,0,0,.5);
}

.nav-left{
font-weight:600;
font-size:18px;
}

.nav-center{
display:flex;
gap:35px;
}

.nav-center span{
padding:8px 18px;
border-radius:20px;
}

.active{
background:linear-gradient(90deg,#00c6ff,#0072ff);
}

.nav-right{
display:flex;
gap:15px;
align-items:center;
}

.avatar{
width:35px;
height:35px;
border-radius:50%;
background:linear-gradient(135deg,#00c6ff,#0072ff);
display:flex;
align-items:center;
justify-content:center;
}


/* TITLE */

.dashboard-title{
text-align:center;
color:white;
font-size:30px;
font-weight:700;
margin-bottom:25px;
}


/* CARDS */

.card{
padding:30px;
border-radius:18px;
text-align:center;
color:white;
font-weight:600;
box-shadow:0px 15px 35px rgba(0,0,0,.5);
}

.green{background:linear-gradient(135deg,#00b09b,#96c93d);}
.red{background:linear-gradient(135deg,#ff416c,#ff4b2b);}
.blue{background:linear-gradient(135deg,#36d1dc,#5b86e5);}
.purple{background:linear-gradient(135deg,#8360c3,#2ebf91);}


/* TABLE CARD */

.white-card{

background:white;
border-radius:20px;
padding:20px;
margin-top:30px;
box-shadow:0px 12px 30px rgba(0,0,0,.5);

}


/* DIAGNOSIS CARD */

.diag{

margin-top:50px;
padding:50px;
border-radius:20px;
background:linear-gradient(135deg,#2193b0,#6dd5ed);
text-align:center;
color:white;
box-shadow:0px 15px 40px rgba(0,0,0,.5);

}


/* CENTER BUTTON */

div.stButton{

display:flex;
justify-content:center;

}

div.stButton > button{

padding:14px 30px;
border-radius:10px;
background:white;
color:#2193b0;
font-weight:700;
border:none;

}

</style>
""", unsafe_allow_html=True)



# ---------- NAVBAR ----------

st.markdown("""
<div class="navbar">

<div class="nav-left">
🏥 ApexCare Medical Centre
</div>

<div class="nav-center">
<span class="active">Dashboard</span>
<span>Diagnosis</span>
<span>Reports</span>
<span>Settings</span>
</div>

<div class="nav-right">

🔔

<div class="avatar">👨‍⚕️</div>

Dr MohanKrishna

</div>

</div>
""", unsafe_allow_html=True)



# ---------- TITLE ----------

st.markdown(
'<div class="dashboard-title">ApexCare Medical Centre Dashboard</div>',
unsafe_allow_html=True)



# ---------- CARDS ----------

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.markdown("""
<div class="card green">
Cases Solved
<h2>150</h2>
</div>
""",unsafe_allow_html=True)


with c2:

    st.markdown("""
<div class="card red">
High Risk
<h2>45</h2>
</div>
""",unsafe_allow_html=True)


with c3:

    st.markdown("""
<div class="card blue">
Stable Patients
<h2>105</h2>
</div>
""",unsafe_allow_html=True)


with c4:

    st.markdown("""
<div class="card purple">
Total Patients
<h2>150</h2>
</div>
""",unsafe_allow_html=True)



# ---------- RECENT PATIENTS ----------

st.markdown('<div class="white-card">',unsafe_allow_html=True)

st.markdown("### 📋 Recent Patients")

df = pd.DataFrame({

"Name":["Ravi Kumar","Anita Devi"],
"Age":[54,39],
"Status":["High Risk","Stable"],
"Treatment":["Cardiac Monitoring","Medication"]

})

st.dataframe(df,use_container_width=True)

st.markdown('</div>',unsafe_allow_html=True)



# ---------- DIAGNOSIS ----------

st.markdown("""
<div class="diag">

<h3>🩺 Medical Diagnosis</h3>

<p>Predict heart disease risk using AI model.</p>

</div>
""", unsafe_allow_html=True)



# BUTTON CENTER INSIDE

col1,col2,col3 = st.columns([3,2,3])

with col2:

    if st.button("Start Diagnosis →", key="diag_btn"):

        st.success("Redirecting to Diagnosis Page...")
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















































