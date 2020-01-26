from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title = "Home")

@app.route('/people')
def people():
    return render_template('people.html',
    title = "People")