import cv2
import numpy as np
# Python code using Flask
from flask import Flask, request, jsonify

app = Flask(__name__)

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
    cv2.imshow("Image", image)
    cv2.waitKey(0)

    # Calculate the height and width of the plant
    height = h*(0.0264)
    width = w*(0.0264)

    return height, width

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
    cv2.imshow("Image", image)
    cv2.waitKey(0)

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


@app.route('/api/collect-results', methods=['POST'])
def collect_results():
    data = request.get_json()
    
    # Process the data as needed
    result = process_data(data)
    
    # Return the result as a JSON response
    return jsonify(result)

def process_data(data):
    # Perform any required processing on the data
    # and generate the result
    result = { 'message': 'Data received and processed successfully!' }
    return result
    

if __name__ == '__main__':

    # Provide the path to your image file
    image_path = "C:/Users/admin/Desktop/Capstone Project/Code/Chilli images/capture1.jpg"
    
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
    
    
    app.run()


# Display the results
#print("Green Percentage: {:.2f}%".format(green_percentage))
#print("Chlorophyll Content: {:.2f}".format(chlorophyll_content))
#print("Leaf Area:", leaf_area*(0.0264))
#print("Plant Height:", plant_height)
#print("Plant Width:", plant_width)

