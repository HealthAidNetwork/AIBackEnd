from flask import Flask, request, jsonify
import base64
import os
import lib

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_image():
    try:
        data = request.get_json()
        if 'image' in data:
            base64_image=data['image']
            # Decode the base64 image data
            image_data = base64.b64decode(data['image'])

            # Save the image to a specific folder
            image_filename = "uploaded_image.png"  # You can specify a filename
            with open(image_filename, "wb") as image_file:
                image_file.write(image_data)

            if "prompt" in data:
                prompt=data["prompt"]
                answer=lib.get_response_enc_img(base64_image,prompt)
                return jsonify({"message": answer})
            else:
                return jsonify({"error": "prompt missing"})            
        else:
            return jsonify({"error": "Image not found in the request"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8001)