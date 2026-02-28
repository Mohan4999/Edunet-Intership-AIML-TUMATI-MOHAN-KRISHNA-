import streamlit as st
import pandas as pd
import pickle

# ---------------- PAGE ----------------
st.set_page_config(layout="wide")

model = pickle.load(open("model.pkl","rb"))

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

.stApp{

background:

linear-gradient(rgba(0,0,0,.75),
rgba(0,0,0,.85)),

url("https://images.unsplash.com/photo-1580281657527-47f249e0bfc4?auto=format&fit=crop&w=2000&q=80");

background-size:cover;
background-position:center;

}

/* remove spacing */

.block-container{

padding-top:120px;

}

/* LOGIN CARD */

.login-card{

background:rgba(255,255,255,.12);

backdrop-filter:blur(18px);

padding:35px;

border-radius:18px;

box-shadow:

0 15px 45px rgba(0,0,0,.7);

text-align:center;

color:white;

}


/* BUTTON */

div.stButton>button{

width:100%;

border-radius:12px;

padding:12px;

background:

linear-gradient(45deg,#00c6ff,#0072ff);

color:white;

font-weight:600;

border:none;

}

</style>

""",unsafe_allow_html=True)


    # CENTER CARD
    left,center,right=st.columns([3,2,3])

    with center:

        st.markdown('<div class="login-card">',
        unsafe_allow_html=True)

        st.image("assets/hospital.png",
        width=220)

        st.markdown(
        "<h3 style='text-align:center;'>ApexCare Medical Centre</h3>",
        unsafe_allow_html=True)

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
