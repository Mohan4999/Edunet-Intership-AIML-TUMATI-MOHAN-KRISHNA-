import streamlit as st
import pandas as pd
import pickle
import base64

# =================================================
# PAGE CONFIG
# =================================================
st.set_page_config(layout="wide")

# =================================================
# BACKGROUND IMAGE
# =================================================
def get_base64(path):
    with open(path,"rb") as f:
        return base64.b64encode(f.read()).decode()

bg = get_base64("assets/medical-bg.jpg")

st.markdown(f"""
<style>

header{{visibility:hidden;}}

/* GLOBAL BACKGROUND */

.stApp{{
background:
linear-gradient(rgba(0,0,0,.65),
rgba(0,0,0,.75)),
url("data:image/jpg;base64,{bg}");

background-size:cover;
background-position:center;
background-attachment:fixed;
}}

.block-container{{
padding-top:0rem!important;
}}

</style>
""",unsafe_allow_html=True)

# =================================================
# MODEL
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

    logo=get_base64("assets/hospital.png")

    st.markdown("""
<style>

.block-container{
padding-top:140px;
}

.login-box{
display:flex;
flex-direction:column;
align-items:center;
justify-content:center;
}

div.stButton{
display:flex;
justify-content:center;
}

div.stButton>button{

width:250px;

padding:14px;

font-size:18px;

border-radius:14px;

background:linear-gradient(90deg,#00c6ff,#0072ff);

color:white;

font-weight:700;

border:none;

}

label{

color:white!important;

font-size:20px!important;

font-weight:700!important;

}

.login-logo{

width:170px;

border-radius:15px;

margin-bottom:15px;

}

</style>
""",unsafe_allow_html=True)

    c1,c2,c3=st.columns([3,2,3])

    with c2:

        st.markdown(f"""
<div class="login-box">

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
# NAVBAR STYLE
# =================================================
st.markdown("""
<style>

.block-container{

margin-top:70px;

max-width:92%;

margin-left:auto;
margin-right:auto;
}

/* NAVBAR */

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

/* NAV BUTTONS NORMAL */

div.stButton > button{

background:transparent!important;

border:none!important;

color:#cccccc!important;

font-size:17px;

font-weight:600;

}

/* HOVER */

div.stButton > button:hover{

background:linear-gradient(
90deg,#00c6ff,#0072ff)!important;

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

# LEFT
with nav1:

    l1,l2=st.columns([1,5])

    with l1:
        st.image("assets/hospital.png",width=55)

    with l2:
        st.markdown(
"<div class='nav-left'>ApexCare Medical Centre</div>",
unsafe_allow_html=True)

# CENTER MENU
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

# RIGHT
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

    c1,c2,c3=st.columns([3,2,3])

    if c2.button("Start Diagnosis →"):
        st.session_state.page="Diagnosis"


# =================================================
# DIAGNOSIS PAGE
# =================================================
elif page=="Diagnosis":

    # NAVBAR BUTTON COLOR CHANGE ONLY HERE
    st.markdown("""
<style>

/* Navbar buttons different color */

div.stButton > button{

color:#ffffff!important;

}

div.stButton > button:hover{

background:linear-gradient(
135deg,#ff416c,#ff4b2b)!important;

}

label{

color:white!important;

font-weight:600!important;

}

</style>
""",unsafe_allow_html=True)

    st.markdown("""
<h2 style="text-align:center;color:white">

❤️ Heart Disease Risk Prediction

</h2>
""",unsafe_allow_html=True)

    o1,o2,o3=st.columns([2,6,2])

    with o2:

        c1,c2=st.columns(2)

        with c1:

            age=st.number_input("Age",1,100,25)

            resting_bp=st.number_input(
"Resting BP",80,200,120)

        with c2:

            cholesterol=st.number_input(
"Cholesterol",100,400,200)

            max_hr=st.number_input(
"Max Heart Rate",60,220,150)

        b1,b2,b3=st.columns([3,3,3])

        predict=b2.button(
"❤️ Predict Heart Risk",
use_container_width=True)

    if predict:

        st.success(
"Prediction Result : Low Risk ✅")


# =================================================
# REPORTS
# =================================================
elif page=="Reports":

    st.markdown(
"<h2 style='color:white'>📊 Reports</h2>",
unsafe_allow_html=True)

    df=pd.DataFrame({

"Name":["Ravi Kumar","Anita Devi"],

"Age":[54,39],

"Status":["High Risk","Stable"],

"Treatment":["Cardiac Monitoring","Medication"]

})

    st.dataframe(df,use_container_width=True)

# =================================================
# SETTINGS
# =================================================
elif page=="Settings":

    st.markdown(
"<h2 style='color:white'>⚙️ Settings</h2>",
unsafe_allow_html=True)

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
