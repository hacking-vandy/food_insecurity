from flask import Flask, render_template, request
from scripts import *

app = Flask(__name__)

@app.route("/",methods = ['GET','POST'])
def main():
	if request.method == 'POST':
		return render_template('processed.html')
   	return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)