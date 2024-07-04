import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Load the resume from a file
with open('example_resume.txt', 'r') as file:
    resume = file.read()

# Define the prompt
prompt = f"""
You are a Resume Parser. I will provide you with a resume, and your task is to parse the content and convert it into a structured JSON format.

Here is the resume:

{resume}

Please return the resume data in the following JSON format:
{{
  "name": "Full Name",
  "contact_information": {{
    "phone": "Phone Number",
    "email": "Email Address",
    "address": "Home Address"
  }},
  "summary": "Professional summary or objective",
  "experience": [
    {{
      "job_title": "Job Title",
      "company": "Company Name",
      "location": "Location",
      "start_date": "Start Date",
      "end_date": "End Date",
      "responsibilities": [
        "Responsibility 1",
        "Responsibility 2"
      ]
    }}
  ],
  "education": [
    {{
      "degree": "Degree",
      "institution": "Institution Name",
      "location": "Location",
      "graduation_date": "Graduation Date"
    }}
  ],
  "skills": [
    "Skill 1",
    "Skill 2"
  ],
  "certifications": [
    {{
      "certification": "Certification Name",
      "institution": "Institution Name",
      "date": "Date Received"
    }}
  ],
  "projects": [
    {{
      "title": "Project Title",
      "description": "Project Description",
      "technologies": [
        "Technology 1",
        "Technology 2"
      ],
      "link": "Project Link"
    }}
  ]
}}
"""

# Make the API request
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=prompt,
  max_tokens=1500
)

# Print the JSON response
print(response.choices[0].text.strip())
