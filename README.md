# Automated Resume Shortlisting using NLP & ML

This project applies **Natural Language Processing (NLP)** and **Machine Learning (ML)** to automate resume shortlisting based on job descriptions.  
It reduces manual effort in candidate screening by matching resumes to job requirements efficiently.

## 🚀 Features
- 📄 **Resume Parsing** from PDF/DOCX formats
- 🧠 **NLP-based keyword extraction** from resumes & job descriptions
- 📊 **Cosine Similarity / TF-IDF** matching to rank candidates
- 📈 Generates shortlist based on highest similarity scores
- 🖥 Simple interface for uploading job descriptions and resumes

## 🛠 Tech Stack
- Python (Pandas, NumPy, Scikit-learn, NLTK, SpaCy)
- Flask / Streamlit for UI
- PDFPlumber / Docx2txt for resume extraction
- Scikit-learn for ML algorithms

## 📂 Project Structure
resume-shortlisting/
│── app.py # Main application file
│── requirements.txt # Python dependencies
│── templates/ # HTML templates (for Flask)
│── static/ # CSS/JS assets
│── data/ # Sample resumes & job descriptions
│── models/ # Trained ML models
│── README.md # Project documentation

## ⚙️ How It Works
1. **Upload Resumes** and a **Job Description**.
2. **Text Preprocessing**:
   - Tokenization, stopword removal, lemmatization
   - TF-IDF vectorization
3. **Matching Algorithm**:
   - Calculates similarity between resumes & job description
   - Ranks resumes based on relevance score
4. **Output**:
   - Displays shortlisted candidates with their similarity score

## 📌 Purpose
Reduce time and effort in recruitment by automating resume filtering and providing a ranked shortlist for recruiters.

