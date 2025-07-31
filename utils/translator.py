from deep_translator import GoogleTranslator
import streamlit as st
from typing import Optional
import time

class IndicTranslator:
    def __init__(self):
        self.translator = GoogleTranslator()
        
    def translate(self, text: str, source_lang: str, target_lang: str) -> Optional[str]:
        """
        Reliable translation using deep-translator
        """
        if not text.strip():
            return "Please enter some text to translate."
        
        try:
            with st.spinner("🌐 AI translating..."):
                # Map language codes
                src = 'en' if source_lang == 'en' else 'ta'
                dest = 'ta' if target_lang == 'ta' else 'en'
                
                # Translate using deep-translator
                result = GoogleTranslator(source=src, target=dest).translate(text)
                
                if result:
                    return result
                else:
                    return "Translation failed. Please try again."
                    
        except Exception as e:
            # Fallback for common phrases
            fallback = {
                "hello": "வணக்கம்",
                "thank you": "நன்றி",
                "how are you": "எப்படி இருக்கிறீர்கள்",
                "good morning": "காலை வணக்கம்",
                "yes": "ஆம்",
                "no": "இல்லை",
                "வணக்கம்": "hello",
                "நன்றி": "thank you",
            }
            
            clean_text = text.lower().strip()
            if clean_text in fallback:
                return f"✨ {fallback[clean_text]} (offline)"
            else:
                return f"⚠️ Translation service unavailable. Showing text: {text}"
    
    def is_configured(self) -> bool:
        return True
