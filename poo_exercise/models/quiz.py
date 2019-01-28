class Quiz:
    def __init__(self, teacher, questions=None):
        """
        :param questions: The questions on the quiz
        :param teacher: The teacher who created the quiz
        """
        self.questions = questions if questions else []
        self.teacher = teacher

    def add_question(self, question):
        self.questions.append(question)
