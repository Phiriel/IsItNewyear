from flask import Flask, render_template
import datetime


app = Flask(__name__, template_folder="template")

@app.route('/')
def hello():
    a = datetime.datetime.now()
    newyear = ((a.day==1) and (a.month==1))
    return render_template('hello.html',newyear=newyear)

app.run(debug=True)

