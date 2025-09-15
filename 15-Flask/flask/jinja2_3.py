from flask import Flask, render_template, request, redirect

## Jinja2 template engine
'''
{{     }} expression to print output in html
{%.....%} conditions, for loops
{#.....#} comments
'''

## WSGI Application
app = Flask(__name__)

@app.route('/',methods=['GET'])
def welcome():
    return '<html><h1>Welcome to the Flask course!!!</h1></html>'

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

## Variable Rule
@app.route('/marks/<int:score>',methods=['GET'])
def marks(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    return render_template('result1.html',results=res)

# Variable Rule passing dictionary to use for loop
@app.route('/success/<int:score>',methods=['GET'])
def success(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    
    exp = {'score':score, "res":res}

    return render_template('result2.html',results=exp)


if __name__ == '__main__':
    app.run(debug=True)