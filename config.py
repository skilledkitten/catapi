import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API keys should be set as environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
PERPLEXITY_API_KEY = os.getenv('PERPLEXITY_API_KEY')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')

# API base URLs
OPENAI_API_URL = "https://api.openai.com/v1"
GOOGLE_API_URL = "https://generativelanguage.googleapis.com/v1beta2"
PERPLEXITY_API_URL = "https://api.perplexity.ai"
ANTHROPIC_API_URL = "https://api.anthropic.com/v1"
CHIPP_API_URL = "https://api.chipp.ai/v1"
MISTRAL_API_URL = "https://api.mistral.ai/v1"
