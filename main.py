
from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True
form_value = """
<!DOCTYPE html>    
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;   

            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
                
            }
        </style>
    </head>
    <body>
    <form method="POST">
      <p>What is going on?!</p>
      <label for="Rotate-by">Rotate By:</label>
       <input id ="Rotate-by" name="rot" type="text" value="0"/> <br>
       <textarea name="text" rows="10" cols="50"></textarea><br>
       <input type="submit" />
    </form>
    </body>
</html>
"""
@app.route('/', methods=['POST'])
def index():
    return form_value
def encrypt():

app.run()