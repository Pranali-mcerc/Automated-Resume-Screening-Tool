from src.skill_extractor import extract_skills


def extract_jd_skills(jd_text):
    required_skills = extract_skills(jd_text)

    return required_skills