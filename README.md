# AI Resume Screening System

## Overview

The AI Resume Screening System is a tool designed to automate the initial resume shortlisting process for recruiters. The system compares multiple candidate resumes with a given job description and ranks candidates based on their relevance.

The application extracts text from resumes, identifies relevant skills using Natural Language Processing (NLP), and computes similarity between resumes and the job description using TF-IDF vectorization and cosine similarity.

The output includes a match score, candidate ranking, key strengths, key gaps, and a final recommendation.

This project demonstrates how AI techniques can be applied to solve real-world recruitment problems.

---

## Features

- Automated resume analysis
- Job Description vs Resume comparison
- Skill extraction using NLP (spaCy)
- TF-IDF based similarity scoring
- Candidate ranking
- Identification of strengths and skill gaps
- Final recommendation:
  - Strong Fit
  - Moderate Fit
  - Not Fit
- Downloadable results (CSV)
- Simple interactive interface using Streamlit

---

## System Workflow

1. User inputs a Job Description.
2. The system reads multiple PDF resumes.
3. Text is extracted from each resume.
4. Skills are detected using keyword matching and NLP tokenization.
5. TF-IDF vectorization converts text into numerical vectors.
6. Cosine similarity calculates similarity between resumes and the job description.
7. The system computes:
   - Match score (0–100)
   - Strengths
   - Skill gaps
8. Candidates are ranked based on their score.
9. The top candidate is highlighted.

---

## Technologies Used

- Python
- Streamlit
- spaCy
- scikit-learn
- pandas
- PyPDF2

---

## Project Structure

ai-resume-screening-system
│
├── app.py
├── requirements.txt
├── README.md
│
└── resumes
    ├── resume1.pdf
    ├── resume2.pdf
    ├── resume3.pdf

---

## Installation

Clone the repository:

git clone https://github.com/Dharani-ThathiReddy/ai-resume-screening-system.git

Move into the project directory:

cd ai-resume-screening-system

Create a virtual environment (recommended):

python3 -m venv venv

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Install spaCy language model:

python -m spacy download en_core_web_sm

---

## Running the Application

Start the Streamlit app:

streamlit run app.py

Then open in your browser:

http://localhost:8501

---

## Example Input

Job Description example:

We are hiring a Machine Learning Engineer.

Required Skills:
Python
Machine Learning
TensorFlow
NLP
SQL

---

## Example Output

Candidate | Match Score | Strengths | Gaps | Recommendation
--------- | ----------- | --------- | ---- | --------------
resume2.pdf | 82 | python, machine learning, tensorflow | sql | Strong Fit
resume1.pdf | 65 | python, machine learning | tensorflow | Moderate Fit

---

## Future Improvements

- Resume upload directly from UI
- More advanced skill extraction using transformer models
- Integration with ATS systems
- Visualization dashboard for HR analytics

---

## Author

Dharani Thathireddy

---

## License

This project is for educational and internship assessment purposes.
