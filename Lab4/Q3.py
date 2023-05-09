from flask import Flask, render_template
import sys
 
app = Flask(__name__)
@app.route('/')
 
def web_page():
    return render_template('Q3.html')
