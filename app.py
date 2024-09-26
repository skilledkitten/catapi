from flask import Flask, request, jsonify, render_template, Response, stream_with_context
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from api import openai, google, perplexity, anthropic, chipp, mistral

app = Flask(__name__)

# Initialize the rate limiter
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    storage_uri="memory://",
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/v1/<provider>/<model>', methods=['POST'])
@limiter.limit("60 per minute")
def relay_request(provider, model):
    try:
        data = request.json
        if provider == 'chipp':
            api_key = request.headers.get('api-key')
            if not api_key:
                return jsonify({"error": "API key is missing"}), 401
            response = chipp.relay_request(model, data, api_key=str(api_key), stream=True)
        elif provider == 'openai':
            response = openai.relay_request(model, data, stream=True)
        elif provider == 'google':
            response = google.relay_request(model, data, stream=True)
        elif provider == 'perplexity':
            response = perplexity.relay_request(model, data, stream=True)
        elif provider == 'anthropic':
            response = anthropic.relay_request(model, data, stream=True)
        elif provider == 'mistral':
            response = mistral.relay_request(model, data, stream=True)
        else:
            return jsonify({"error": "Invalid provider"}), 400
        
        def generate():
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    yield chunk

        return Response(stream_with_context(generate()), content_type='application/json')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify(error="Rate limit exceeded", details=str(e.description)), 429

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
