import streamlit as st

# ------------------------
# SESSION STATE INIT
# ------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ------------------------
# LOGIN PAGE
# ------------------------

def login_page():
    st.title("Medical AI Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "admin@123" and password == "admin1234":
            st.session_state.logged_in = True
            st.success("Login Successful")
            st.rerun()
        else:
            st.error("Invalid Login")


# ------------------------
# DASHBOARD
# ------------------------

def dashboard():
    st.title("Dashboard")

    st.metric("Cases Solved", 120)
    st.metric("High Risk", 45)
    st.metric("Stable", 75)


# ------------------------
# DIAGNOSIS
# ------------------------

def diagnosis():

    st.title("Heart Disease Prediction")

    age = st.number_input("Age", min_value=1, max_value=120)
    bp = st.number_input("Blood Pressure")
    chol = st.number_input("Cholesterol")

    if st.button("Predict"):

        if age > 50 or bp > 140 or chol > 240:
            st.error("High Risk - Patient has higher chance of heart disease.")
        else:
            st.success("Low Risk - Patient condition looks stable.")


# ------------------------
# REPORTS
# ------------------------

def reports():
    st.title("Reports")
    st.write("New Patient Report Added")
    st.write("AI Model Updated")


# ------------------------
# SETTINGS
# ------------------------

def settings():
    st.title("Settings")
    st.write("Update your system settings here.")


# ------------------------
# MAIN APP
# ------------------------

if not st.session_state.logged_in:
    login_page()
else:

    st.sidebar.title("Navigation")

    page = st.sidebar.radio(
        "Go to",
        ["Dashboard", "Diagnosis", "Reports", "Settings", "Logout"]
    )

    if page == "Dashboard":
        dashboard()

    elif page == "Diagnosis":
        diagnosis()

    elif page == "Reports":
        reports()

    elif page == "Settings":
        settings()

    elif page == "Logout":
        st.session_state.logged_in = False
        st.rerun()