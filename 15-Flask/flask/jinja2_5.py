from flask import Flask, render_template, request, redirect, url_for

## jinja2 template engine
'''
{{ }} expression to print out in html
{% for loop %} {endfor} or {% if condition %} {% endif %} condition
{# ... #} comments
'''

## WSGI Application
app = Flask(__name__)

@app.route('/',methods=['GET'])
def welcome():
    return '<html><h1>Welcome to the Flask Course!!!</h1></html>'

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

@app.route('/marks/<int:score>',methods=['GET'])
def marks(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    return render_template('result1.html',results=res)

@app.route('/success/<int:score>',methods=['GET'])
def success(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    
    exp = {'score':score, 'result':res}

    return render_template('result2.html',results=exp)

@app.route('/successif/<int:score>',methods=['GET'])
def successif(score):
    return render_template('result3.html',results=score)

@app.route('/submitclick',methods=['POST','GET'])
def submitclick():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science+maths+c+data_science)/4
    else:
        return render_template('result4.html')
    return redirect(url_for('success',score=total_score))

if __name__ == '__main__':
    app.run(debug=True)