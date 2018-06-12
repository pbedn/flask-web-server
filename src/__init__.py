from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    now = datetime.datetime.now()
    time_string = now.strftime("%Y-%m-%d %H:%M")
    template_data = {
        'title': 'Hello',
        'time': time_string,
        }
    return render_template('index.html', **template_data)
