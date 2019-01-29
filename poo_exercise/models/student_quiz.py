class StudentQuiz:
    def __init__(self, student, quiz):
        """
        To associate the student with a quiz, the student has to be in the classroom that the quiz
        is associated with
        :param student: The student that will answer the quiz
        :param quiz: The quiz to be answered
        """
        assert quiz.classroom in student.classes
        self.student = student
        self.quiz = quiz
        self.answered = False
        self.grade = 0
        self.answers = []
        self.student.quizzes.append(self)

    def submit_answers(self, answers):
        if len(answers) != len(self.quiz.questions):
            raise Exception('Less answers than options')
        for index, answer in enumerate(answers):
            if answer and answer not in self.quiz.questions[index].options:
                return None
        self.answers = answers

    def grade_quiz(self):
        answer_points = round(10 / len(self.quiz.questions), 2)
        for index, question in enumerate(self.quiz.questions):
            if self.answers[index] == question.correct_answer:
                self.grade += answer_points
        return self.grade
