import streamlit as st
import pandas as pd

career_data = pd.read_csv("careers.csv")

st.set_page_config(
    page_title="Student Skill Analyzer",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Skill & Internship Readiness Analyzer")

st.write(
    "Find your skill gaps, measure your internship readiness, "
    "and discover what you should learn next."
)

st.header("👤 Student Profile")

name = st.text_input("Enter your name")

department = st.selectbox(
    "Select your department",
    [
        "Bioinformatics",
        "Computer Science",
        "Information Technology",
        "Artificial Intelligence & Data Science",
        "Biotechnology",
        "Other"
    ]
)

year = st.selectbox(
    "Select your year",
    [
        "1st Year",
        "2nd Year",
        "3rd Year",
        "4th Year"
    ]
)

career = st.selectbox(
    "What is your target career?",
    [
        "Data Analyst",
        "Data Scientist",
        "AI Engineer",
        "Web Developer",
        "Healthcare Data Analyst"
    ]
)

st.write("### Your Profile")
st.write("Name:", name)
st.write("Department:", department)
st.write("Year:", year)
st.write("Career Goal:", career)
st.header("🛠️ Your Current Skills")

skills = st.multiselect(
    "Select the skills you currently have:",
    [
        "Python",
        "SQL",
        "Excel",
        "Pandas",
        "NumPy",
        "Statistics",
        "Power BI",
        "Machine Learning",
        "Data Visualization",
        "Communication",
        "Problem Solving",
        "HTML & CSS",
        "Java",
        "C/C++"
    ]
)

if skills:
    st.write("### ✅ Your Selected Skills")
    st.write(", ".join(skills))
else:
    st.info("Please select the skills you currently have.")
    st.header("📊 Internship Readiness Analysis")

if st.button("🔍 Analyze My Readiness"):

    if not name:
        st.warning("Please enter your name.")

    elif not skills:
        st.warning("Please select at least one skill.")

    else:
        required_skills = career_data[
            career_data["Career"] == career
        ]

        total_importance = required_skills["Importance"].sum()

        matched_importance = required_skills[
            required_skills["Skill"].isin(skills)
        ]["Importance"].sum()

        readiness_score = (
            matched_importance / total_importance
        ) * 100

        st.subheader("🎯 Your Internship Readiness")

        st.metric(
            "Readiness Score",
            f"{readiness_score:.0f}%"
        )

        st.write("### ✅ Skills You Already Have")

        matched_skills = required_skills[
            required_skills["Skill"].isin(skills)
        ]["Skill"].tolist()

        if matched_skills:
            for skill in matched_skills:
                st.success(skill)
        else:
            st.info("No required skills matched yet.")

        st.write("### 📚 Skills You Should Develop")

        missing_skills = required_skills[
            ~required_skills["Skill"].isin(skills)
        ].sort_values(
            by="Importance",
            ascending=False
        )["Skill"].tolist()

        if missing_skills:
            for skill in missing_skills:
                st.warning(skill)
        else:
            st.success("Amazing! You have all the required skills!")
