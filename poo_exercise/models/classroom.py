class Classroom:
    def __init__(self, teacher, year, semester):
        """
        :param teacher: The teacher object
        :param year: The year of this class
        :param semester: The semester of this class
        """
        self.teacher = teacher
        self.year = year
        self.semester = semester
        self.teacher.classes.append(self)
        self.students = []

    def add_student(self, student):
        # A student should not be added to the same classroom twice
        if self not in student.classes:
            self.students.append(student)
            student.classes.append(self)
        return self.students
