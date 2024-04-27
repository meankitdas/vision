# from flask import Flask,jsonify,request,make_response
import requests, json, os, io
# from flask_cors import CORS
# from dotenv import load_dotenv
from google.cloud import vision

# load_dotenv()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'products-406910-08369e38553b.json'

client = vision.ImageAnnotatorClient()

file_name = 'tshirt.png'
image_path = os.path.join('./images',file_name)

with io.open(image_path,'rb') as image_file:
    content = image_file.read()
    # print(content)
    
image = vision.Image(content=content)
response = client.web_detection(image=image)
web_detection = response.web_detection

# print(response)

for entity in web_detection.web_entities:
    # if (str(entity.description).find(domain) >-1):
        print(entity.description)


print("done!")



# app = Flask(__name__)
# CORS(app)

# @app.route('/', methods=['GET'])
# def hello():
#     return jsonify('Hello World!')

# @app.route('/', methods=['POST'])
# def get_params():
#     params = request.get_json()
#     prompt = params['prompt']
      
    
#     return params

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=80)
    