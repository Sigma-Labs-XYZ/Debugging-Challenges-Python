import unittest
from classroom import Student, Teacher, Classroom


class TestClassroomSimulation(unittest.TestCase):

    def test_student(self):
        student = Student("Test Student", {"Is the Earth round?": "Yes"})
        self.assertEqual(student.answer_question(
            "Is the Earth round?"), "Test Student answers: Yes")
        self.assertIn(student.answer_question("Unknown question"), ["Test Student answers: I don't know",
                                                                    "Test Student answers: Maybe",
                                                                    "Test Student answers: I'm not sure"])

    def test_teacher(self):
        teacher = Teacher("Test Teacher", "Math")
        self.assertEqual(teacher.ask_question("What is 2 + 2?"),
                         "Test Teacher (Math) asks: What is 2 + 2?")

    def test_classroom(self):
        teacher = Teacher("Mrs. Smith", "Science")
        student_knowledge = [
            {"Is the Earth round?": "Yes", "Do plants need sunlight?": "Yes"},
            {"Is the Earth round?": "Yes", "Do plants need sunlight?": "No"},
            {"Is the Earth round?": "No", "Do plants need sunlight?": "Yes"},
            {"Is the Earth round?": "Maybe",
                "Do plants need sunlight?": "I don't know"},
            {"Is the Earth round?": "I'm not sure",
                "Do plants need sunlight?": "Yes"}
        ]
        students = [Student(f"Student {i}", knowledge) for i, knowledge in enumerate(
            student_knowledge, start=1)]
        classroom = Classroom(teacher, students)

        self.assertEqual(classroom.teacher, teacher)
        self.assertEqual(classroom.students, students)


if __name__ == '__main__':
    unittest.main()
