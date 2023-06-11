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
    
    # Call the function to find plant dimensions
    plant_height, plant_width = find_plant_dimensions(image_path)

    # Call the function to calculate the leaf area
    leaf_area = calculate_leaf_area(image_path)
   
    # Call the fuction to calculate the green percentage
    green_percentage = green_percentage_plant(image_path)

    # Calculate the chlorophyll content based on the green percentage (example formula)
    chlorophyll_content = 0.01 * green_percentage

    # Perform biomass estimation (replace with your own method)
    biomass = 0.2 * plant_height + 10
    
    lum = float(fetch_luminosity_data())
    hum = float(fetch_humidity_data())
    Mois = float(fetch_Mois_data())
    Temp = float(fetch_Temp_data())
    N = float(fetch_N_data())
    P = float(fetch_P_data())
    K = float(fetch_K_data())
    
    #model = health.load()
    #health = health.predict()
    
    health = health_plant(image_path)   
    
    
    model = joblib.load('Fertility.joblib')
    soil = model.predict([[N,P,K]])
    print(soil)
    
    model = joblib.load('Growth.joblib')
    growth = model.predict([[plant_height,plant_width,chlorophyll_content, Temp,hum , lum]])
    print(growth)
    
    # Example results for demonstration
    results = [ str(soil[0]), str(growth[0]), health]

    response = jsonify({'results': results})
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    return response


# Define a route and its corresponding view function
@app.route('/')
def hello():
    return "Hello, World!"

def find_plant_dimensions(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Find contours of the plant
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour (assuming it's the plant)
    largest_contour = max(contours, key=cv2.contourArea)

    # Find the bounding rectangle of the largest contour
    x, y, w, h = cv2.boundingRect(largest_contour)

    # Draw the bounding rectangle on the image
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the image with the bounding rectangle
    # cv2.imshow("Image", image)
    # cv2.waitKey(0)

    # Calculate the height and width of the plant
    height = h*(0.0264)
    width = w*(0.0264)

    return height, width

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




def calculate_leaf_area(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply image thresholding
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize total leaf area
    total_area = 0

    # Iterate over each contour and calculate leaf area
    for contour in contours:
        # Calculate contour area
        area = cv2.contourArea(contour)
        total_area += area

        # Draw contour on the image (optional)
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

    # Display the image with contours (optional)
    #cv2.imshow("Image", image)
    #cv2.waitKey(0)

    return total_area

def green_percentage_plant(image_path):
    
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for green color in HSV
    lower_green = np.array([36, 25, 25])
    upper_green = np.array([86, 255, 255])

    # Threshold the image to get the green areas
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Calculate the percentage of green pixels in the image
    total_pixels = np.prod(mask.shape[:2])
    green_pixels = np.count_nonzero(mask)
    green_percentage = (green_pixels / total_pixels) * 100
    
    return green_percentage

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