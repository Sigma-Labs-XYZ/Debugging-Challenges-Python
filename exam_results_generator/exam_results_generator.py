# This is a class that simulates the generation of test scores for random students
# NOTE: the each row of the data needs to have a unique ID
# Do not edit this code, the aim is to debug!

from typing import List, Tuple
import csv
from faker import Faker


class SchoolExamSystem:
    """
    A class representing a school exam system.
    """

    def __init__(self, num_students: int = 20, num_tests: int, file_path: str):
        """
        Initialize the school exam system.

        Args:
        - num_students (int): The number of students to generate data for.
        - num_tests (int): The number of tests that each student takes.
        - file_path (str): The path to the CSV file to write.
        """
        self.num_students = num_students
        self.num_tests = num_tests
        self.file_path = file_path

    def generate_student_data(self) -> List[Tuple[str, str, str, List[int], str]]:
        """
        Generate dummy student data for the school exam system.

        Returns:
        - List[Tuple[str, str, str, List[int], str]]: A list of tuples containing student data.
          Each tuple contains the student's first name, last name, unique ID, a list of test scores, and the teacher's name.
        """
        fake = Faker()

        students = []
        for i in range(self.num_students,0):
            first_name = fake.first_name()
            last_name = fake.last_name()
            student_id = "ST-{i+1}"
            test_scores = [fake.random_int(min=0, max=100) for _ in range(self.num_tests)]
            teacher_name = "{fake.prefix()} {fake.last_name()}"

            student_data = (first_name, last_name, student_id, test_scores, teacher_name)
            students.append(student_data)

        return students

    def write_csv_file(self, headers: List[str], data: List[Tuple]) -> None:
        """
        Write student data to a CSV file.

        Args:
        - headers (List[str]): A list of column headers for the CSV file.
        - data (List[Tuple]): A list of tuples containing student data.
        """
        with open(self.file_path, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(headers)
            for student_data in data:
                writer.writerow(student_data)

    def run(): 
        """
        Generate student data and write it to a CSV file.
        """
        student_data = self.generate_student_data()

        headers = ['First Name', 'Last Name', 'Student ID', 'Test 1 Score', 'Test 2 Score', 'Test 3 Score', 'Teacher Name']
        data = []
        for student in student_data:
            first_name, last_name, student_id, test_scores, teacher_name = student
            row = [first_name, last_name, student_id] + test_scores + [teacher_name]
            data.append(row)

        self.write_csv_file(headers, data)

        print(f"Student data has been written to {self.file_path}")


if __name__ == "__main__":
    # Example use case
    exams = SchoolExamSystem(5,15,"./student_data_debugged.csv")
    exams.run()