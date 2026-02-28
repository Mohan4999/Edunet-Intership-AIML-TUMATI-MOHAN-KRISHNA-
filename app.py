import streamlit as st
import pandas as pd
import pickle
import base64

def get_base64(img_path):
    with open(img_path,"rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
bg = get_base64("assets/medical-bg")
    
# ---------------- PAGE ----------------
st.set_page_config(layout="wide")

model = pickle.load(open("model.pkl","rb"))

st.set_page_config(layout="wide")

if "login" not in st.session_state:
    st.session_state.login=False

# =================================================
# LOGIN PAGE
# =================================================

if not st.session_state.login:

    st.markdown("""

<style>

header, footer {visibility:hidden;}
#MainMenu {visibility:hidden;}


/* BACKGROUND IMAGE */

.stApp{

background:

linear-gradient(

rgba(0,0,0,.75),

rgba(0,0,0,.85)

),

url("assets/medical-bg");

background-size:cover;

background-position:center;

background-repeat:no-repeat;

}


/* REMOVE WHITE SPACE */

.block-container{

padding-top:140px;

max-width:100%;

}


/* LOGIN CARD */

div[data-testid="column"]:nth-child(2){

background:rgba(0,0,0,.55);

backdrop-filter:blur(15px);

padding:35px;

border-radius:18px;

box-shadow:

0 20px 60px rgba(0,0,0,.8);

text-align:center;

color:white;

}


/* LOGIN BUTTON */

div.stButton>button{

width:100%;

padding:14px;

border-radius:10px;

background:

linear-gradient(

90deg,

#00c6ff,

#0072ff

);

color:white;

font-weight:600;

border:none;

}

</style>

""",unsafe_allow_html=True)



    left,center,right = st.columns([3,1.4,3])

    with center:

        st.image("assets/hospital.png",width=200)

        st.markdown("### ApexCare Medical Centre")

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





