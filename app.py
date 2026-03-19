import streamlit as st
import pandas as pd
import PyPDF2
import os
import spacy

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load NLP model
nlp = spacy.load("en_core_web_sm")



# Skill Keywords
skill_keywords = [
    "python",
    "machine learning",
    "deep learning",
    "sql",
    "data analysis",
    "pandas",
    "tensorflow",
    "nlp",
    "statistics",
    "java",
    "spring",
    "docker",
    "kubernetes",
    "aws",
    "flask",
    "django"
]


# Extract text from PDF

def extract_text_from_pdf(file_path):

    text = ""

    with open(file_path, "rb") as file:

        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text.lower()



# Extract skills using NLP

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skill_keywords:

        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills


# Recommendation logic

def get_recommendation(score):

    if score >= 75:
        return "Strong Fit"

    elif score >= 50:
        return "Moderate Fit"

    else:
        return "Not Fit"



# Streamlit UI

st.title("AI Resume Screening System")

st.write("Compare candidate resumes with a Job Description.")


job_description = st.text_area("Paste Job Description")

analyze = st.button("Analyze Resumes")



# Main Processing

if analyze:

    if job_description == "":
        st.warning("Please enter a job description")
        st.stop()

    resume_folder = "resumes"

    resumes_text = []
    resume_names = []

    # Read resumes
    for file in os.listdir(resume_folder):

        if file.endswith(".pdf"):

            path = os.path.join(resume_folder, file)

            text = extract_text_from_pdf(path)

            resumes_text.append(text)

            resume_names.append(file)


    # Combine JD + resumes
    documents = [job_description.lower()] + resumes_text


    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    jd_vector = tfidf_matrix[0]

    resume_vectors = tfidf_matrix[1:]


    similarity_scores = cosine_similarity(resume_vectors, jd_vector)


    results = []


    # Extract JD skills
    jd_skills = extract_skills(job_description.lower())


    for i, score in enumerate(similarity_scores):

        resume_text = resumes_text[i]

        resume_skills = extract_skills(resume_text)


        strengths = [s for s in resume_skills if s in jd_skills]

        gaps = [s for s in jd_skills if s not in resume_skills]


        #strengths = strengths[:3]
        #gaps = gaps[:3]


        # TF-IDF similarity score
        tfidf_score = score[0] * 100


        # Skill match score
        skill_match_count = len(strengths)
        total_required = len(jd_skills)


        if total_required > 0:
            skill_score = (skill_match_count / total_required) * 100
        else:
            skill_score = 0


        # Final Score
        final_score = round((0.7 * skill_score) + (0.3 * tfidf_score), 2)


        # If all skills match → Strong Fit
        if skill_match_count == total_required and total_required > 0:
            recommendation = "Strong Fit"
        else:
            recommendation = get_recommendation(final_score)


        results.append({

            "Candidate": resume_names[i],
            "Match Score": final_score,
            "Strengths": ", ".join(strengths),
            "Gaps": ", ".join(gaps),
            "Recommendation": recommendation

        })


    # Create DataFrame
    df = pd.DataFrame(results)


    # Rank candidates
    df = df.sort_values(by="Match Score", ascending=False)


    # Top candidate
    top_candidate = df.iloc[0]["Candidate"]
    top_score = df.iloc[0]["Match Score"]


    st.success(f"Top Candidate: {top_candidate}  (Score: {top_score})")


    st.subheader("Candidate Ranking")

    st.dataframe(df)


    # Skill summary
    st.markdown("## Candidate Ranking")
    for index, row in df.iterrows():

        st.write(
            f"{row['Candidate']} → Strengths: {row['Strengths']} | Gaps: {row['Gaps']}"
        )


    # Download CSV
    csv = df.to_csv(index=False)

    st.download_button(
        label="Download Results",
        data=csv,
        file_name="resume_screening_results.csv",
        mime="text/csv"
    )