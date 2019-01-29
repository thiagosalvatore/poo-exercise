from poo_exercise.models import Question, Quiz, StudentQuiz
from poo_exercise.services.grade import GradeService


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

    assert GradeService(tst.teacher).calculate_grade(tst.student, 2019, 1) == 10


def test_submit_quiz_answers_and_grade_zero(tst):
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

    assert GradeService(tst.teacher).calculate_grade(tst.student, 2019, 1) == 0


def test_submit_quiz_answers_and_get_grade_another_semester(tst):
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

    assert GradeService(tst.teacher).calculate_grade(tst.student, 2018, 1) == 0
