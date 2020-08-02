import pandas as pd

from Student import Student

class Student_reader():
    def __init__(self, file, subjects, attributes, ignore):
        self.file = file
        self.subjects = subjects
        self.attributes = attributes
        self.ignore = ignore

        self.all_student, self.subejct_student = self.process_data()


    def process_data(self):
        data = pd.read_excel(self.file)

        
