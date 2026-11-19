from src.batch_screening import screen_resumes

# Read Job Description
with open("data/job_description.txt", "r", encoding="utf-8") as file:
    jd_text = file.read()

# Screen all resumes
results = screen_resumes("data/resumes", jd_text)

# Display ranking
print("\n========== CANDIDATE RANKING ==========\n")

if not results.empty:
    print(results.to_string(index=False))

    # Save report
    results.to_csv("screening_results.csv", index=False)

    print("\nReport saved: screening_results.csv")

else:
    print("No resumes found!")