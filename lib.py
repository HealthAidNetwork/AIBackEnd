import base64
import requests

# OpenAI API Key
api_key = "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"


# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')




def get_response_enc_img(base64_image,prompt):
    
    
    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {api_key}"
    }

    payload = {
      "model": "gpt-4-vision-preview",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": f"{prompt}"
            },
            {
              "type": "image_url",
              "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
              }
            }
          ]
        }
      ],
      "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

#     print(response.json())    
    answer=response.json()["choices"][0]["message"]["content"]
    return answer  


def get_response_image_path(image_path,prompt):
    base64_image = encode_image(image_path)
    return get_response_enc_img(base64_image,prompt)
    
    