class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):")
        self.check_answer(user_answer,current_question.answer)

    def still_has_questions(self):
        number_of_questions = len(self.questions_list)
        return self.question_number < number_of_questions

    def check_answer(self,users_answer,correct_answer):
        if users_answer.lower().startswith("t"):
            users_answer = "true"
        else:
            users_answer = "false"

        if users_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n")