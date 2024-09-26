import requests
from config import OPENAI_API_KEY, OPENAI_API_URL

def relay_request(model, data, stream=False):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    url = f"{OPENAI_API_URL}/chat/completions"
    data['model'] = model
    data['stream'] = stream
    
    response = requests.post(url, json=data, headers=headers, stream=stream)
    
    return response
