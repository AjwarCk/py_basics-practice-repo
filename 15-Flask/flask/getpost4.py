from flask import Flask, render_template, request

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

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}, thanks for equiring!"
    return render_template('getpost4_form.html')

@app.route("/submit",methods=['POST'])
def submit():
    name = request.form['name']
    return f"Hellow {name}, thanks for equiring!"


if __name__ == '__main__':
    app.run(debug=True)