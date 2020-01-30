import requests, json
from flask import Flask, render_template, url_for,request
from databases import *
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'



@app.route('/')
def index():
	return render_template('index.html')

@app.route('/form')
def form():
	return render_template('form.html')



image_url = "car.jpg" 

@app.route('/generic',methods=['GET','POST'])
def car_detect():
	with open(image_url, 'rb') as f:
		response = (requests.post(
		'http://api.carnet.ai/mmg/detect',
		data = f.read(),
		headers = {
		'api-key': '4c0ee160-4278-4142-a54e-8266d3542d7f',
		'Content-Type': 'application/octet-stream',
		},
		).text)
		#print('response')
		#print(response)

		response_dict = json.loads(response)
		gen_years = response_dict["detections"][0]["mmg"][0]["gen_years"]
		make_name = response_dict["detections"][0]["mmg"][0]["make_name"]
		model_name = response_dict["detections"][0]["mmg"][0]["model_name"]


		#gen_years = response_dict["detections"]
		Carname = (gen_years + make_name + " " + model_name)
		print('this is car is a ' + Carname)
		return render_template('generic.html' , Carname = Carname )

 


if __name__ == '__main__':
    app.run(debug=True)


