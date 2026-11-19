import streamlit as st
import pandas as pd

from src.batch_screening import screen_resumes

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Automated Resume Screening Tool")
st.caption("AI-powered Resume Analysis & Candidate Ranking")

st.sidebar.header("Job Description")

jd_text = st.text_area(
    "Enter Job Description",
    height=250
)

uploaded_files = st.file_uploader(
    "Upload Resumes (PDF, DOCX, TXT)",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

if st.button("🚀 Screen Resumes"):

    if not jd_text:
        st.warning("Please enter Job Description.")

    elif not uploaded_files:
        st.warning("Please upload resumes.")

    else:
        import os

        os.makedirs("temp_resumes", exist_ok=True)

        for file in uploaded_files:
            file_path = os.path.join("temp_resumes", file.name)

            with open(file_path, "wb") as f:
                f.write(file.getbuffer())

        results = screen_resumes("temp_resumes", jd_text)

        if not results.empty:

            st.success("Resume Screening Completed!")

            st.metric("Total Candidates", len(results))

            st.dataframe(
                results,
                use_container_width=True
            )

                        # Candidate Score Visualization

            st.subheader("📊 Candidate Score Comparison")

            chart_data = results.set_index("Name")[
                ["Skill Score", "Similarity Score", "Final Score"]
            ]

            st.bar_chart(chart_data)

            st.subheader("🏆 Final Score Ranking")

            st.bar_chart(
                results.set_index("Name")["Final Score"]
            )

            st.subheader("🏆 Candidate Ranking")

            for _, row in results.iterrows():

                with st.expander(
                    f"Rank {row['Rank']} - {row['Name']} | "
                    f"{row['Final Score']}%"
                ):

                    st.write("Email:", row["Email"])
                    st.write("Matched Skills:", row["Matched Skills"])
                    st.write("Missing Skills:", row["Missing Skills"])
                    st.write("Skill Score:", row["Skill Score"], "%")
                    st.write("Similarity Score:", row["Similarity Score"], "%")

            csv = results.to_csv(index=False).encode("utf-8")

            st.download_button(
                "📥 Download Screening Report",
                data=csv,
                file_name="screening_results.csv",
                mime="text/csv"
            )

        else:
            st.warning("No resumes processed.")