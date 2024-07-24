__import__('pysqlite3')
import sys

sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')



import streamlit as st
from main import ask


# page config
st.set_page_config(page_title="Bible_Bot-Thomas", page_icon="📖")  # Icône de Bible



# message initiation
if 'messages' not in st.session_state:
    st.session_state.messages = []


def add_message(message, is_user):
    st.session_state.messages.append({"message": message, "is_user": is_user})



# Interface 
st.title("Thomas")
st.write("Salut, je suis Thomas et je réponds à toutes tes questions concernant la Bible")
st.write("Je suis expert en théologie et maîtrise l'histoire de la Bible. Je peux répondre à tes questions sur la Bible, notamment sur son histoire, ses personnages, ses thèmes et son impact sur la culture et la société.Je peux également t'aider à trouver des versets bibliques spécifiques et à comprendre leur contexte et leur signification.")

# CSS 
st.markdown("""
            
    <link href="https://fonts.googleapis.com/css2?family=Lora:wght@400;700&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
    .user-message {
        font-family: "Noto Serif';
        font-size: 16px;
        color: black;
        font-weight: None;
        background-color: white;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 5px;

    }
    .bot-message {
        font-family: 'Merriweather', serif;
        font-size: 16px;
        color: black;
        font-weight: None;
        background-color: #E0F7FA;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 5px;
    }
    .footer {
        font-family: 'Noto Serif', serif;
        font-size: 14px;
        color: #555555;
        text-align: center;
        margin-top: 100px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# previious messages
for msg in st.session_state.messages:
    if msg["is_user"]:
        st.markdown(f'<div class="user-message">Moi✨: {msg["message"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-message">Thomas📖📖: {msg["message"]}</div>', unsafe_allow_html=True)



user_input = st.text_input("Pose ta question ici:")

# Button
if st.button("Envoyer"):
    if user_input:
        add_message(user_input, is_user=True)  # Ajouter le message de l'utilisateur
        response = ask(user_input)
        add_message(response, is_user=False)   # Ajouter la réponse du chatbot
        st.experimental_rerun()  # Recharger la page pour afficher les nouveaux messages
    else:
        st.write("Autre chose à me demander ? Pose ta question.")



if not user_input:
    st.write("J'ai hâte de t'aider")







# bio
# 
linkedin_url = "https://www.linkedin.com/in/ghilth/"
st.markdown(f'<div class="footer">Made by <a href="{linkedin_url}" target="_blank" style="color: brown; text-style : italic;">Ghilth GBAGUIDI</a></div>', unsafe_allow_html=True)
