# Import statements to display model predictions
from ultralytics import YOLO
import matplotlib.pyplot as plt
import cv2

# Load YOLO model
model = YOLO("Train4best.pt")
 
# Path to the image
img_path = "FullImageperson.jpg"

# Perform prediction
results = model.predict(img_path, save = True)



# Get bounding box coordinates and areas
xy_array = results[0].boxes.xywh.numpy()
#print(xy_array)
AreaArray = [xy[2] * xy[3] for xy in xy_array]

max_index = AreaArray.index(max(AreaArray))

# Convert image to OpenCV format
img = cv2.cvtColor(results[0].plot(), cv2.COLOR_BGR2RGB)
#img = cv2.cvtColor(results[0][max_index].plot(), cv2.COLOR_BGR2RGB)


print(results[0].keypoints.xy)


# Display the image with the bounding box
plt.figure()
plt.imshow(img)
plt.show()

