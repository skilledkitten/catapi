import requests
from config import GOOGLE_API_KEY, GOOGLE_API_URL

def relay_request(model, data, stream=False):
    headers = {
        "Content-Type": "application/json"
    }
    
    url = f"{GOOGLE_API_URL}/models/{model}:generateContent?key={GOOGLE_API_KEY}"
    data['stream'] = stream
    
    response = requests.post(url, json=data, headers=headers, stream=stream)
    
    return response
