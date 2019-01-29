from poo_exercise.models import Classroom, Student


def test_create_classroom(tst):
    cr = Classroom(tst.teacher, 2018, 1)
    assert len(cr.students) == 0
    assert cr.teacher.name == tst.teacher.name
    assert cr.semester == 1
    assert cr.year == 2018


def test_add_student_to_classroom(tst):
    cr = Classroom(tst.teacher, 2018, 1)
    student = Student(name='Calvin Bond')

    assert len(cr.students) == 0
    assert cr.teacher.name == tst.teacher.name
    assert cr.semester == 1
    assert cr.year == 2018

    cr.add_student(student)
    assert len(cr.students) == 1
    assert cr.students[0].name == student.name


def test_add_student_to_classroom_twice(tst):
    cr = Classroom(tst.teacher, 2018, 1)
    student = Student(name='Calvin Bond')

    assert len(cr.students) == 0
    assert cr.teacher.name == tst.teacher.name
    assert cr.semester == 1
    assert cr.year == 2018

    cr.add_student(student)
    cr.add_student(student)
    assert len(cr.students) == 1
    assert cr.students[0].name == student.name
