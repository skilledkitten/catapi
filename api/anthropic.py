import requests
from config import ANTHROPIC_API_KEY, ANTHROPIC_API_URL

def relay_request(model, data, stream=False):
    headers = {
        "Authorization": f"Bearer {ANTHROPIC_API_KEY}",
        "Content-Type": "application/json"
    }
    
    url = f"{ANTHROPIC_API_URL}/completions"
    data['model'] = model
    data['stream'] = stream
    
    response = requests.post(url, json=data, headers=headers, stream=stream)
    
    return response
