from flask import Flask

## WSGI Application
app = Flask(__name__)

@app.route("/")
def weclome():
    return "Welcome to the Flask course."

@app.route("/index")
def description():
    return "This is an amazing course."

@app.route("/contact-us")
def contact():
    return "Contact us @12345"

if __name__ == "__main__":
    app.run(debug=True)