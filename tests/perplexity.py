import requests
import json

def test_perplexity_relay():
    url = "https://c5dfa47b-2b2f-4a91-b067-2b28e0df40de-00-1dwf39mp74997.janeway.replit.dev/v1/perplexity/llama-3.1-sonar-small-128k-online"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "messages": [
            {"role": "user", "content": "What is wrong with Intel at the moment? Could you give me a list of the latest news?"}
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
    test_perplexity_relay()
