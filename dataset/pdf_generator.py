from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer
import os

INPUT_FOLDER = "Generated_Resumes"

OUTPUT_FOLDER = "Generated_PDF_Resumes"

os.makedirs(
    OUTPUT_FOLDER,
    exist_ok=True
)

styles = getSampleStyleSheet()

def convert_to_pdf(txt_file):

    pdf_name = txt_file.replace(
        ".txt",
        ".pdf"
    )

    pdf_path = os.path.join(
        OUTPUT_FOLDER,
        pdf_name
    )

    doc = SimpleDocTemplate(pdf_path)

    story = []

    txt_path = os.path.join(
        INPUT_FOLDER,
        txt_file
    )

    with open(
        txt_path,
        "r",
        encoding="utf-8"
    ) as f:

        lines = f.readlines()

    for line in lines:

        story.append(
            Paragraph(
                line.strip(),
                styles["BodyText"]
            )
        )

        story.append(
            Spacer(
                1,
                6
            )
        )

    doc.build(story)

print("="*50)

print("Generating PDF Resumes")

print("="*50)

count = 0

for file in os.listdir(INPUT_FOLDER):

    if file.endswith(".txt"):

        convert_to_pdf(file)

        count += 1

print()

print("Done!")

print()

print("PDF Generated :", count)    