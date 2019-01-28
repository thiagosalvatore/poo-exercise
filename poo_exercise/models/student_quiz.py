class StudentQuiz:
    def __init__(self, student, quiz):
        self.student = student
        self.quiz = quiz
        self.answered = False
        self.grade = 0
        self.answers = []

    def submit_answers(self, answers):
        self.answers = answers

    def grade_quiz(self):
        answer_points = 10 / len(self.quiz.questions)
        for index, question in enumerate(self.quiz.questions):
            if self.answers[index] == question.correct_answer:
                self.grade += answer_points
        return self.grade
