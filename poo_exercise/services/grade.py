class GradeService:
    def __init__(self, teacher):
        self.teacher = teacher

    def calculate_grade(self, student, year, semester):
        # Get the intersection of classes taught by the teacher and the student
        student_teacher_classes = set(student.classes).intersection(set(self.teacher.classes))
        student_teacher_classes = list(student_teacher_classes)
        classes_semester = filter(lambda c: c.year == year and c.semester == semester,
                                  student_teacher_classes)
