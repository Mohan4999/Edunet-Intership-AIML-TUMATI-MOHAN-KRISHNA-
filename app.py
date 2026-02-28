import streamlit as st
import pandas as pd

st.set_page_config(page_title="ApexCare Medical Centre", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.main {
    background-color: #0e1117;
    color: white;
}
.card {
    padding: 20px;
    border-radius: 12px;
    color: white;
    text-align: center;
    font-size: 20px;
}
.green { background-color: #00c853; }
.red { background-color: #d50000; }
.blue { background-color: #2962ff; }
.purple { background-color: #aa00ff; }

.big-button {
    background: linear-gradient(90deg,#00c6ff,#0072ff);
    padding: 10px;
    border-radius: 8px;
    text-align:center;
    color:white;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# ---------- LOGIN SYSTEM ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🏥 ApexCare Medical Centre")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid Credentials")

    st.stop()

# ---------- SIDEBAR ----------
st.sidebar.title("ApexCare")
page = st.sidebar.radio("Navigation", 
                        ["Dashboard", "Diagnosis", "Reports", "Settings"])

st.sidebar.write("👨‍⚕️ Dr MohanKrishna")

# ---------- DASHBOARD ----------
if page == "Dashboard":
    st.title("📊 Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('<div class="card green">Cases Solved<br><h2>150</h2></div>',
                    unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card red">High Risk<br><h2>45</h2></div>',
                    unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card blue">Stable Patients<br><h2>105</h2></div>',
                    unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="card purple">Total Patients<br><h2>150</h2></div>',
                    unsafe_allow_html=True)

    st.subheader("Recent Patients")

    data = {
        "Name": ["Ravi Kumar", "Anita Devi"],
        "Age": [54, 39],
        "Status": ["High Risk", "Stable"],
        "Treatment": ["Cardiac Monitoring", "Medication"]
    }

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

# ---------- DIAGNOSIS ----------
elif page == "Diagnosis":
    st.title("❤️ Heart Disease Check")
    st.write("Enter patient details")

    age = st.number_input("Age", 1, 100)
    bp = st.number_input("Blood Pressure", 50, 200)
    chol = st.number_input("Cholesterol Level", 100, 400)

    if st.button("Predict Heart Risk"):
        if age > 50 and bp > 130 and chol > 200:
            st.error("🔴 High Risk - Patient has higher chance of heart disease.")
        else:
            st.success("🟢 Low Risk - Patient condition looks stable.")

# ---------- REPORTS ----------
elif page == "Reports":
    st.title("📑 Patient Treatment Reports")

    data = {
        "Name": ["Ravi Kumar", "Anita Devi", "Suresh Reddy", "Meena Sharma", "Priya Nair"],
        "Age": [54, 39, 61, 45, 33],
        "Status": ["High Risk", "Stable", "High Risk", "Stable", "Stable"],
        "Treatment": ["Cardiac Monitoring", "Medication", "ICU Observation", 
                      "Regular Checkup", "Diet Monitoring"]
    }

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

# ---------- SETTINGS ----------
elif page == "Settings":
    st.title("⚙ Account Settings")

    st.subheader("Doctor Profile")
    name = st.text_input("Doctor Name", "Dr MohanKrishna")
    email = st.text_input("Email", "mohankrishna@email.com")
    hospital = st.text_input("Hospital Name", "ApexCare Medical Centre")

    if st.button("Save Profile"):
        st.success("Profile Saved Successfully")

    st.subheader("Notification Settings")
    st.checkbox("Email Alerts", value=True)
    st.checkbox("High Risk Patient Alerts", value=True)
    st.checkbox("Weekly Diagnosis Report")
