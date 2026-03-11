import streamlit as st
import os

# Configuration de la page
st.set_page_config(
    page_title="Le Cockpit - DYNIA",
    page_icon="🚀",
    layout="centered"
)

# --- CHARTE GRAPHIQUE DYNIA (CSS Personnalisé) ---
st.markdown("""
    <style>
    :root {
        --brand-deep: #0c2461;
        --brand-primary: #1e3799;
        --brand-medium: #4a69bd;
        --brand-light: #f0f7ff;
    }
    
    .main {
        background-color: #f8fafc;
    }
    
    h1 {
        color: var(--brand-deep) !important;
        font-weight: 800 !important;
    }
    
    .stProgress > div > div > div > div {
        background-color: var(--brand-primary);
    }
    
    .tool-card {
        background-color: white;
        padding: 2rem;
        border-radius: 1.5rem;
        border: 1px solid #e2e8f0;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .nickname-tag {
        background-color: var(--brand-light);
        color: var(--brand-deep);
        padding: 0.2rem 0.6rem;
        border-radius: 0.5rem;
        font-size: 0.7rem;
        font-weight: bold;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 0.5rem;
    }
    
    .install-button {
        background-color: var(--brand-deep);
        color: white !important;
        padding: 0.6rem 1.2rem;
        border-radius: 0.8rem;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        margin-top: 1rem;
        transition: transform 0.2s;
    }
    
    .install-button:hover {
        transform: scale(1.05);
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- EN-TÊTE AVEC LOGO ---
col_logo, col_title, col_help = st.columns([1.5, 3, 1])

with col_logo:
    if os.path.exists("logo.png"):
        st.image("logo.png", use_container_width=True)
    else:
        st.info("Logo.png manquant")

with col_title:
    st.title("Le Cockpit")

with col_help:
    st.markdown(f"""
        <a href="mailto:thomas@dynia.fr" style="text-decoration:none;">
            <button style="
                border-radius:20px; 
                border:1px solid #cbd5e1; 
                padding:8px 16px; 
                cursor:pointer; 
                background:white;
                font-weight:500;
                color:#475569;
                width:100%;">
                🆘 Aide
            </button>
        </a>
    """, unsafe_allow_html=True)

# --- DONNÉES DES OUTILS (ORDRE MIS À JOUR) ---
TOOLS = [
    {
        "id": "warp",
        "name": "Warp",
        "nickname": "Le Centre de Commande",
        "analogy": "Warp est comme un assistant intelligent qui vous aide à donner des ordres directs à l'ordinateur.",
        "benefit": "Il se souvient des commandes complexes pour vous et rend la communication fluide.",
        "url": "https://www.warp.dev/",
        "steps": [
            "Cliquez sur le bouton 'Download' sur le site de Warp.",
            "Installez l'application et inscrivez-vous avec votre e-mail.",
            "Suivez la courte 'Visite de Bienvenue'."
        ]
    },
    {
        "id": "claude",
        "name": "Claude Code",
        "nickname": "Le Cerveau IA",
        "analogy": "Claude Code est comme un assistant qui peut accomplir des tâches complexes en français courant.",
        "benefit": "Il peut lire l'intégralité de votre projet et résoudre de gros problèmes en quelques secondes.",
        "url": "https://www.anthropic.com/claude",
        "steps": [
            "Ouvrez votre nouveau 'Centre de Commande' (Warp).",
            "Tapez la commande d'installation fournie par Thomas.",
            "Tapez 'claude' et appuyez sur Entrée pour commencer."
        ]
    },
    {
        "id": "n8n",
        "name": "n8n",
        "nickname": "L'Usine à Automatisations",
        "analogy": "n8n est comme un chef d'orchestre qui fait travailler vos applications ensemble automatiquement.",
        "benefit": "Il permet de créer des workflows intelligents pour gagner des heures de travail répétitif chaque semaine.",
        "url": "https://n8n.io/",
        "steps": [
            "Créez un compte sur n8n.io ou installez-le localement via Warp.",
            "Connectez vos premières applications (Google, Slack, etc.).",
            "Importez votre premier workflow de test fourni par Thomas."
        ]
    },
    {
        "id": "github",
        "name": "GitHub",
        "nickname": "La Bibliothèque Mondiale",
        "analogy": "GitHub est comme une bibliothèque magique où vous rangez vos projets pour ne jamais les perdre.",
        "benefit": "Il garde une trace de chaque changement et permet de partager votre travail en sécurité.",
        "url": "https://github.com/",
        "steps": [
            "Créez un compte gratuit sur le site officiel de GitHub.",
            "Téléchargez 'GitHub Desktop' pour gérer vos projets.",
            "Connectez votre compte GitHub pour sauvegarder votre travail."
        ]
    }
]

# --- INITIALISATION DE L'ÉTAT ---
if 'completed_steps' not in st.session_state:
    st.session_state.completed_steps = {}

st.markdown("""
    ### Bienvenue dans votre centre de commande !
    Avant de commencer à automatiser, nous devons configurer vos outils essentiels. 
    Suivez le guide ci-dessous étape par étape.
""")

# --- BARRE DE PROGRESSION ---
total_steps = sum(len(t["steps"]) for t in TOOLS)
completed_count = sum(1 for step_id, done in st.session_state.completed_steps.items() if done)
progress = completed_count / total_steps if total_steps > 0 else 0

st.write(f"**Votre Progression :** {completed_count} sur {total_steps} étapes complétées")
st.progress(progress)

st.divider()

# --- AFFICHAGE DES OUTILS ---
for tool in TOOLS:
    with st.container():
        st.markdown(f"""
            <div class="tool-card">
                <div class="nickname-tag">{tool['nickname']}</div>
                <h2 style="margin-top:0;">{tool['name']}</h2>
                <p style="font-style: italic; color: #64748b; font-size: 1.1rem;">"{tool['analogy']}"</p>
                <p><b>Pourquoi ?</b> {tool['benefit']}</p>
                <a href="{tool['url']}" target="_blank" class="install-button">Configurer {tool['name']}</a>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("### 🛠️ Étapes à suivre")
        for i, step in enumerate(tool['steps']):
            step_key = f"{tool['id']}_step_{i}"
            is_done = st.checkbox(step, key=step_key, value=st.session_state.completed_steps.get(step_key, False))
            st.session_state.completed_steps[step_key] = is_done
        
        st.markdown("<br>", unsafe_allow_html=True)

# --- PIED DE PAGE ---
st.divider()
st.markdown(f"""
    <div style="text-align: center; padding: 40px 20px; background-color: #f1f5f9; border-radius: 1.5rem;">
        <h3 style="color: var(--brand-deep);">Besoin d'un coup de main ?</h3>
        <p style="color: #475569;">Thomas est à votre disposition pour vous aider à finaliser votre installation.</p>
        <br>
        <a href="mailto:thomas@dynia.fr" style="
            background-color: var(--brand-primary); 
            color: white; 
            padding: 12px 30px; 
            border-radius: 12px; 
            text-decoration: none; 
            font-weight: bold;
            box-shadow: 0 10px 15px -3px rgba(30, 55, 153, 0.3);">
            Envoyer un message à Thomas
        </a>
    </div>
    <div style="text-align: center; padding: 20px; color: #94a3b8; font-size: 0.8rem;">
        © 2024 DYNIA - Le Cockpit Onboarding
    </div>
""", unsafe_allow_html=True)

if progress == 1.0:
    st.balloons()
    st.success("🎉 Félicitations ! Votre Cockpit est prêt. Place à l'automatisation !")
