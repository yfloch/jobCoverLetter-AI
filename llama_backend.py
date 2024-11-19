from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Configuration du modèle Ollama avec Llama 3.2
model = OllamaLLM(model="llama3.2")

# Template pour l'analyse du CV en fonction de l'offre d'emploi
template = """
You are an AI assistant specialized in evaluating resumes (CVs) against job descriptions. Your goal is to provide a detailed analysis that helps recruiters or candidates assess the alignment between a CV and a job posting.

Use the following structure to analyze the data:

1. **Matching Score**:
   - Calculate a matching score between **0 and 100** based on the alignment of the candidate's skills, experience, and qualifications with the job description.

2. **Strengths**:
   - List the key strengths of the candidate that make them a good match for the job.

3. **Missing Qualifications or Skills**:
   - Identify the qualifications, skills, or experience that the candidate lacks to fully meet the job requirements.

4. **Suggestions for Improvement**:
   - Provide actionable recommendations to improve the CV so that it better aligns with the job description.

### Job Description:
{jobDescription}

### Candidate's CV:
{candidateCV}

### Provide your analysis in this structured format:
---
### Matching Score:
XX/100

### Strengths:
- [Key strengths relevant to the job]

### Missing Qualifications or Skills:
- [List of missing elements]

### Suggestions for Improvement:
- [Actionable suggestions]
"""

def evaluate_cv_with_job_offer(job_offer: str, cv_text: str) -> str:
    """
    Utilise le modèle Ollama pour évaluer le CV par rapport à l'offre d'emploi.
    
    Args:
        job_offer (str): Description de l'offre d'emploi.
        cv_text (str): Contenu du CV.
    
    Returns:
        str: Résultat structuré de l'analyse.
    """
    # Créer le prompt final à partir du template
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    # Envoyer le prompt au modèle pour une évaluation
    try:
        response = chain.invoke(
            {"jobDescription": job_offer, "candidateCV": cv_text}
            )
        return response
    except Exception as e:
        return f"Erreur lors de l'évaluation avec le modèle : {str(e)}"
