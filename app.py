from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def age_calculator():

    age = None

    if request.method == "POST":

        dob = request.form["dob"]

        # Convert DOB string to date
        year, month, day = map(int, dob.split("-"))
        birth_date = date(year, month, day)

        today = date.today()

        # Calculate age
        age = today.year - birth_date.year

        # Check if birthday has occurred this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

    return render_template("index.html", age=age)


if __name__ == "__main__":
    app.run(debug=True)