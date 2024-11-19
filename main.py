import streamlit as st
from PyPDF2 import PdfReader
from llama_backend import evaluate_cv_with_job_offer  # Importer la fonction backend

# Titre de l'application
st.title("jobFit AI - CV Evaluation Tool")

# Zone de texte pour entrer l'offre d'emploi
st.subheader("Entrez l'offre d'emploi")
job_offer = st.text_area("Copiez et collez ici la description de l'offre d'emploi :", height=200)

# Zone pour uploader le CV au format PDF
st.subheader("Téléchargez le CV (format PDF)")
uploaded_file = st.file_uploader("Choisissez un fichier PDF :", type=["pdf"])

# Action après téléchargement
cv_text = ""
if uploaded_file is not None:
    # Lecture et extraction du contenu du fichier PDF
    pdf_reader = PdfReader(uploaded_file)
    for page in pdf_reader.pages:
        cv_text += page.extract_text()
    
    # Afficher un aperçu du contenu extrait
    st.subheader("Contenu extrait du CV")
    st.text_area("Aperçu du contenu extrait :", cv_text, height=200)

# Bouton pour lancer l'évaluation
if st.button("Évaluer le CV"):
    if not job_offer.strip():
        st.error("Veuillez entrer une offre d'emploi.")
    elif not cv_text.strip():
        st.error("Veuillez télécharger un CV valide.")
    else:
        st.info("Évaluation en cours...")
        try:
            # Appeler la fonction d'évaluation du backend
            evaluation_result = evaluate_cv_with_job_offer(job_offer, cv_text)
            
            # Afficher les résultats de l'évaluation
            st.subheader("Résultat de l'évaluation")
            st.text(evaluation_result)
        except Exception as e:
            st.error(f"Erreur lors de l'évaluation : {str(e)}")
