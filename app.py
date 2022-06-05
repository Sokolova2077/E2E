# standart
import numpy as np
# work w images
from PIL import Image
import io
from io import BytesIO
import base64
# JFML
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, decode_predictions
from keras.applications.vgg16 import VGG16, decode_predictions

# Flask fpr WS
from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__) 
#makingmodel
Shape = (224, 224, 3)
def ml1():
    model = ResNet50(include_top=True, weights="imagenet", input_shape=Shape)
    return model

def ml2():
    model = VGG16(include_top=True, weights="imagenet", input_shape=Shape)
    return model

# decoding
def decode(req):
    encoded = req["image"]
    decoded = base64.b64decode(encoded)
    return decoded
#preparing RGB and etc
def prepare(decoded):
    PilImage = Image.open(io.BytesIO(decoded)).resize((224,224), Image.LANCZOS).convert("RGB") 
    image = np.asarray(PilImage)
    batch = np.expand_dims(image, axis=0)
    return batch

model16 = ml2()
model50 = ml1()
  
@app.route("/predict50", methods=["POST"])
def predict50():
    # get the data request and prepar for ml
    req = request.get_json(force=True)
    image = decode(req)
    batch = prepare(image)
    
    prediction = model.predict(batch)
    top_label = [(i[1],str(i[2])) for i in decode_predictions(prediction)[0][0]]
    # response 
    response = {"prediction": top_label}
    print("[+] results {}".format(response))
    
    return jsonify(response) # JSON
    
@app.route("/predict16", methods=["POST"])
def predict16():
    # get the data request and prepar for ml
    req = request.get_json(force=True)
    image = decode(req)
    batch = prepare(image)
    
    prediction = model.predict(batch)
    top_label = [(i[1],str(i[2])) for i in decode_predictions(prediction)[0][0]]
    # response 
    response = {"prediction": top_label}
    print("[+] results {}".format(response))
    
    return jsonify(response) # JSON
if __name__ == '__main__':
    app.run()