import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Translation configuration
    TRANSLATION_MODEL = "huggingface_api"
    
    # Streamlit configuration
    PAGE_TITLE = "🤖 AI English-Tamil Translator"
    PAGE_ICON = "🤖"
    
    # Language mappings
    LANGUAGES = {
        "English": "en",
        "Tamil": "ta"
    }
    
    # Model information
    MODEL_INFO = {
        "name": "Hugging Face AI",
        "description": "Real AI translation using Helsinki-NLP models",
        "provider": "Hugging Face"
    }
