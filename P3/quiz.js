// Questions et réponses
const questions = [
    {
        question: "Quel est le mois de sensibilisation au cancer du sein ?",
        reponseCorrecte: "A"
    },
    {
        question: "Qui peut développer un cancer du sein ?",
        reponseCorrecte: "C"
    },
    // Ajoutez les autres questions ici...
];

let score = 0;
let questionIndex = 0;

function afficherQuestion() {
    const questionText = document.getElementById("question");
    const reponsesListe = document.getElementById("reponses");
    const questionCourante = questions[questionIndex];

    questionText.textContent = `Question ${questionIndex + 1} : ${questionCourante.question}`;

    reponsesListe.innerHTML = "";
    questionCourante.reponses.forEach((reponse, index) => {
        reponsesListe.innerHTML += `<li><button onclick="verifierReponse('${String.fromCharCode(65 + index)}')">${reponse}</button></li>`;
    });
}

function verifierReponse(reponseUtilisateur) {
    const questionCourante = questions[questionIndex];
    if (reponseUtilisateur === questionCourante.reponseCorrecte) {
        score++;
    }

    questionIndex++;

    if (questionIndex < questions.length) {
        afficherQuestion();
    } else {
        afficherResultats();
    }
}

function afficherResultats() {
    const scoreText = document.getElementById("score");
    scoreText.textContent = score;
}
afficherQuestion();
