AI Job Application Generator

Automates the job application workflow by combining web scraping, data analysis, and generative AI.

The system collects job postings, analyzes job market trends, and generates tailored CVs and cover letters for specific job descriptions.

Project Pipeline
LinkedIn Scraper → Job Dataset → EDA → LLM Generator → Streamlit App

The project moves from data collection → analysis → automated application generation.

Features

Scrape LinkedIn job postings

Analyze job market trends

Generate tailored CVs

Generate personalized cover letters

Streamlit interface for easy usage

Generate applications for multiple jobs

Project Structure
project/
│
├── webscraping_linkedin.ipynb   # job scraper
├── EDA.ipynb                    # data analysis
├── LLM_cover+CV.ipynb           # LLM prompt system
├── app.py                       # Streamlit application
├── data/                        # scraped datasets
└── README.md
Components
Web Scraper

Collects LinkedIn job postings using Selenium.

Extracted information:

job title

company name

location

job description

company description

Exploratory Data Analysis

Analyzes trends in the job dataset.

Examples:

job distribution by location

remote vs on-site roles

company hiring patterns

keyword frequency in job descriptions

LLM Application Generator

Uses a Large Language Model to generate job applications.

Inputs:

master CV

job description

company information

Outputs:

tailored CV

personalized cover letter

Streamlit Application

A web interface that allows users to:

paste their CV

enter job information

generate applications automatically

download results

Installation

Clone the repository

git clone https://github.com/yourusername/ai-job-application-generator.git
cd ai-job-application-generator

Install dependencies

pip install -r requirements.txt

Create .env

OPENAI_API_KEY=your_api_key
Run the App
streamlit run app.py
Example Workflow

Scrape LinkedIn job postings

Analyze the dataset with EDA

Paste your CV into the Streamlit app

Enter job descriptions

Generate tailored applications

Technologies

Python
Selenium
BeautifulSoup
Pandas
Matplotlib
OpenAI API
Streamlit

Author

Gail Marechal
