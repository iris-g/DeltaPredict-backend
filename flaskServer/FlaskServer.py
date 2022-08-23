# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template
from flask import request
from waitress import serve
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)
app._static_folder = ''


@app.route("/")
@app.route('/data')
def get_time():
    # Returning an api for showing in  reactjs
    return {
        'Name': "geek",
        "Age": "22",
        "Date": x,
        "programming": "python"
    }


@app.route('/members')
def members():
    #Returning an api for showing in  reactjs
   return {
        'Name': "vered",
        "Age": "22",
        "Date": x,
        "programming": "python"
  }


import datetime

x = datetime.datetime.now()

if __name__ == "__main__":
    app.run(debug=True)
    #serve(app, host="0.0.0.0", port=5000)


def create_app():
    return app
