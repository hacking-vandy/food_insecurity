from flask import Flask, render_template, request
from scripts import data, model

app = Flask(__name__)

data_df = data.get_data()

@app.route("/",methods = ['GET','POST'])
def main():
	if request.method == 'POST':
		results = model.do(data_df)
		return render_template('processed.html',results = results)
   	return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)