import random


class Student:
    def __init__(self, name, knowledge):
        self.name = name
        self.knowledge = knowledge

    def answer_question(self, question):
        if question in self.knowledge:
            answer = self.knowledge[question]
        else:
            answer = random.choice(['I don\'t know', 'Maybe', 'I\'m not sure'])
        return f"{self.name} answers: {answer}. But I might be wrong."


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def ask_question(self, question):
        return f"{self.subject} ({self.name}) asks: {question}"


class Classroom:
    def __init__(self, teacher, students):
        self.teacher = teacher
        self.students = students

    def simulate_class(self, questions):
        for question in range(len(questions)):
            teacher_question = self.teacher.ask_question(question)
            print(teacher_question)
            for student in self.students[1:]:
                student_answer = student.answer_question(question)
                print(student_answer)


teacher = Teacher("Mrs. Smith", "Science")

student_knowledge = [
    {"Is the Earth round?": "Yes", "Do plants need sunlight?": "Yes"},
    {"Is the Earth round?": "Yes", "Do plants need sunlight?": "No"},
    {"Is the Earth round?": "No", "Do plants need sunlight?": "Yes"},
    {"Is the Earth round?": "Maybe", "Do plants need sunlight?": "I don't know"},
    {"Is the Earth round?": "I'm not sure", "Do plants need sunlight?": "Yes"}
]

students = [Student(f"Student {i}", knowledge)
            for i, knowledge in enumerate(student_knowledge, start=1)]
questions = ["Is the Earth round?", "Do plants need sunlight?"]

classroom = Classroom(teacher, students)
classroom.simulate_class(questions)
