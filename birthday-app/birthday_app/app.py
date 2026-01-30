from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

PASSWORD = "kitty0202"

@app.route("/", methods=["GET", "POST"])
def lock():
    if request.method == "POST":
        if request.form.get("password") == PASSWORD:
            return redirect(url_for("home"))
        else:
            return render_template("lock.html", error=True)
    return render_template("lock.html", error=False)

@app.route("/home")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
