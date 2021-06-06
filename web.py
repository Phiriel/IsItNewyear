from flask import Flask, render_template
import datetime


app = Flask(__name__, template_folder="template")

@app.route('/')
def hello():
    now = datetime.datetime.now()
    newyear = ((now.day==1) and (now.month==1))
    return render_template('hello.html',newyear=newyear)

app.run(debug=True)

