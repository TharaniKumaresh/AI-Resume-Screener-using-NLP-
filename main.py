from src.extract_text import extract_resumes, extract_job_description
from src.preprocess import preprocess_text
from src.score_match import compute_similarity

# Extract text
resume_texts = extract_resumes("data/resumes")
job_desc = extract_job_description("data/job_description.txt")

# Preprocess
preprocessed_resumes = [preprocess_text(text) for text in resume_texts]
preprocessed_job_desc = preprocess_text(job_desc)

# Score
scores = compute_similarity(preprocessed_job_desc, preprocessed_resumes)

# Output
for idx, score in enumerate(scores):
    print(f"Resume {idx + 1} - Score: {round(score * 100, 2)}%")