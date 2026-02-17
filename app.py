from flask import Flask, render_template, request, redirect, url_for, jsonify
import html

app = Flask(__name__)

messages = []
users = set()

@app.route("/")
def index():
    return render_template("index.html", messages=messages)


@app.route("/send", methods=["POST"])
def send():
    username = request.form.get("username", "").strip()
    message = request.form.get("message", "").strip()

    if not username or not message:
        return redirect(url_for("index"))

    if len(username) > 50:
        username = username[:50]

    if len(message) > 500:
        message = message[:500]

    username = html.escape(username)
    message = html.escape(message)

    users.add(username)
    messages.append({"username": username, "message": message})

    if len(messages) > 100:
        messages.pop(0)

    return redirect(url_for("index"))


@app.route("/get_users")
def get_users():
    return jsonify(list(users))


if __name__ == "__main__":
    app.run(debug=True)