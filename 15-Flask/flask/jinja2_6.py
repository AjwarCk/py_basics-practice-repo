from flask import Flask, render_template, request, redirect, url_for

## jinja2 template engine
'''
{{ }}  expressions to print out to html
{% %}  conditions
{# #}  comments
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

@app.route('/avgmarks/<int:avgmark>',methods=['GET'])
def avgmarks(avgmark):
    res = ""
    if avgmark >= 40:
        res = "PASSED"
    else:
        res = "FAILED"
    exp = {'Average Mark':avgmark, 'result':res}
    return render_template('result2.html',results=exp)

## 1. Bulding dynamic URLs (redirect URL)
@app.route('/submitclick',methods=['GET','POST'])
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

## 2. Bulding dynamic URLs (redirect URL)
@app.route('/submitmark',methods=['GET','POST'])
def submitmark():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        avg_score = (science+maths+c+data_science)/4

    else:
        return render_template('result5.html')
    
    return redirect(url_for('avgmarks',avgmark=avg_score))


if __name__ == '__main__':
    app.run(debug=True)