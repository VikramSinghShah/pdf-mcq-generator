from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

from werkzeug.utils import secure_filename

from parser import extract_mcqs

import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

questions_cache = []


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route("/upload", methods=["POST"])
def upload():

    global questions_cache

    questions_cache = []

    files = request.files.getlist(
        "pdfs"
    )

    for file in files:

        filename = secure_filename(
            file.filename
        )

        filepath = os.path.join(
            UPLOAD_FOLDER,
            filename
        )

        file.save(filepath)

        extracted_questions = extract_mcqs(
            filepath
        )

        print(
            f"{filename}: {len(extracted_questions)} questions"
        )

        questions_cache.extend(
            extracted_questions
        )

    print(
        "TOTAL QUESTIONS:",
        len(questions_cache)
    )

    return jsonify({
        "total_questions":
        len(questions_cache)
    })


@app.route("/questions")
def questions():

    print(
        "/questions returning:",
        len(questions_cache)
    )

    return jsonify(
        questions_cache
    )


@app.route("/debug")
def debug():

    return jsonify({
        "count":
        len(questions_cache),

        "sample":
        questions_cache[:3]
    })


if __name__ == "__main__":

    app.run(
        debug=True
    )