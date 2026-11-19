import os
import pandas as pd

from src.resume_parser import parse_resume
from src.email_extractor import extract_email
from src.name_extractor import extract_name
from src.skill_extractor import extract_skills
from src.jd_skill_extractor import extract_jd_skills
from src.skill_matcher import match_skills
from src.similarity_engine import calculate_similarity


def screen_resumes(resume_folder, jd_text):

    results = []

    required_skills = extract_jd_skills(jd_text)

    for filename in os.listdir(resume_folder):

        file_path = os.path.join(resume_folder, filename)

        if filename.lower().endswith((".pdf", ".docx", ".txt")):

            resume_text = parse_resume(file_path)

            name = extract_name(resume_text)
            email = extract_email(resume_text)

            candidate_skills = extract_skills(resume_text)

            matched, missing, skill_score = match_skills(
                candidate_skills, required_skills
            )

            similarity_score = calculate_similarity(
                resume_text, jd_text
            )

            final_score = (skill_score * 0.70) + (
                similarity_score * 0.30
            )

            results.append({
                "Name": name,
                "Email": email,
                "Resume": filename,
                "Matched Skills": ", ".join(matched),
                "Missing Skills": ", ".join(missing),
                "Skill Score": round(skill_score, 2),
                "Similarity Score": round(similarity_score, 2),
                "Final Score": round(final_score, 2)
            })

    df = pd.DataFrame(results)

    if not df.empty:
        df = df.sort_values(
            by="Final Score",
            ascending=False
        ).reset_index(drop=True)

        df.insert(0, "Rank", range(1, len(df) + 1))

    return df