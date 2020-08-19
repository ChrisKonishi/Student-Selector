'''
Writer
Writes a .xlxs file with all approved students and subject classes

init(Student_reader: students, str: path)
    students: contains all students approved and not approved
    path: directory to save the file
'''
APROVACAO = "Aprovações"

import pandas as pd

class Writer:
    def __init__(self, student_reader, path, subjects):
        self.path = path
        self.all_students = student_reader.get_all_students()
        self.subj_students = student_reader.get_students_subject()
        self.subjects = subjects
        self.exwriter = pd.ExcelWriter(path, engine='xlsxwriter')

    def __call__(self):
        #main sheet
        gen_data = self.__emptydict__()
        
        #read data
        for i in self.all_students:
            for j in i.data.keys():
                gen_data[j].append(i.data[j])
            gen_data[APROVACAO].append(i.get_approved_subejcts())

        #dataframe and to excel
        gen_data = pd.DataFrame(gen_data)
        gen_data.to_excel(
            self.exwriter,
            sheet_name="Todos os Alunos",
            index=False
        )
        gen_data.to_excel(
            self.exwriter,
            sheet_name="sheet1",
            index=False
        )

        self.exwriter.save()
        


    def __emptydict__(self):
        ret = {}
        for i in self.all_students[0].data.keys():
            ret[i] = []

        ret[APROVACAO] = []

        return ret

    