import pytest

from poo_exercise.models import Question, Quiz, StudentQuiz


def test_assign_quiz_student(tst):
    q1 = Question('whats your name?', ['Thiago', 'James', 'Bond'], 'Thiago')
    q2 = Question('how old are you?', [20, 40, 27], 27)
    quiz = Quiz(tst.teacher, tst.classroom, [q1, q2])

    student_quiz = StudentQuiz(tst.student, quiz)
    assert student_quiz.quiz == quiz
    assert student_quiz.student == tst.student
    assert student_quiz.grade == 0
    assert student_quiz.answers == []


def test_assign_quiz_student_not_in_classroom(tst):
    q1 = Question('whats your name?', ['Thiago', 'James', 'Bond'], 'Thiago')
    q2 = Question('how old are you?', [20, 40, 27], 27)
    quiz = Quiz(tst.teacher, tst.classroom, [q1, q2])
    tst.student.classes = []

    with pytest.raises(AssertionError):
        StudentQuiz(tst.student, quiz)


def test_submit_quiz_answers(tst):
    q1 = Question('whats your name?', ['Thiago', 'James', 'Bond'], 'Thiago')
    q2 = Question('how old are you?', [20, 40, 27], 27)
    quiz = Quiz(tst.teacher, tst.classroom, [q1, q2])
    student_quiz = StudentQuiz(tst.student, quiz)
    student_quiz.submit_answers(['Thiago', 27])

    assert student_quiz.quiz == quiz
    assert student_quiz.student == tst.student
    assert student_quiz.grade == 0
    assert student_quiz.answers == ['Thiago', 27]


def test_submit_quiz_answers_empty(tst):
    q1 = Question('whats your name?', ['Thiago', 'James', 'Bond'], 'Thiago')
    q2 = Question('how old are you?', [20, 40, 27], 27)
    quiz = Quiz(tst.teacher, tst.classroom, [q1, q2])
    student_quiz = StudentQuiz(tst.student, quiz)
    student_quiz.submit_answers(['', ''])

    assert student_quiz.quiz == quiz
    assert student_quiz.student == tst.student
    assert student_quiz.grade == 0
    assert student_quiz.answers == ['', '']


def test_submit_quiz_less_answers_than_options(tst):
    q1 = Question('whats your name?', ['Thiago', 'James', 'Bond'], 'Thiago')
    q2 = Question('how old are you?', [20, 40, 27], 27)
    quiz = Quiz(tst.teacher, tst.classroom, [q1, q2])
    student_quiz = StudentQuiz(tst.student, quiz)

    with pytest.raises(Exception):
        student_quiz.submit_answers(['Thiago'])


def test_submit_quiz_answers_and_grade_ten(tst):
    q1 = Question('whats your name?', ['Thiago', 'James', 'Bond'], 'Thiago')
    q2 = Question('how old are you?', [20, 40, 27], 27)
    quiz = Quiz(tst.teacher, tst.classroom, [q1, q2])
    student_quiz = StudentQuiz(tst.student, quiz)
    student_quiz.submit_answers(['Thiago', 27])

    assert student_quiz.quiz == quiz
    assert student_quiz.student == tst.student
    assert student_quiz.grade == 0
    assert student_quiz.answers == ['Thiago', 27]

    student_quiz.grade_quiz()
    assert student_quiz.grade == 10


def test_submit_quiz_answers_and_grade_5(tst):
    q1 = Question('whats your name?', ['Thiago', 'James', 'Bond'], 'Thiago')
    q2 = Question('how old are you?', [20, 40, 27], 27)
    quiz = Quiz(tst.teacher, tst.classroom, [q1, q2])
    student_quiz = StudentQuiz(tst.student, quiz)
    student_quiz.submit_answers(['Thiago', 40])

    assert student_quiz.quiz == quiz
    assert student_quiz.student == tst.student
    assert student_quiz.grade == 0
    assert student_quiz.answers == ['Thiago', 40]

    student_quiz.grade_quiz()
    assert student_quiz.grade == 5


def test_submit_quiz_answers_and_grade_0(tst):
    q1 = Question('whats your name?', ['Thiago', 'James', 'Bond'], 'Thiago')
    q2 = Question('how old are you?', [20, 40, 27], 27)
    quiz = Quiz(tst.teacher, tst.classroom, [q1, q2])
    student_quiz = StudentQuiz(tst.student, quiz)
    student_quiz.submit_answers(['James', 40])

    assert student_quiz.quiz == quiz
    assert student_quiz.student == tst.student
    assert student_quiz.grade == 0
    assert student_quiz.answers == ['James', 40]

    student_quiz.grade_quiz()
    assert student_quiz.grade == 0
