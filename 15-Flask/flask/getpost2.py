from flask import Flask, render_template, request

## WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>This is a Flask course.</h1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about",methods=['GET'])
def about():
    return render_template('about.html')

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method == 'POST':
        pass
    return render_template('getpost2_form.html')

if __name__ == '__main__':
    app.run(debug=True)