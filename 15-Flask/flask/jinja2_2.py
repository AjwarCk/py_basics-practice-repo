from flask import Flask, render_template, request, redirect

### jinja2 Template Engine
'''
{{ }} expression to print output in html
{%...%} conditions, for loops
(#...#) this is for comments
'''

## WSGI Application
app = Flask(__name__)

@app.route('/',methods=['GET'])
def welcome():
    return '<html><h1>This is the Flask course!!!</h1></html>'

@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET'])
def form():
    return render_template('getpost4_form.html')

@app.route('/submit',methods=['POST'])
def submit():
    name = request.form['name']
    return render_template('getpost5_thankyou.html',username=name)

## Jinja2 template engine ({{ }} expression through html output)
@app.route('/success/<int:score>',methods=['GET','POST'])
def success(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    return render_template('result1.html',results=res)


if __name__ == '__main__':
    app.run(debug=True)