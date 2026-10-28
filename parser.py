import fitz
import re


def extract_text(pdf_path):

    text = ""

    try:
        doc = fitz.open(pdf_path)

        for page in doc:
            text += page.get_text("text")

        doc.close()

    except Exception as e:
        print("PDF Error:", e)

    return text


def extract_mcqs(pdf_path):

    text = extract_text(pdf_path)

    questions = []

    blocks = re.split(
        r'Qns\.\d+\)',
        text
    )

    for block in blocks:

        block = block.strip()

        if not block:
            continue

        lines = [
            line.strip()
            for line in block.split("\n")
            if line.strip()
        ]

        option_lines = [
            line for line in lines
            if line.startswith("Option")
        ]

        if len(option_lines) < 4:
            continue

        question_lines = []

        for line in lines:

            if line.startswith("Option"):
                break

            question_lines.append(line)

        question = " ".join(question_lines)

        options = []

        for line in option_lines[:4]:

            option = line.split(":",1)[1].strip()

            options.append(option)

        questions.append({
            "question": question,
            "option_a": options[0],
            "option_b": options[1],
            "option_c": options[2],
            "option_d": options[3],
        })

    print("Extracted:", len(questions))

    return questions
