import torch
import torchvision.transforms as T
from torchvision.models.detection import maskrcnn_resnet50_fpn
from PIL import Image
import numpy as np
import cv2

# Load pre-trained Mask R-CNN model
model = maskrcnn_resnet50_fpn(pretrained=True)
model.eval()

# Define the transformation to preprocess the image
transform = T.Compose([
    T.ToTensor(),
    T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# Load and preprocess the image
image_path = "C:/Users/admin/Desktop/Capstone Project/Code/Final/Chilli.jpg"
image = Image.open(image_path).convert('RGB')
input_image = transform(image)

# Add a batch dimension to the input image
input_image = input_image.unsqueeze(0)

# Pass the input image through the model
with torch.no_grad():
    predictions = model(input_image)

# Extract the bounding boxes, labels, and masks from the predictions
boxes = predictions[0]['boxes']
labels = predictions[0]['labels']
masks = predictions[0]['masks'].squeeze(1).numpy()

# Display the results
image = np.array(image)
for box, label, mask in zip(boxes, labels, masks):
    # Draw bounding box
    cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), color=(0, 255, 0), thickness=2)
    
    # Add label
    label_str = f'Label: {label}'
    cv2.putText(image, label_str, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # Apply mask
    mask = (mask > 0.5)
    masked_image = np.zeros_like(image)
    masked_image[mask] = image[mask]

    # Display the image with mask
    cv2.imshow('Object Detection', masked_image)
    cv2.waitKey(0)
    
# Close all windows
cv2.destroyAllWindows()