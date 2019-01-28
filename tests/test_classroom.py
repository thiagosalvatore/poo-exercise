from poo_exercise.models import Classroom


def test_create_classroom(tst):
    cr = Classroom(tst.teacher, 2018, 1)
    assert len(cr.students) == 0
    assert cr.teacher.name == tst.teacher.name
    assert cr.semester == 1
    assert cr.year == 2018


def test_add_student_to_classroom(tst):
    cr = Classroom(tst.teacher, 2018, 1)
    assert len(cr.students) == 0
    assert cr.teacher.name == tst.teacher.name
    assert cr.semester == 1
    assert cr.year == 2018

    cr.add_student(tst.student)
    assert len(cr.students) == 1
    assert cr.students[0].name == tst.student.name
