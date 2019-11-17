from flask import Flask, render_template
from werkzeug import secure_filename
from flask import request


app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      gc4.flite_convert()
      return render_template("about.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if (__name__ == "__main__"):
    app.run(debug=True)
