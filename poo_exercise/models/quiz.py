class Quiz:
    def __init__(self, teacher, classroom, questions=None):
        """
        Given that the teacher has to calculate the grade of a student in a specific semester
        I decided to relate the quiz with a class too
        :param questions: The questions on the quiz
        :param teacher: The teacher who created the quiz
        """
        self.questions = questions if questions else []
        self.teacher = teacher
        self.classroom = classroom

    def add_question(self, question):
        self.questions.append(question)
