import requests
import json

def test_mistral_relay():
    base_url = "https://c5dfa47b-2b2f-4a91-b067-2b28e0df40de-00-1dwf39mp74997.janeway.replit.dev"
    model = "mistral-tiny"  # Replace with an actual Mistral model name
    
    url = f"{base_url}/v1/mistral/{model}"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "messages": [
            {"role": "user", "content": "What are the main features of the Mistral AI language model?"}
        ]
    }

    with requests.post(url, headers=headers, json=data, stream=True) as response:
        print(f"Status Code: {response.status_code}")
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                if decoded_line.startswith("data: "):
                    try:
                        json_data = json.loads(decoded_line[6:])
                        if 'choices' in json_data and len(json_data['choices']) > 0:
                            content = json_data['choices'][0]['delta'].get('content', '')
                            if content:
                                print(content, end='', flush=True)
                    except json.JSONDecodeError:
                        print(f"Error decoding JSON: {decoded_line}")

if __name__ == "__main__":
    test_mistral_relay()
