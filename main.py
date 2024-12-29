from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Necessary for flash messages

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    # Get form data
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    
    # You can process or save the data here (e.g., store in a database or send an email)
    # For now, let's just display a confirmation message
    flash(f"Thank you, {name}! Your message has been sent.")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
