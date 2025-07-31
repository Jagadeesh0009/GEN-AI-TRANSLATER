import streamlit as st
from langchain.memory import ConversationBufferMemory
from utils.translator import IndicTranslator
from config import Config
import time

# Page configuration
st.set_page_config(
    page_title="🤖 AI Neural Translator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for attractive tech/AI background
def set_custom_background():
    st.markdown("""
    <style>
    /* Main background with tech/AI theme */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    /* Circuit board pattern overlay */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 25% 25%, #00ff88 2px, transparent 2px),
            radial-gradient(circle at 75% 75%, #0066ff 1px, transparent 1px),
            linear-gradient(135deg, rgba(0,20,40,0.8) 0%, rgba(0,10,30,0.9) 100%);
        background-size: 50px 50px, 30px 30px, 100% 100%;
        opacity: 0.1;
        z-index: -1;
    }
    
    /* Sidebar styling with glass effect */
    .css-1d391kg {
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 15px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
    }
    
    /* Chat messages with glass morphism */
    .stChatMessage {
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 15px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        margin: 10px 0 !important;
    }
    
    /* Input box styling */
    .stChatInputContainer {
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 25px !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
    }
    
    /* Headers and text styling */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #ffffff !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5) !important;
    }
    
    /* Metrics and info boxes */
    .stMetric, .stInfo {
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        color: white !important;
    }
    
    /* Success and error message styling */
    .stSuccess, .stError {
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
    }
    
    /* Animated floating tech icons */
    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(180deg); }
        100% { transform: translateY(0px) rotate(360deg); }
    }
    
    .stApp::after {
        content: "🤖 AI ⚡ 🔬 💻 🌐 🚀";
        position: fixed;
        top: 20%;
        right: -100px;
        font-size: 3rem;
        opacity: 0.03;
        animation: float 20s ease-in-out infinite;
        z-index: -1;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize components
@st.cache_resource
def get_translator():
    return IndicTranslator()

def initialize_session_state():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "memory" not in st.session_state:
        st.session_state.memory = ConversationBufferMemory()

def render_sidebar():
    """Render sidebar with settings and info"""
    with st.sidebar:
        st.header("🔧 Translation Settings")
        
        direction = st.selectbox(
            "Translation Direction:",
            ["English → Tamil", "Tamil → English"],
            index=0
        )
        
        st.markdown("---")
        st.header("📊 Session Stats")
        st.metric("Total Translations", len(st.session_state.messages) // 2)
        
        st.markdown("---")
        st.header("🤖 AI Technology")
        st.markdown("""
        **AI-Powered Translator**
        
        🌟 Advanced neural translation
        
        **Features:**
        - 🔄 Real-time AI processing
        - 💬 Intelligent conversation  
        - 🧠 Context awareness
        - 📱 Modern tech interface
        - 🆓 Open-source technology
        
        **Languages:**
        - 🇬🇧 English
        - 🇮🇳 Tamil (தமிழ்)
        
        **Powered by:** Modern AI & Deep Learning
        """)
        
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.messages = []
            st.session_state.memory.clear()
            st.success("Chat cleared!")
            time.sleep(1)
            st.rerun()
            
    return direction

def process_translation(text: str, direction: str, translator: IndicTranslator):
    """Process translation based on direction"""
    if direction == "English → Tamil":
        source_lang, target_lang = "en", "ta"
        lang_display = "English to Tamil"
    else:
        source_lang, target_lang = "ta", "en"
        lang_display = "Tamil to English"
    
    # Show translation progress with tech styling
    with st.spinner(f'🤖 AI Processing {lang_display} Translation...'):
        translation = translator.translate(text, source_lang, target_lang)
        time.sleep(0.5)  # Small delay for better UX
    
    return translation

def render_chat_interface():
    """Render main chat interface"""
    translator = get_translator()
    direction = render_sidebar()
    
    # Main header with tech styling
    st.markdown("""
        <div style='text-align: center; padding: 20px;'>
            <h1 style='color: #ffffff; font-size: 3rem; text-shadow: 2px 2px 8px rgba(0,0,0,0.7);'>
                🤖 AI Neural Translator
            </h1>
            <h2 style='color: #00ff88; font-size: 1.5rem; text-shadow: 1px 1px 4px rgba(0,0,0,0.7);'>
                English ⟷ Tamil • Powered by AI Technology
            </h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"**Current Mode:** {direction}")
    st.info("🚀 Advanced AI Translation • Neural Network Processing • Real-time Results")
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    placeholder_text = "Type in English..." if direction == "English → Tamil" else "தமிழில் தட்டச்சு செய்யுங்கள்..."
    
    if prompt := st.chat_input(placeholder_text):
        # Validate input
        if not prompt.strip():
            st.error("Please enter some text to translate.")
            return
            
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Process translation
        with st.chat_message("assistant"):
            translation = process_translation(prompt, direction, translator)
            
            # Display result with formatting
            if translation.startswith("❌") or translation.startswith("Translation error") or translation.startswith("Please enter"):
                st.error(translation)
                response_content = translation
            else:
                st.success("**AI Translation:**")
                st.markdown(f"### {translation}")
                response_content = f"**AI Translation:** {translation}"
        
        # Add to chat history and memory
        st.session_state.messages.append({
            "role": "assistant",
            "content": response_content
        })
        
        # Update LangChain memory
        st.session_state.memory.chat_memory.add_user_message(prompt)
        st.session_state.memory.chat_memory.add_ai_message(translation)

def main():
    """Main application function"""
    # Set custom background
    set_custom_background()
    
    initialize_session_state()
    
    # Display welcome message for new users
    if len(st.session_state.messages) == 0:
        st.info("🤖 Welcome to AI Neural Translator! Start translating by typing in the chat box below.")
    
    render_chat_interface()

if __name__ == "__main__":
    main()
