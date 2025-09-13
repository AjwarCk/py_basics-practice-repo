from flask import Flask, render_template

'''
It creates an instance of the Flask class,
which will be your WSGI (web server gateway interface) application.
'''

## WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the Flask course.</H1></html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/support")
def support():
    return "Write us to test@test.com"

if __name__ == "__main__":
    app.run(debug=True)