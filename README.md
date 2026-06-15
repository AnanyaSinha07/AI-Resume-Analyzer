# AI Resume Analyzer

AI Resume Analyzer is a Django-based web application that analyzes resumes and compares them against a job description to calculate an ATS (Applicant Tracking System) score.

## Features

* Upload PDF resumes
* Extract resume text using PyPDF2
* Extract candidate details:

* Name
* Email
* Phone Number
* Detect technical skills from the resume
* Compare resume skills with job description skills
* Calculate ATS Score
* Show matched skills
* Show missing skills

## Tech Stack

* Python
* Django
* HTML
* CSS
* PyPDF2
* SQLite

## How It Works

1. Upload a PDF resume.
2. Enter a job description.
3. The system extracts resume content.
4. Skills are identified from both the resume and job description.
5. An ATS score is calculated based on skill matching.
6. The user receives:

   * ATS Score
   * Matched Skills
   * Missing Skills

## Future Improvements

* ATS Progress Bar
* Resume Recommendations
* Database Storage
* Advanced Skill Matching
* Resume Ranking
* Deployment on Cloud

## Author

Ananya Sinha
