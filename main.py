from src.resume_parser import parse_resume
from src.email_extractor import extract_email
from src.name_extractor import extract_name
from src.skill_extractor import extract_skills
from src.jd_skill_extractor import extract_jd_skills
from src.skill_matcher import match_skills
from src.similarity_engine import calculate_similarity

# Resume path
file_path = "data/sample_resume.txt"

# Read resume
resume_text = parse_resume(file_path)

# Extract details
name = extract_name(resume_text)
email = extract_email(resume_text)
candidate_skills = extract_skills(resume_text)

# Read Job Description
with open("data/job_description.txt", "r", encoding="utf-8") as file:
    jd_text = file.read()

# Extract required skills
required_skills = extract_jd_skills(jd_text)

# Match skills
matched_skills, missing_skills, skill_score = match_skills(
    candidate_skills, required_skills
)

# Text similarity
similarity_score = calculate_similarity(resume_text, jd_text)

# Combined score
final_score = (skill_score * 0.70) + (similarity_score * 0.30)

# Display results
print("=" * 50)
print("       AUTOMATED RESUME SCREENING TOOL")
print("=" * 50)

print("\nCandidate Name:", name)
print("Candidate Email:", email)

print("\nRequired Skills:", required_skills)
print("\nMatched Skills:", matched_skills)
print("\nMissing Skills:", missing_skills)

print("\nSkill Match Score:", round(skill_score, 2), "%")
print("Text Similarity Score:", round(similarity_score, 2), "%")
print("Final Combined Score:", round(final_score, 2), "%")

if final_score >= 75:
    print("Candidate Status: Shortlisted")

elif final_score >= 50:
    print("Candidate Status: Under Review")

else:
    print("Candidate Status: Not Shortlisted")

print("=" * 50)