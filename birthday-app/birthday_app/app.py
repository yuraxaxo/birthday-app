from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "kitty-secret-key"

PASSWORD = "kitty0202"

@app.route("/", methods=["GET", "POST"])
def lock():
    error = None
    if request.method == "POST":
        if request.form.get("password") == PASSWORD:
            session["unlocked"] = True
            return redirect(url_for("card"))
        else:
            error = "Wrong password 💔"
    return render_template("lock.html", error=error)

@app.route("/card")
def card():
    if not session.get("unlocked"):
        return redirect(url_for("lock"))
    return render_template("card.html")

if __name__ == "__main__":
    app.run()
