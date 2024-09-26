import requests
import time

def test_provider(provider, model):
    url = f"https://c5dfa47b-2b2f-4a91-b067-2b28e0df40de-00-1dwf39mp74997.janeway.replit.dev/v1/{provider}/{model}"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "messages": [
            {"role": "user", "content": "Hello, how are you?"}
        ]
    }

    successful_requests = 0
    rate_limited_requests = 0

    for i in range(70):
        print(f"{provider} Request {i+1}")
        try:
            response = requests.post(url, headers=headers, json=data, timeout=10)
            print(f"Status Code: {response.status_code}")
            if response.status_code == 429:
                print("Rate limit exceeded")
                rate_limited_requests += 1
            elif response.status_code == 200:
                successful_requests += 1
                print("Request successful")
            else:
                print(f"Unexpected status code: {response.status_code}")
                print(f"Response: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

        time.sleep(0.1)  # Reduce delay between requests to trigger rate limiting faster

    print(f"\n{provider} - Successful requests: {successful_requests}")
    print(f"{provider} - Rate limited requests: {rate_limited_requests}")

def test_all_providers():
    providers = [
        ("openai", "gpt-4o-mini"),
        ("google", "gemini-pro"),
        ("perplexity", "llama-3.1-sonar-small-128k-online"),
        ("anthropic", "claude-2"),
        ("mistral", "mistral-tiny")
    ]

    for provider, model in providers:
        print(f"\nTesting {provider}")
        test_provider(provider, model)
        time.sleep(5)  # Wait between provider tests

if __name__ == "__main__":
    test_all_providers()
