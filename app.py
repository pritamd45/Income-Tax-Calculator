from flask import Flask, render_template, request, redirect, url_for,send_file,flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlalchemy

app = Flask(__name__)
app.secret_key = 'sdfadfsdgf'

# Hardcoded user credentials for learning purposes
users = {}

@app.route("/")
def index():
    return render_template("index.html")

#Sign page
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name=request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        if name in users:
            return "Username already exists"
        users[name] = generate_password_hash(password)
        return redirect(url_for("login"))

    return render_template("signup.html")

#signin page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        name = request.form["name"]
        password = request.form["password"]

        if name in users and check_password_hash(users[name], password):
            return redirect(url_for("Calculator"))
        
        else:
            flash('Invalid Username or password !')

    return render_template("login.html")

#calculator
@app.route("/calculator", methods=["GET", "POST"])
def Calculator():
    if request.method=="POST":
        Income_from_salary=request.form["Income_from_salary"]
        Income_from_Interest=request.form["Income_from_Interest"]
        Rental_Income_Received=request.form["Rental_Income_Received"]
        Income_from_Digital_Assets=request.form["Income_from_Digital_Assets"]
        Other_Income=request.form["Other_Income"]
        exempt_allowances=request.form["exempt_allowances"]
        Interest_Paid_on_Home_Loan=request.form["Interest_Paid_on_Home_Loan"]
        Interest_Paid_on_Loan=request.form["Interest_Paid_on_Loan"]
        Basic_Deductions_80C=request.form["Basic_Deductions_80C"]
        Medical_Insurance_80D=request.form["Medical_Insurance_80D"]
        Interest_on_Educational_Loan_80E=request.form["Interest_on_Educational_Loan_80E"]
        Employees_contribution_to_NPS_80CCD=request.form["Employees_contribution_to_NPS_80CCD"]
        Interest_from_Deposits_80TTA=request.form["Interest_from_Deposits_80TTA"]
        Donations_to_Charity_80G=request.form["Donations_to_Charity_80G"]
        Interest_on_Housing_Loan_80EEA=request.form["Interest_on_Housing_Loan_80EEA"]
        net_taxable_income= (int(Income_from_salary) + int(Income_from_Interest) + int(Rental_Income_Received) + int(Income_from_Digital_Assets) +  int(Other_Income))-(int(Interest_on_Housing_Loan_80EEA) + int(Donations_to_Charity_80G) + int(Interest_from_Deposits_80TTA) + int(Employees_contribution_to_NPS_80CCD) + int(Interest_on_Educational_Loan_80E) + int(Medical_Insurance_80D) + int(Basic_Deductions_80C) + int(Interest_Paid_on_Loan) + int(Interest_Paid_on_Home_Loan) + int(exempt_allowances))
        tax=0
        if net_taxable_income<=700000:
            flash("Calculated Tax : {}".format(tax))
        elif net_taxable_income <= 600000 and net_taxable_income > 300000:
            tax=(net_taxable_income-300000)/20
            flash("Calculated Tax : {}".format(tax))
        elif net_taxable_income <= 900000:
            tax=(net_taxable_income-600000)*0.1 + 15000
            flash("Calculated Tax : {}".format(tax))
        elif net_taxable_income <= 1200000:
            tax=((net_taxable_income-900000)*3)/20 + 15000 + 30000
            flash("Calculated Tax : {}".format(tax))
        elif net_taxable_income <= 1500000:
            tax=(net_taxable_income-1200000)/5 + 15000 + 30000 + 45000
            flash("Calculated Tax : {}".format(tax))
        else:
            tax=((net_taxable_income-1500000)*30)/100 + 15000 + 30000 + 45000 + 60000
            flash("Calculated Tax : {}".format(tax))
        
    return render_template("calculator.html")

    


#main block
if __name__ == "__main__":
    app.run(debug=True)
