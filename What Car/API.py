import requests, json


#image_url = "mazda.jpg" 

@app.route('/')
def car_detect():
	with open("mazda.jpg", 'rb') as f:
		response = (requests.post(
		'http://api.carnet.ai/mmg/detect',
		data = f.read(),
		headers = {
		'api-key': '4c0ee160-4278-4142-a54e-8266d3542d7f',
		'Content-Type': 'application/octet-stream',
		},
		).text)

		response_dict = json.loads(response)
		gen_years = response_dict["detections"][0]["mmg"][0]["gen_years"]
		make_name = response_dict["detections"][0]["mmg"][0]["make_name"]
		model_name = response_dict["detections"][0]["mmg"][0]["model_name"]


		#gen_years = response_dict["detections"]
		print(gen_years + make_name + " " + model_name)
		return render_template("car_detect.html" , G = model_name)

