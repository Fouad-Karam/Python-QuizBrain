from data import question_data
from question_model import Question
from quiz_brain import Quizbrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

next_quiz = Quizbrain(question_bank)

while next_quiz.still_has_questions():
    next_quiz.next_question()

print("You have completed the quiz. Congrats!")
print(f"Your final score is {next_quiz.score}/{next_quiz.question_number}")
