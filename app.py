from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

messages = []
users = set()


@app.route("/")
def index():
    return render_template("index.html", messages=messages)


@app.route("/send", methods=["POST"])
def send():
    username = request.form.get("username")
    message = request.form.get("message")
    users.add(username)
    messages.append({"username": username, "message": message})
    return redirect(url_for("index"))


@app.route("/get_users")
def get_users():
    return jsonify(list(users))


if __name__ == "__main__":
    app.run(debug=True)
