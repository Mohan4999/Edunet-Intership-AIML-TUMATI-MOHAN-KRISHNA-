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

    /* Hide Streamlit Menu */
    header, footer {{visibility:hidden;}}
    #MainMenu {{visibility:hidden;}}

    /* Labels */
    label {{
        color:white !important;
        font-weight:600 !important;
        background:rgba(0,0,0,0.4);
        padding:3px 8px;
        border-radius:6px;
        display:inline-block;
    }}

    input::placeholder {{
        color:#cccccc;
    }}

    /* Full Background */
    .stApp {{
        background:
        linear-gradient(rgba(0,0,0,.65),
        rgba(0,0,0,.75)),
        url("data:image/jpg;base64,{bg}");
        background-size:cover;
        background-position:center;
        background-repeat:no-repeat;
    }}

    /* Page spacing */
    .block-container {{
        padding-top:120px;
        max-width:100%;
    }}

    /* Login Card Center */
    section.main > div > div > div > div:nth-child(2) {{
        background:rgba(0,0,0,.55);
        backdrop-filter:blur(18px);
        padding:35px;
        border-radius:18px;
        width:350px;
        margin:auto;
        box-shadow:0 30px 60px rgba(0,0,0,.8);
        text-align:center;
    }}

    /* Input Box */
    div[data-baseweb="input"] > div {{
        border-radius:12px;
    }}

    /* Login Button */
    div.stButton > button {{
        width:100%;
        padding:12px;
        border-radius:12px;
        background:linear-gradient(90deg,#00c6ff,#0072ff);
        color:white;
        font-weight:600;
        border:none;
        margin-top:10px;
    }}

    /* Logo Center + Bigger */
.logo-box {{
    display:flex;
    justify-content:center;
    align-items:center;
    margin-bottom:15px;
}}

.login-logo {{
    width:160px;      /* increase size here */
    border-radius:15px;
}}

    </style>
    """, unsafe_allow_html=True)
st.markdown("""
<h1 style='text-align:center;
           color:white;
           font-weight:700;
           margin-bottom:25px;'>
ApexCare Medical Centre
</h1>
""", unsafe_allow_html=True)
    # Center layout
    left, center, right = st.columns([3,2,3])

    with center:
        st.markdown(f"""
        <div class="logo-box">
        <img src="data:image/png;base64,{logo}" class="login-logo">
        </div>
        """, unsafe_allow_html=True)
        st.markdown(
            "<h2 style='text-align:center;color:white;'>ApexCare Medical Centre</h2>",
            unsafe_allow_html=True
        )
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == "admin" and password == "1234":
                st.success("Login Successful")
            else:
                st.error("Invalid Login")

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





















