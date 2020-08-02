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
        data = pd.read_csv(self.file)

        sub_student = {}
        for i in self.subjects:
            sub_student[i] = []

        all_student = []

        for row in range(len(data)):
            stt_dic = {}

            #aqui eh a atribuicao de dados
            for att in self.attributes.keys():
                stt_dic[att] = data[self.attributes[att]][row]

            stt_dic["Ordem chegada"] = row + 1
            #fim da coleta de dados

            student = Student(stt_dic)

            all_student.append(student)

            #decidir materia(s)
            for i in self.subjects:
                if i in stt_dic["matéria inscrita"]:
                    sub_student[i].append(student)


        return all_student, sub_student


    def get_all_students(self):
        return self.all_student

    def get_student_subject(self):
        return self.subejct_student


        

        
