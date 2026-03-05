import streamlit as st
from typing import Dict, List
from openai import OpenAI
import os
from dotenv import load_dotenv
# -----------------------------
# OPENAI CLIENT
# -----------------------------


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("OPENAI_API_KEY not found in .env file")
    st.stop()

client = OpenAI(api_key=api_key)

# -----------------------------
# LLM CALL
# -----------------------------
def call_llm(master_cv: str, job: Dict) -> str:

    prompt = f"""
SYSTEM INSTRUCTIONS:

You are an expert resume and cover letter writer.

You are given:
1. A candidate CV
2. A job description

Your job:
- Rewrite the CV tailored to the job
- Write a cover letter (max 350 words)

Rules:
- Do NOT invent skills or experience
- Mirror terminology from the job description
- Optimize for ATS
- Highlight relevant projects
- Professional tone

Candidate CV:
{master_cv}

Job Information

Company: {job['company_name']}
Title: {job['job_title']}
Location: {job['location']}
Company Description:
{job['company_description']}

Job Description:
{job['job_description']}

OUTPUT FORMAT

====================================================
JOB: {job['company_name']} – {job['job_title']}
====================================================

----- TAILORED CV -----
[CV]

----- COVER LETTER -----
[LETTER]
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.4,
        messages=[
            {"role": "system", "content": "You are a professional resume writer."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


# -----------------------------
# STREAMLIT UI
# -----------------------------
st.set_page_config(page_title="AI Job Application Generator", layout="wide")

st.title("AI CV + Cover Letter Generator")

st.write(
    "Generate tailored CVs and cover letters for multiple jobs."
)

# -----------------------------
# MASTER CV
# -----------------------------
st.header("1️⃣ Master CV")

master_cv = st.text_area(
    "Paste your full CV",
    height=300
)

# -----------------------------
# JOB INPUT
# -----------------------------
st.header("2️⃣ Job Information")

num_jobs = st.number_input(
    "Number of jobs to generate for",
    min_value=1,
    max_value=10,
    value=1
)

jobs: List[Dict] = []

for i in range(num_jobs):

    st.subheader(f"Job {i+1}")

    col1, col2 = st.columns(2)

    with col1:
        company = st.text_input(f"Company {i}", key=f"company{i}")
        title = st.text_input(f"Job Title {i}", key=f"title{i}")
        location = st.text_input(f"Location {i}", key=f"location{i}")

    with col2:
        url = st.text_input(f"Job URL {i}", key=f"url{i}")
        company_desc = st.text_area(
            f"Company Description {i}",
            key=f"companydesc{i}"
        )

    job_desc = st.text_area(
        f"Job Description {i}",
        height=200,
        key=f"jobdesc{i}"
    )

    jobs.append({
        "company_name": company,
        "job_title": title,
        "location": location,
        "company_description": company_desc,
        "job_description": job_desc,
        "job_url": url
    })


# -----------------------------
# GENERATE BUTTON
# -----------------------------
st.header("3️⃣ Generate Applications")

if st.button("Generate Applications"):

    if not master_cv:
        st.error("Paste your CV first.")
        st.stop()

    results = []

    progress = st.progress(0)

    for i, job in enumerate(jobs):

        with st.spinner(f"Generating for {job['company_name']}..."):

            output = call_llm(master_cv, job)

            results.append(output)

        progress.progress((i + 1) / len(jobs))

    st.success("Generation Complete")

    # -----------------------------
    # DISPLAY RESULTS
    # -----------------------------
    st.header("Results")

    full_output = "\n\n".join(results)

    st.text_area(
        "Generated Applications",
        full_output,
        height=600
    )

    st.download_button(
        label="Download Results",
        data=full_output,
        file_name="applications.txt"
    )
