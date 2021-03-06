import os
from flask import Flask, render_template
from tools import *
#from surprise import SVD
#from surprise import Dataset
#from surprise import evaluate, print_perf

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template')
app = Flask(__name__, template_folder = template_dir )


@app.route('/', methods=['GET'])
def index():
    topChoicefr = collab()
    data = yelpAPI_GetBusinesses(topChoicefr)
    print (data)
    return render_template('index.html', data=data)

# @app.route('/search/<input>', methods=['POST'])
# def search(input):   

#   return 

@app.route('/profile', methods=['GET'])
def profile():
    return render_template('profile.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/result', methods=['GET'])
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run()

