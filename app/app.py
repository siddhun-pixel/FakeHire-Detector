import streamlit as st
from src.model import train_model, predict
from src.feature_engineering import keyword_score, is_free_email, salary_flag
from src.explainability import explain

def run_app():
    st.title("FakeHire Detector 🛡️")
    st.write("Detect fake job & internship postings")

    job_desc = st.text_area("Job Description")
    email = st.text_input("Contact Email")
    salary = st.number_input("Salary / Stipend", 0)

    if st.button("Analyze"):
        train_model()
        result = predict(job_desc)

        keywords = keyword_score(job_desc)
        email_check = is_free_email(email)
        salary_check = salary_flag(salary)

        reasons = explain(result, keywords, email_check, salary_check)

        st.subheader("Result:")
        st.success(result.upper())

        st.subheader("Reasons:")
        for r in reasons:
            st.write("- ", r)

