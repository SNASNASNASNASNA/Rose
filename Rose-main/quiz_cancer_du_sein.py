import tkinter as tk
from tkinter import messagebox

# Définition des questions et réponses
questions = [
    {
        "question": "Quel est le mois de sensibilisation au cancer du sein ?",
        "reponses": ["A) Octobre", "B) Novembre", "C) Décembre"],
        "reponse_correcte": "A) Octobre",
    },
    {
        "question": "Qui peut développer un cancer du sein ?",
        "reponses": ["A) Les femmes uniquement", "B) Les hommes uniquement", "C) Les femmes et les hommes"],
        "reponse_correcte": "C) Les femmes et les hommes",
    },
    {
        "question": "À quel âge les femmes devraient-elles commencer à effectuer des mammographies de dépistage régulières ?",
        "reponses": ["A) 30 ans", "B) 40 ans", "C) 50 ans"],
        "reponse_correcte": "B) 40 ans",
    },
    {
        "question": "Quels sont les facteurs de risque connus du cancer du sein ?",
        "reponses": ["A) Manger des bonbons", "B) Le tabagisme", "C) L'âge, les antécédents familiaux et le sexe"],
        "reponse_correcte": "C) L'âge, les antécédents familiaux et le sexe",
    },
    {
        "question": "Quel est le principal moyen de dépistage précoce du cancer du sein ?",
        "reponses": ["A) Échographie", "B) Biopsie", "C) Mammographie"],
        "reponse_correcte": "C) Mammographie",
    },
    {
        "question": "Que signifie l'acronyme 'AUTOCHEK' en rapport avec le cancer du sein ?",
        "reponses": [
            "A) Un groupe de soutien pour les patients atteints de cancer du sein",
            "B) Un programme de dépistage du cancer du sein",
            "C) Une organisation caritative pour la recherche sur le cancer",
        ],
        "reponse_correcte": "B) Un programme de dépistage du cancer du sein",
    },
    {
        "question": "Quel symptôme peut être un signe de cancer du sein ?",
        "reponses": ["A) Douleur abdominale", "B) Changement de la taille, de la forme ou de la texture du sein", "C) Toux persistante"],
        "reponse_correcte": "B) Changement de la taille, de la forme ou de la texture du sein",
    },
    {
        "question": "Quelle est la couleur traditionnelle associée à la sensibilisation au cancer du sein ?",
        "reponses": ["A) Bleu", "B) Vert", "C) Rose"],
        "reponse_correcte": "C) Rose",
    },
    {
        "question": "Pourquoi est-il important de promouvoir la sensibilisation au cancer du sein ?",
        "reponses": ["A) Pour collecter des dons", "B) Pour encourager la prévention et le dépistage précoce", "C) Pour vendre des produits de beauté"],
        "reponse_correcte": "B) Pour encourager la prévention et le dépistage précoce",
    },
]

# Fonction pour vérifier les réponses et calculer le score
def verifier_reponse(question_index, reponse):
    if questions[question_index]["reponse_correcte"] == reponse:
        return True
    else:
        return False

# Fonction pour afficher le score final et les réponses
def afficher_resultats():
    score = 0
    reponses = []

    for i in range(len(questions)):
        if verifier_reponse(i, choix_var[i].get()):
            score += 1
            reponses.append(f"{questions[i]['question']}\nRéponse : {questions[i]['reponse_correcte']} (Correcte)\n")
        else:
            reponses.append(f"{questions[i]['question']}\nRéponse : {questions[i]['reponse_correcte']} (Incorrecte)\n")

    resultat_text = f"Score final : {score}/{len(questions)}\n\nRéponses :\n\n{''.join(reponses)}"

    messagebox.showinfo("Résultats du quizz", resultat_text)

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Quizz sur le Cancer du Sein")

choix_var = [tk.StringVar() for _ in range(len(questions))]

# Création des widgets pour les questions et réponses
for i, question in enumerate(questions):
    frame = tk.Frame(fenetre)
    frame.pack(pady=10)

    label = tk.Label(frame, text=f"Question {i + 1}: {question['question']}", font=("Arial", 12))
    label.pack()

    for j, reponse in enumerate(question["reponses"]):
        radiobtn = tk.Radiobutton(frame, text=reponse, variable=choix_var[i], value=reponse)
        radiobtn.pack()

# Bouton de soumission des réponses
bouton_submit = tk.Button(fenetre, text="Soumettre", command=afficher_resultats)
bouton_submit.pack(pady=10)

# Boucle principale de l'application
fenetre.mainloop()
