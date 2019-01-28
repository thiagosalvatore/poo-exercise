from poo_exercise.models import Question, Quiz


def test_create_quiz_two_questions(tst):
    q1 = Question('whats your name?', ['Thiago', 'James', 'Bond'], 'Thiago')
    q2 = Question('how old are you?', [20, 40, 27], 27)

    assert q1.question == 'whats your name?'
    assert q1.options == ['Thiago', 'James', 'Bond']
    assert q1.correct_answer == 'Thiago'

    quiz = Quiz(tst.teacher, tst.classroom, [q1, q2])
    assert len(quiz.questions) == 2
    assert quiz.questions == [q1, q2]
    assert quiz.teacher.name == tst.teacher.name


def test_create_quiz_with_questions_later(tst):
    q1 = Question('whats your name?', ['Thiago', 'James', 'Bond'], 'Thiago')
    q2 = Question('how old are you?', [20, 40, 27], 27)

    assert q1.question == 'whats your name?'
    assert q1.options == ['Thiago', 'James', 'Bond']
    assert q1.correct_answer == 'Thiago'

    quiz = Quiz(tst.teacher, tst.classroom)
    assert len(quiz.questions) == 0
    assert quiz.questions == []
    assert quiz.teacher.name == tst.teacher.name

    quiz.add_question(q1)
    quiz.add_question(q2)

    assert len(quiz.questions) == 2
    assert quiz.questions == [q1, q2]
