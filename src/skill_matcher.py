def match_skills(candidate_skills, required_skills):

    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill in candidate_skills:
            matched_skills.append(skill)

        else:
            missing_skills.append(skill)

    if required_skills:
        match_percentage = (len(matched_skills) / len(required_skills)) * 100

    else:
        match_percentage = 0

    return matched_skills, missing_skills, match_percentage