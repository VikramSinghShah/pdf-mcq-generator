let questions = [];
let current = 0;
let answers = {};

async function uploadPDFs() {

    const files =
        document.getElementById(
            "pdfs"
        ).files;

    const formData =
        new FormData();

    for (let file of files) {

        formData.append(
            "pdfs",
            file
        );
    }

    const response =
        await fetch(
            "/upload",
            {
                method: "POST",
                body: formData
            }
        );

    const result =
        await response.json();

    console.log(result);

    await loadQuestions();
}

async function loadQuestions() {

    const response =
        await fetch(
            "/questions"
        );

    questions =
        await response.json();

    console.log(
        "Loaded",
        questions.length,
        "questions"
    );

    current = 0;

    showQuestion();
}

function showQuestion() {

    if (
        !questions ||
        questions.length === 0
    ) {

        document
            .getElementById(
                "quiz"
            )
            .innerHTML =
            "<h2>No Questions Loaded</h2>";

        return;
    }

    const q =
        questions[current];

    document
        .getElementById(
            "quiz"
        )
        .innerHTML = `

<h3>
Question ${current + 1}
of
${questions.length}
</h3>

<h2>
${q.question}
</h2>

<label>
<input
type="radio"
name="answer"
value="A"
${answers[current] === "A" ? "checked" : ""}
onchange="saveAnswer('A')">
${q.option_a}
</label>

<br><br>

<label>
<input
type="radio"
name="answer"
value="B"
${answers[current] === "B" ? "checked" : ""}
onchange="saveAnswer('B')">
${q.option_b}
</label>

<br><br>

<label>
<input
type="radio"
name="answer"
value="C"
${answers[current] === "C" ? "checked" : ""}
onchange="saveAnswer('C')">
${q.option_c}
</label>

<br><br>

<label>
<input
type="radio"
name="answer"
value="D"
${answers[current] === "D" ? "checked" : ""}
onchange="saveAnswer('D')">
${q.option_d}
</label>

<br><br>

<button onclick="previous()">
Previous
</button>

<button onclick="next()">
Next
</button>

`;
}

function saveAnswer(option) {

    answers[current] =
        option;
}

function next() {

    if (
        current <
        questions.length - 1
    ) {

        current++;

        showQuestion();
    }
}

function previous() {

    if (
        current > 0
    ) {

        current--;

        showQuestion();
    }
}