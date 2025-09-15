from flask import Flask, render_template, request, redirect

## jinja2 template engine
'''
{{    }} expression to print out html output
{%..forloop / ifelse..%} {% endfor %} conditions, for loop
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

## Variable Rule : Dictionary and for loop and comments in html
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    exp = {'score':score, 'result':res}
    return render_template('result2.html',results=exp)

## Variable Rule: if condition
@app.route('/successif/<int:score>',methods=['GET'])
def successif(score):
    return render_template('result3.html',results=score)

if __name__ == '__main__':
    app.run(debug=True)