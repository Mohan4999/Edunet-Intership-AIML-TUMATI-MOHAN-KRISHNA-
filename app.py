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

    st.markdown(f"""
    <style>

    header, footer {{visibility:hidden;}}
    #MainMenu {{visibility:hidden;}}

    /* FULL BACKGROUND */
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

    /* CENTER CARD */
    .login-card {{
        background:rgba(0,0,0,.55);
        backdrop-filter:blur(15px);
        padding:35px 30px;
        border-radius:18px;
        width:320px;
        margin:auto;
        box-shadow:0 25px 60px rgba(0,0,0,.7);
        text-align:center;
    }}

    .login-title {{
        color:white;
        font-size:20px;
        font-weight:600;
        margin-top:10px;
        margin-bottom:20px;
    }}

    div[data-baseweb="input"] > div {{
        border-radius:10px !important;
    }}

    div.stButton > button {{
        width:100%;
        padding:12px;
        border-radius:10px;
        background:linear-gradient(90deg,#00c6ff,#0072ff);
        color:white;
        font-weight:600;
        border:none;
        margin-top:10px;
    }}

    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='login-card'>", unsafe_allow_html=True)

    st.image("assets/hospital.png", width=160)

    st.markdown("<div class='login-title'>ApexCare Medical Centre</div>",
                unsafe_allow_html=True)

    username = st.text_input("Username", label_visibility="collapsed")
    password = st.text_input("Password", type="password",
                             label_visibility="collapsed")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.success("Login Successful")
        else:
            st.error("Invalid Login")

    st.markdown("</div>", unsafe_allow_html=True)

    st.stop()
# =================================================
# SIDEBAR
# =================================================

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

# =================================================
# DASHBOARD
# =================================================

if page=="Dashboard":

    st.title("ApexCare Medical Centre Dashboard")

    col1,col2,col3,col4=st.columns(4)

    col1.success("Cases Solved\n\n150")

    col2.error("High Risk\n\n45")

    col3.info("Stable Patients\n\n105")

    col4.warning("Total Patients\n\n150")


    st.subheader("Recent Patients")

    df=pd.DataFrame({

    "Name":["Ravi Kumar","Anita Devi"],

    "Age":[54,39],

    "Status":["High Risk","Stable"],

    "Treatment":[
    "Cardiac Monitoring",
    "Medication"]

    })

    st.dataframe(df,
    use_container_width=True)


# =================================================
# DIAGNOSIS
# =================================================

elif page=="Diagnosis":

    st.title("❤️ Heart Disease Check")

    age=st.number_input("Age",1,100)

    bp=st.number_input("Blood Pressure",50,200)

    chol=st.number_input("Cholesterol",100,400)

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











