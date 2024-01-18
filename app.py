import os
import streamlit as st
import io
import base64
import google.generativeai as genai 
from dotenv import load_dotenv
from PIL import Image
import pdf2image


load_dotenv()


genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def input_pdf_setup(uploaded_file):
    try:
        if uploaded_file is not None:
            images = pdf2image.convert_from_bytes(uploaded_file.read())
            first_page = images[0]

            img_byte_arr = io.BytesIO()
            first_page.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()

            pdf_parts = [
                    {
                        "mime_type": "image/jpeg",
                        "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
                    }
                ]
            return pdf_parts
    except pdf2image.exceptions.PDFInfoNotInstalledError:
    # Handle the PDFInfoNotInstalledError by providing a helpful message to the user
        st.error("Unable to get page count. Please make sure Poppler is installed and added to the system PATH.")
        st.stop()
    
    else:
        raise FileNotFoundError("No file uploaded")
    

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel("gemini-pro-vision")
    response = model.generate_content([input,pdf_content[0],prompt])
    return response.text

st.set_page_config("Hire-Like-a-Fortune-500-End-to-End-ATS-with-Google-Gemini-Pro-Vision")
st.header("ATS Tracking System")
input_text = st.text_area("Job Description:", key="input")
uploaded_file = st.file_uploader("Upload the resume PDF", type = ["pdf"])

if uploaded_file is not None:
    st.write("PDF uploaded successfully")

submit1 = st.button("Tell me about the resume")
submit2 = st.button("How Can I Improvise my skill")
submit3 = st.button("What are the keywords that are missing")
submit4 = st.button("Percentage Match")


# Input prompts
input_prompt1 = """
As an experienced Technical Human Resource Manager, your expertise is invaluable in evaluating the provided resume against the specific job description.
Please share your professional insights on whether the candidate's profile aligns with the role.
Highlight both strengths and areas for improvement in the applicant's qualifications, ensuring a thorough assessment.
"""

input_prompt2 = """
In your role as a dedicated career advisor, your mission is to provide personalized suggestions for skills enhancement.
Request additional information from the user about their current skills, experiences, and career aspirations.
Based on this information, deliver constructive advice on how they can strategically enhance their skill set for continuous career development.
"""

input_prompt3 = """
Imagine yourself as an AI-powered Keyword Analyst. To identify missing keywords in the resume, 
please upload the job description or provide details about the industry and specific job requirements.
Analyze the resume to pinpoint crucial keywords that might be underrepresented in the document, ensuring a comprehensive coverage.
"""

input_prompt4 = """
As a Match Percentage Calculator, your role is crucial in determining the candidate's suitability for a job.
Please upload both the job description and the candidate's resume.
Leverage your expertise to calculate the percentage match between the required skills and the candidate's qualifications, providing a quantitative assessment.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

if submit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")
if submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")
elif submit4:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt4,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")