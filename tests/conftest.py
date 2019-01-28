import pytest

from poo_exercise.models import Classroom, Student, Teacher


def basic_data():
    teacher = Teacher(name='John Kennedy')
    classroom = Classroom(teacher=teacher, year=2019, semester=1)
    student = Student(name='James Bond')
    classroom.add_student(student)
    return type('', (), {'teacher': teacher, 'student': student, 'classroom': classroom})


@pytest.fixture(autouse=True)
def tst():
    return basic_data()
