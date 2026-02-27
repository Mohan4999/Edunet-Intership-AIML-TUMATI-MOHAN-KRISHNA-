from flask import request
from flask import Flask,render_template,request,redirect,url_for,session

app=Flask(__name__)

app.secret_key="medicalai"



# LOGIN

@app.route("/",methods=["GET","POST"])

def login():

    if request.method=="POST":

        user=request.form["username"]
        pwd=request.form["password"]

        if user=="admin@123" and pwd=="admin1234":

            session["user"]=user

            return redirect("/dashboard")

        else:

            return render_template(
            "login.html",
            error="Invalid Login"
            )

    return render_template("login.html")



# LOGIN CHECK

def check_login():

    if "user" not in session:

        return False

    return True



# DASHBOARD

@app.route("/dashboard")

def dashboard():

    return render_template(

        "dashboard.html",

        cases_solved=150,

        high_risk=45,

        stable=105,

        total=150

    )
# DIAGNOSIS

@app.route("/diagnosis")

def diagnosis():

    notes=[

    "New Patient Report Added",

    "AI Model Updated"

    ]

    return render_template(

    "diagnosis.html",

    notifications=notes,

    request=request

    )
#Predict

@app.route("/predict",methods=["POST"])

def predict():

    age=int(request.form["age"])

    bp=int(request.form["bp"])

    chol=int(request.form["chol"])


    # SIMPLE DEMO AI LOGIC

    if age>50 or bp>140 or chol>240:

        result="High Risk"

        message="Patient has higher chance of heart disease."

    else:

        result="Low Risk"

        message="Patient condition looks stable."


    notes=[

    "New Diagnosis Completed"

    ]


    return render_template(

    "diagnosis.html",

    result=result,

    message=message,

    notifications=notes,

    request=request

    )
# REPORTS

@app.route("/reports")

def reports():

    notes=[

    "New Patient Report Added",

    "AI Model Updated"

    ]

    return render_template(

    "reports.html",

    notifications=notes,

    request=request

    )
# SETTINGS

@app.route("/settings")

def settings():

    notes=[

    "New Patient Report Added",

    "AI Model Updated"

    ]

    return render_template(

    "settings.html",

    notifications=notes,

    request=request

    )

#Notifications

@app.route("/notifications")

def notifications():

    notes=[

    "New Patient Report Added",

    "AI Model Updated Successfully",

    "3 High Risk Predictions Today",

    "Password Changed Successfully"

    ]

    return render_template(

        "notifications.html",

        notes=notes,

        notifications=notes,

        request=request

    )
# LOGOUT

@app.route("/logout")

def logout():

    session.clear()

    return redirect("/")

app.run(debug=True)
if __name__ == "__main__":
    app.run()