class Question:
    def __init__(self, question, options, correct_answer):
        """
        The correct answers has to be in the list of options and the list of options cannot be empty
        :param question: The question, for example ("What's your name")
        :param options: The options for the question, for example ["Thiago", "Denis"]
        :param correct_answer: The the correct answer
        """
        assert options
        assert correct_answer in options
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
