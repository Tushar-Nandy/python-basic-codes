from data import question_data
from quiz import Question
from quizBrain import QuizBrain
question_bank=[]

for question in question_data:
    question_text=question['q']
    answer=question['a']
    new_question=Question(question_text,answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.nextQuestion()
print("You have completed the quiz!!")
quiz.final_statement()