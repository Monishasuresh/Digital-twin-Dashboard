import cv2
import numpy as np
# Python code using Flask
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
import joblib
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import image
from PIL import Image



app = Flask(__name__)
CORS(app)

@app.route('/api/upload-image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'No image selected'}), 400

    # Save the uploaded image to a local folder
    upload_folder = 'C:\\Users\\admin\\Desktop\\Capstone Project\\Code\\Data'  # Adjust this path to your desired upload folder
    os.makedirs(upload_folder, exist_ok=True)
    image_path = os.path.join(upload_folder, image_file.filename)
    image_file.save(image_path)

    response = jsonify({'message': 'Image uploaded successfully', 'imagePath': image_path})
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    return response


@app.route('/api/process-image', methods=['POST'])
def process_image():
    data = request.get_json()
    image_path = data.get('imagePath')

    # Process the image and generate results
    # ...
    
    # Provide the path to your image file
    #image_path = "C:/Users/admin/Desktop/Capstone Project/Code/Chilli images/capture1.jpg"
    
    lum = float(fetch_luminosity_data())
    hum = float(fetch_humidity_data())
    Mois = float(fetch_Mois_data())
    Temp = float(fetch_Temp_data())
    N = float(fetch_N_data())
    P = float(fetch_P_data())
    K = float(fetch_K_data())
    
    #model = health.load()
    #health = health.predict()
    
    Tempsug = ''
    Humsug = ''
    lumsug = ''
    Moissug = ''
    Fersug = ''
    
    if(Temp<20):
        Tempsug = 'Low'
    elif(Temp>30):
        Tempsug = 'High'
        
    if(hum<40):
        Humsug = 'Low'
    elif(hum>70):
        Humsug = 'High'
        
    if(lum>800):
        lumsug = 'Low'
        
    if(Mois>1000):
        Moissug = 'Low'
             

    
    health = health_plant(image_path)   
    model = joblib.load('Fertility.joblib')
    soil = model.predict([[N,P,K]])
    print(soil)
    
    if(soil == 'Fertile'):
        Fersug = 'Fertile soil typically indicates a well-balanced nutrient composition and good organic matter content.\nIt provides an ideal environment for plant growth and nutrient uptake.\nSuggestions to maintain the soil fertility:\n1. Continuously enhance the organic matter content by adding compost, well-rotted manure, or cover crops improves soil structure, water retention, and nutrient availability\n2.Ensure appropriate irrigation practices, avoiding overwatering or underwatering, and improving drainage.\n3.  Implement a crop rotation plan to minimize nutrient imbalances and pests.'
    else :
        Fersug = 'Infertile soil lacks essential nutrients and may have imbalances that hinder plant growth and productivity.low nutrient levels can effect plant growth in a number of ways including:1. reduced growth2. stunted roots3. yellowing leaves4. reduced flowering and fruitingsuggestions:1. use organic fertilizers which is rich in nitrogen (N), phosphorus (P) , potassium (K) to increase the npk level eg. well-rotted manure, seaweed-based fertilizers2. Avoid Overuse of Chemical Fertilizers3. Water Properly4. Rotate Nutrient-Hungry Crops with Legumes: Practice crop rotation by alternating nutrient-hungry plants with legumes like beans, peas, or lentils. Legumes fix nitrogen in the soil, helping to increase the NPK levels naturally for the subsequent crops.5. Use Organic Soil Amendments: Add organic soil amendments that naturally contain NPK elements. For example, incorporate compost, aged manure, or worm castings into the soil.'
    
    model = joblib.load('Growth.joblib')
    growth = model.predict([[ Temp,hum,lum,Mois]])
    print(growth)
    
    # Example results for demonstration
    results = [ str(soil[0]), str(growth[0]), health, Tempsug, Humsug, lumsug, Moissug, Fersug]

    response = jsonify({'results': results})
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    return response


# Define a route and its corresponding view function
@app.route('/')

def fetch_luminosity_data():
    try:
        response = requests.get('https://api.thingspeak.com/channels/2146750/fields/1.json?api_key=PNOQX59AGZZYNI98&results=2')
        data = response.json()
        return data['feeds'][0]['field1']
    except Exception as error:
        print('Error fetching luminosity data:', error)

def fetch_humidity_data():
    try:
        response = requests.get('https://api.thingspeak.com/channels/2146750/fields/4.json?api_key=PNOQX59AGZZYNI98&results=2')
        data = response.json()
        return data['feeds'][0]['field4']
    except Exception as error:
        print('Error fetching Humidity data:', error)
    
def fetch_N_data():
    try:
        response = requests.get('https://api.thingspeak.com/channels/2146750/fields/5.json?api_key=PNOQX59AGZZYNI98&results=2')
        data = response.json()
        return data['feeds'][0]['field5']
    except Exception as error:
        print('Error fetching N data:', error)

def fetch_P_data():
    try:
        response = requests.get('https://api.thingspeak.com/channels/2146750/fields/6.json?api_key=PNOQX59AGZZYNI98&results=2')
        data = response.json()
        return data['feeds'][0]['field6']
    except Exception as error:
        print('Error fetching P data:', error)

def fetch_K_data():
    try:
        response = requests.get('https://api.thingspeak.com/channels/2146750/fields/7.json?api_key=PNOQX59AGZZYNI98&results=2')
        data = response.json()
        return data['feeds'][0]['field7']
    except Exception as error:
        print('Error fetching K data:', error)


def fetch_Mois_data():
    try:
        response = requests.get('https://api.thingspeak.com/channels/2146750/fields/2.json?api_key=PNOQX59AGZZYNI98&results=2')
        data = response.json()
        return data['feeds'][0]['field2']
    except Exception as error:
        print('Error fetching Moisture data:', error)


def fetch_Temp_data():
    try:
        response = requests.get('https://api.thingspeak.com/channels/2146750/fields/3.json?api_key=PNOQX59AGZZYNI98&results=2')
        data = response.json()
        return data['feeds'][0]['field3']
    except Exception as error:
        print('Error fetching Temperature data:', error)


def health_plant(image_path):
    test_image_path = image_path
    
    img_width, img_height = 224, 224
    test_image = Image.open(test_image_path)
    test_image = test_image.resize((img_width, img_height))
    test_image = np.array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    test_image = test_image / 255.0
    
    model = tf.keras.models.load_model('health.h5')
    predictions = model.predict(test_image)
    
    predicted_class = 'Healthy' if predictions[0][0] < 0.5 else 'Unhealthy'
    
    return predicted_class
    
    

if __name__ == '__main__':
    
    app.run()