class Question:
    def __init__(self, question, options, correct_answer):
        """
        :param question: The question, for example ("What's your name")
        :param options: The options for the question, for example ["Thiago", "Denis"]
        :param correct_answer: The index of the correct answer
        """
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
