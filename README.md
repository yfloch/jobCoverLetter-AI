# Job Cover Letter AI

Job Cover Letter AI is an intelligent Cover Letter Writer tool that helps job seekers to write a good Cover Letter Draft based on a job description and a Resume. Using advanced AI technology powered by Llama 3.2, it provides a 3 drafts.

## Features

- **CV Upload**: Support for PDF format CVs
- **Job Description Analysis**: Paste any job description for analysis
- **Cover Letter writing

## Prerequisites

- Python 3.x
- Ollama with Llama 3.2 model installed
- PDF files for CV analysis

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/jobfit-ai.git
cd jobfit-ai
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure Ollama is installed and the Llama 3.2 model is available.

## Usage

1. Start the application:
```bash
streamlit run main.py
```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Use the interface to:
   - Paste the job description
   - Upload a CV in PDF format
   - Click "Generate Draft" to get the analysis

## Dependencies

- streamlit: Web application framework
- python-dotenv: Environment variable management
- langchain: LLM framework
- PyPDF2: PDF processing
- langchain_ollama: Ollama integration

## Project Structure

- `main.py`: Main application file with Streamlit interface
- `llama_backend.py`: Backend logic for Cover Letter Draft Generation
- `requirements.txt`: Project dependencies
- `README.md`: Project documentation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
