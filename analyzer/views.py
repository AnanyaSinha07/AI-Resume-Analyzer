from django.shortcuts import render
from PyPDF2 import PdfReader
import re


def home(request):

    extracted_text = ""

    name = ""
    email = ""
    phone = ""

    skills_found = []

    matched_skills = []
    missing_skills = []
    ats_score = 0

    skills_list = [
        "python",
        "sql",
        "mysql",
        "html",
        "css",
        "javascript",
        "django",
        "flask",
        "numpy",
        "pandas",
        "machine learning",
        "deep learning",
        "data analysis",
        "git",
        "github",
        "c",
        "c++",
        "java"
    ]

    if request.method == "POST":

        uploaded_file = request.FILES.get("resume")
        job_description = request.POST.get("job_description", "")

        if uploaded_file:

            reader = PdfReader(uploaded_file)

            for page in reader.pages:

                text = page.extract_text()

                if text:
                    extracted_text += text + "\n"

            # Name
            lines = extracted_text.split("\n")

            for line in lines:

                line = line.strip()

                if len(line) > 2 and len(line) < 40:

                    if not any(char.isdigit() for char in line):

                        name = line
                        break

            # Email
            email_match = re.search(
                r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
                extracted_text
            )

            if email_match:
                email = email_match.group()

            # Phone
            phone_match = re.search(
                r'\d{10}',
                extracted_text
            )

            if phone_match:
                phone = phone_match.group()

            # Resume Skills
            resume_text_lower = extracted_text.lower()

            for skill in skills_list:

                if skill in resume_text_lower:
                    skills_found.append(skill)

            # Job Description Skills
            jd_lower = job_description.lower()

            jd_skills = []

            for skill in skills_list:

                if skill in jd_lower:
                    jd_skills.append(skill)

            # ATS Calculation
            for skill in jd_skills:

                if skill in skills_found:
                    matched_skills.append(skill)
                else:
                    missing_skills.append(skill)

            if len(jd_skills) > 0:
                ats_score = round(
                    (len(matched_skills) / len(jd_skills)) * 100,
                    2
                )

    return render(
        request,
        "analyzer/home.html",
        {
            "text": extracted_text,
            "name": name,
            "email": email,
            "phone": phone,
            "skills": skills_found,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "ats_score": ats_score
        }
    )