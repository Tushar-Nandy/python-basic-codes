class QuizBrain():
    def __init__(self,q_list) -> None:
        self.question_number=0
        self.question_list=q_list
        self.score=0

    def still_has_questions(self):
       return self.question_number<len(self.question_list)
           
    def nextQuestion(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_ans=input(f"Q.{self.question_number}: {current_question.question} (True/False): ").capitalize()
        self.check_answer(user_ans,current_question.answer)
        print(f"Your score is {self.score}")
    
    def check_answer(self,user_answer,correct_answer):
        if user_answer==correct_answer:
            print("You got it right")
            self.score+=1
        else:
            print("You are wrong")
        print(f"The correct answer is {correct_answer}")

    def final_statement(self):
        print(f"You got {self.score}/{len(self.question_list)} right")
