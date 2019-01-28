import pytest

from poo_exercise.models import Student, Teacher


def basic_data():
    teacher = Teacher(name='John Kennedy')
    student = Student(name='James Bond')

    return type('', (), {'teacher': teacher, 'student': student})


@pytest.fixture(autouse=True)
def tst():
    return basic_data()
