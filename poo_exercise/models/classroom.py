class Classroom:
    def __init__(self, teacher, code, year, semester, students=None):
        """
        :param teacher: The teacher object
        :param code: The code of the class (for example CC231)
        :param year: The year of this class
        :param semester: The semester of this class
        :param code: The code of the class (for example CC231)
        :param students: The students in this classroom (optional)
        """
        self.code = code
        self.teacher = teacher
        self.year = year
        self.semester = semester
        self.students = students if students else []

    def add_student_to_class(self, student):
        self.students.append(student)
        return self.students
