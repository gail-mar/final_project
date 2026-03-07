AI Job Application Generator

An end-to-end pipeline that collects job postings, analyzes job market trends, and automatically generates tailored CVs and cover letters using a Large Language Model (LLM).

The project combines web scraping, exploratory data analysis, prompt engineering, and a Streamlit application to streamline the job application process.

Project Architecture
LinkedIn Web Scraper
        │
        ▼
   Job Dataset
        │
        ▼
Exploratory Data Analysis
        │
        ▼
LLM CV + Cover Letter Generator
        │
        ▼
 Streamlit Web Application

The pipeline transforms job postings into automated, tailored job applications.

Features

Scrape LinkedIn job postings

Analyze job market trends

Generate tailored CVs

Generate personalized cover letters

Web application interface using Streamlit

Generate applications for multiple jobs simultaneously

Project Structure
project/
│
├── webscraping_linkedin.ipynb
│   LinkedIn job scraper
│
├── EDA.ipynb
│   Exploratory data analysis of scraped jobs
│
├── LLM_cover+CV.ipynb
│   LLM prompt system for generating CVs and cover letters
│
├── app.py
│   Streamlit application interface
│
├── data/
│   scraped job datasets
│
├── requirements.txt
│   project dependencies
│
└── README.md
1 LinkedIn Job Scraper

The scraper collects job postings from LinkedIn using Selenium and BeautifulSoup.

Collected information

Job title

Company name

Location

Job description

Company description

Filters

Job title (Data Scientist)

Location

Experience level

Remote work

Recent postings

The scraper stores results in a structured dataset (CSV).

2 Exploratory Data Analysis

EDA is used to explore patterns in the job market.

Analysis includes

Job distribution by location

Remote vs on-site roles

Company hiring patterns

Job description length

Keyword and skill patterns

Tools

Pandas

Matplotlib

Seaborn

The analysis helps understand demand trends in the data science job market.

3 LLM CV & Cover Letter Generator

This component uses a Large Language Model to generate tailored job applications.

Inputs

Master CV

Job description

Company information

Prompt Design

The prompt instructs the model to:

Rewrite the CV to match the job

Write a professional cover letter

Mirror terminology from the job posting

Highlight relevant skills

Avoid inventing experience

Output

For each job posting the system generates:

Tailored CV

Personalized cover letter

4 Streamlit Application

A Streamlit web application makes the system easy to use.

Instead of running notebooks, users interact with a simple interface.

Interface Features

Paste a master CV

Enter job information

Generate applications for multiple jobs

View generated CV and cover letter

Download generated applications

This turns the project into a practical application instead of just a script.

Installation
1 Clone the repository
git clone https://github.com/yourusername/ai-job-application-generator.git
cd ai-job-application-generator
2 Install dependencies
pip install -r requirements.txt
3 Add OpenAI API key

Create a .env file:

OPENAI_API_KEY=your_api_key_here
Running the Application

Run the Streamlit app:

streamlit run app.py

The app will open in your browser.

Example Workflow

Scrape job postings from LinkedIn

Explore job market patterns using EDA

Paste your master CV into the Streamlit app

Enter job descriptions

Generate tailored CVs and cover letters

Future Improvements

Skill extraction using NLP

Resume scoring against job descriptions

PDF export of applications

Automatic job scraping pipeline

Integration with job boards

Technologies

Programming

Python

Web Scraping

Selenium

BeautifulSoup

Data Analysis

Pandas

Matplotlib

Seaborn

AI

OpenAI API

Prompt Engineering

Application

Streamlit