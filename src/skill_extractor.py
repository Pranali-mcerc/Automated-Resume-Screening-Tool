def extract_skills(text):

    skills_list = [
        "Python",
        "Java",
        "C++",
        "SQL",
        "HTML",
        "CSS",
        "JavaScript",
        "Pandas",
        "NumPy",
        "Matplotlib",
        "Machine Learning",
        "Deep Learning",
        "Data Analysis",
        "Power BI",
        "Tableau",
        "Excel",
        "Scikit-learn",
        "TensorFlow",
        "PyTorch",
        " NLP",
        "Flask",
        "Django",
        "Git",
        "GitHub"
    ]

    extracted_skills = []

    text_lower = text.lower()

    for skill in skills_list:

        if skill.lower() in text_lower:
            extracted_skills.append(skill)

    return extracted_skills