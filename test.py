import requests
import base64

# Encode an image to base64 (replace 'image.png' with your image file)


# image_path='medFront.jpeg'
# with open(image_path, "rb") as image_file:
#     base64_image= base64.b64encode(image_file.read()).decode('utf-8')
 
# # Send a POST request to the Flask server
# response = requests.post('http://localhost:8001/process', json={"image": base64_image,"prompt":"Is it an image of a medicine? Anser yes or no"})


# print(response.json())

image_path='medBack.jpeg'
with open(image_path, "rb") as image_file:
    base64_image= base64.b64encode(image_file.read()).decode('utf-8')
 
# Send a POST request to the Flask server

response = requests.post('http://localhost:8001/process', json={"image": base64_image,"prompt":"Can you read the text."})
print(response.json())