# app.py
import streamlit as st
from src.rag_model import RAGModel
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'rag_model' not in st.session_state:
    st.session_state.rag_model = RAGModel()

# Page configuration
st.set_page_config(
    page_title="Z.A.S - Zombie Apocalypse System",
    page_icon="☢️",
    layout="wide"
)

# Fallout-themed Custom CSS
st.markdown("""
<style>
    /* Global Styles */
    .stApp {
        background-color: #0C0C0C;
        color: #45FF45;
    }
    
    /* Terminal-like font */
    * {
        font-family: 'Courier New', Courier, monospace !important;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #45FF45 !important;
        text-transform: uppercase;
        border-bottom: 2px solid #45FF45;
        padding-bottom: 10px;
    }
    
    /* Terminal-like response box */
    .response-box {
        background-color: #0F1F0F;
        border: 2px solid #45FF45;
        padding: 20px;
        border-radius: 5px;
        margin: 10px 0;
        color: #45FF45;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #0F1F0F !important;
        color: #45FF45 !important;
        border: 2px solid #45FF45 !important;
        border-radius: 5px !important;
        font-weight: bold !important;
    }
    
    .stButton > button:hover {
        background-color: #45FF45 !important;
        color: #0C0C0C !important;
    }
    
    /* Text input */
    .stTextArea > div > div > textarea {
        background-color: #0F1F0F !important;
        color: #45FF45 !important;
        border: 2px solid #45FF45 !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #0F1F0F;
    }
    
    /* Status indicators */
    .status-online {
        color: #45FF45;
        animation: blink 1s infinite;
    }
    
    @keyframes blink {
        50% {
            opacity: 0;
        }
    }
    
    /* Custom divider */
    .divider {
        border-bottom: 2px solid #45FF45;
        margin: 20px 0;
    }
    
    /* Info boxes */
    .stAlert {
        background-color: #0F1F0F !important;
        color: #45FF45 !important;
        border: 2px solid #45FF45 !important;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Title with Fallout-style header
    st.markdown("""
        <h1 style='text-align: center; margin-bottom: 30px;'>
            ☢️ Z.A.S - ZOMBIE APOCALYPSE SYSTEM ☢️
        </h1>
        <p class='status-online' style='text-align: center;'>
            [SYSTEM ONLINE] - VAULT-TEC SURVIVAL PROTOCOL ACTIVATED
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.markdown("### SYSTEM STATUS")
        st.markdown("""
        <div class='response-box'>
        🟢 MAIN POWER: ONLINE<br>
        🟢 RAG SYSTEM: OPERATIONAL<br>
        🟢 SURVIVAL DATABASE: CONNECTED<br>
        ⚠️ THREAT LEVEL: SEVERE
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### COMMAND SUGGESTIONS")
        st.markdown("""
        <div class='response-box'>
        > LOCATE SAFE ZONE<br>
        > SCAN FOR SUPPLIES<br>
        > ANALYZE ESCAPE ROUTES<br>
        > CHECK MEDICAL RESOURCES
        </div>
        """, unsafe_allow_html=True)

    # Main content
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### ENTER SURVIVAL QUERY")
        query = st.text_area("INPUT COMMAND:", height=100)
        
        if st.button("PROCESS QUERY", type="primary"):
            if query:
                with st.spinner("ANALYZING SURVIVAL PARAMETERS..."):
                    try:
                        response = st.session_state.rag_model.process_query(query)
                        st.session_state.chat_history.append({
                            "question": query,
                            "answer": response
                        })
                        
                        st.markdown("### SYSTEM RESPONSE:")
                        st.markdown(f'<div class="response-box">{response}</div>', 
                                  unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"SYSTEM ERROR: {str(e)}")
            else:
                st.warning("ERROR: NO QUERY DETECTED")

    with col2:
        st.markdown("### TACTICAL ASSESSMENT")
        st.markdown("""
        <div class='response-box'>
        [SAFE ZONES]
        ✓ SCHOOL GYMNASIUM
        ✓ LIBRARY BASEMENT
        
        [DANGER ZONES]
        ⚠️ COLLAPSED BRIDGE
        ⚠️ MAJOR INTERSECTIONS
        
        [RESOURCES]
        🏥 CENTRAL HOSPITAL
        🚒 FIRE STATION
        </div>
        """, unsafe_allow_html=True)

    # Chat History
    if st.session_state.chat_history:
        st.markdown("### COMMAND HISTORY")
        for chat in st.session_state.chat_history:
            st.markdown(f"""
            <div class='response-box'>
            > QUERY: {chat['question']}<br>
            > RESPONSE: {chat['answer']}
            </div>
            """, unsafe_allow_html=True)

        # Download button
        chat_text = "\n\n".join([
            f"QUERY: {chat['question']}\nRESPONSE: {chat['answer']}"
            for chat in st.session_state.chat_history
        ])
        st.download_button(
            label="DOWNLOAD LOGS",
            data=chat_text,
            file_name="ZAS_survival_log.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()