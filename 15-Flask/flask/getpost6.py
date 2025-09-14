from flask import Flask, render_template, request, redirect

## WSGI Application
app = Flask(__name__)

@app.route("/",methods=['GET'])
def welcome():
    return "<html><h1>Welcome to the Flask Course!!!</h1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about",methods=['GET'])
def about():
    return render_template('about.html')

@app.route("/form",methods=['GET'])
def form():
    return render_template('getpost4_form.html')

# @app.route("/submit",methods=['POST'])
# def submit():
#     name = request.form['name']
#     return f"Hello {name}, thanks for submitting the form!!!"

@app.route("/submit",methods=['POST'])
def submit():
    name = request.form['name']
    return render_template('getpost5_thankyou.html',username=name)

if __name__ == '__main__':
    app.run(debug=True)