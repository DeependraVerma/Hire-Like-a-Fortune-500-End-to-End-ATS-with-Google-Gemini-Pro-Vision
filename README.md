# **Hire Like a Fortune 500: End-to-End ATS with Google Gemini Pro Vision**

Welcome to the **Hire Like a Fortune 500** project, your comprehensive End-to-End Applicant Tracking System (ATS) powered by Google Gemini Pro Vision. This cutting-edge system leverages advanced AI to analyze resumes and provide valuable insights for hiring professionals. Whether you want to evaluate a candidate's profile, offer career advice, identify missing keywords, or calculate the percentage match, this tool has you covered.

## Getting Started

### Prerequisites

Make sure you have the following Python libraries installed:

- streamlit
- google-generativeai
- python-dotenv
- langchain
- pdf2image

Additionally, ensure that Poppler is installed on your local machine to enable the pdf2image library.

### Installation

```bash
pip install streamlit google-generativeai python-dotenv langchain pdf2image
```

## Usage

1. **Job Description Input:**
    - Enter the job description in the provided text area.

2. **Resume Upload:**
    - Upload the candidate's resume in PDF format.

3. **Choose Action:**
    - Select one of the following actions:
        - "Tell me about the resume"
        - "How Can I Improve my skill"
        - "What are the keywords that are missing"
        - "Percentage Match"

4. **Get Results:**
    - Click the corresponding button to receive AI-generated insights.

## Actions and Prompts

### Action 1: Tell me about the resume
Prompt:
```plaintext
As an experienced Technical Human Resource Manager, your expertise is invaluable in evaluating the provided resume against the specific job description.
Please share your professional insights on whether the candidate's profile aligns with the role.
Highlight both strengths and areas for improvement in the applicant's qualifications, ensuring a thorough assessment.
```

### Action 2: How Can I Improve my skill
Prompt:
```plaintext
In your role as a dedicated career advisor, your mission is to provide personalized suggestions for skills enhancement.
Request additional information from the user about their current skills, experiences, and career aspirations.
Based on this information, deliver constructive advice on how they can strategically enhance their skill set for continuous career development.
```

### Action 3: What are the keywords that are missing
Prompt:
```plaintext
Imagine yourself as an AI-powered Keyword Analyst. To identify missing keywords in the resume, 
please upload the job description or provide details about the industry and specific job requirements.
Analyze the resume to pinpoint crucial keywords that might be underrepresented in the document, ensuring a comprehensive coverage.
```

### Action 4: Percentage Match
Prompt:
```plaintext
As a Match Percentage Calculator, your role is crucial in determining the candidate's suitability for a job.
Please upload both the job description and the candidate's resume.
Leverage your expertise to calculate the percentage match between the required skills and the candidate's qualifications, providing a quantitative assessment.
```

## Notes

- Ensure your Google API key is set as an environment variable named "GOOGLE_API_KEY" for Google Gemini Pro Vision.

Feel free to explore, analyze, and make data-driven decisions with the **Hire Like a Fortune 500** ATS! 🚀