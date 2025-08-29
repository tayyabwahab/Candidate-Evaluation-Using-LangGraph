import sys
import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text

def data_pdf():
    
    pdf_file = "/home/tayyab/Downloads/Resume/NLP/Resume.pdf"
    extracted_text = extract_text_from_pdf(pdf_file)
    
    # print("----- Extracted Text -----\n")
    # print(extracted_text)
    return extracted_text
