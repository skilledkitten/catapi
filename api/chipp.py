import requests

def relay_request(model, data, api_key, stream=False):
    headers = {
        "Content-Type": "application/json"
    }
    
    url = "https://api.chipp.ai/chat"
    
    chipp_data = {
        "messageList": [
            {
                "role": message["role"],
                "content": message["content"]
            } for message in data.get("messages", [])
        ],
        "applicationId": int(model),
        "apiKey": str(api_key)  # Ensure the API key is a string
    }
    
    if "threadId" in data:
        chipp_data["threadId"] = data["threadId"]
    
    response = requests.post(url, json=chipp_data, headers=headers, stream=stream)
    
    return response
