
from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True
form_value="""C:\Users\snoop\lc101\web-caesar\forms.html"""
@app.route('/', methods=['POST'])
def index():
    return form_value
def encrypt():

app.run()