# 🤖 AI Job Application Generator

> Automate your entire job search — from scraping listings to generating tailored CVs and cover letters — powered by LLMs and Streamlit.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI_API-412991?style=flat&logo=openai&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=flat&logo=selenium&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=flat)

---

## 📌 Overview

Job hunting is repetitive and time-consuming. This project automates the entire workflow:

1. **Scrape** LinkedIn job postings with Selenium
2. **Analyse** job market trends with EDA
3. **Generate** tailored CVs and cover letters using an LLM
4. **Deploy** everything through a clean Streamlit interface

---

## 🔁 Pipeline

```
LinkedIn Scraper → Job Dataset → EDA → LLM Generator → Streamlit App
```

---

## ✨ Features

- 🔍 Scrape LinkedIn job postings by role and location
- 📊 Analyse hiring trends, keywords, and remote vs on-site patterns
- 🧠 Generate tailored CVs matched to specific job descriptions
- ✉️ Generate personalised cover letters per company
- 💻 Simple Streamlit UI — paste your CV, get your applications
- 📥 Download generated documents directly from the app

---

## 🗂️ Project Structure

```
project/
│
├── webscraping_linkedin.ipynb   # LinkedIn job scraper
├── EDA.ipynb                    # Exploratory data analysis
├── LLM_cover+CV.ipynb           # LLM prompt engineering & generation
├── app.py                       # Streamlit application
├── data/                        # Scraped job datasets
└── README.md
```

---

## 🧩 Components

### 🔎 Web Scraper
Collects LinkedIn job postings using **Selenium + BeautifulSoup**.

Extracted fields:
- Job title, company name, location
- Full job description
- Company description

### 📈 Exploratory Data Analysis
Analyses trends in the scraped job dataset:
- Job distribution by location
- Remote vs on-site ratio
- Company hiring patterns
- Keyword frequency in job descriptions

### 🤖 LLM Application Generator
Uses the **OpenAI API** to generate personalised job applications.

**Inputs:** master CV + job description + company info  
**Outputs:** tailored CV + personalised cover letter

### 🖥️ Streamlit App
User-friendly interface to:
- Paste your CV
- Enter job descriptions
- Generate applications in one click
- Download results

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/gail-mar/final_project.git
cd final_project
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API key
Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_api_key_here
```

### 4. Run the app
```bash
streamlit run app.py
```

---

## 🔄 Example Workflow

1. Run `webscraping_linkedin.ipynb` to collect job postings
2. Run `EDA.ipynb` to explore the dataset
3. Open the Streamlit app
4. Paste your CV and a job description
5. Click **Generate** — get a tailored CV and cover letter instantly

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Selenium + BeautifulSoup | Web scraping |
| Pandas + Matplotlib | Data analysis & visualisation |
| OpenAI API | LLM-powered generation |
| Streamlit | Web app interface |

---

## 👩‍💻 Author

**Gail Marechal** — Data Science & AI  
[![GitHub](https://img.shields.io/badge/GitHub-gail--mar-181717?style=flat&logo=github)](https://github.com/gail-mar)

---

*Built as a final project for a Data Science & AI bootcamp.*
