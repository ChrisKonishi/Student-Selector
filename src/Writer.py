'''
Writer
Writes a .xlxs file with all approved students and subject classes

init(Student_reader: students, str: path)
    students: contains all students approved and not approved
    path: directory to save the file
'''
import pandas as pd
APROVACAO = "Aprovações"
ESPERA = "Lista de espera"


class Writer:
    def __init__(self, student_reader, path, subjects):
        self.path = path
        self.all_students = student_reader.get_all_students()
        self.subj_students = student_reader.get_students_subject()
        self.subjects = subjects
        self.exwriter = pd.ExcelWriter(path, engine='xlsxwriter')

    def __call__(self):

        # main page
        self.__to_writer__(self.all_students, "Todos os incritos")

        # classes by subject
        for i in self.subjects:
            self.__to_writer__(self.subj_students[i], i)

        self.exwriter.save()

    def __to_writer__(self, students, sheet_name):
        gen_data = self.__emptydict__()
        # read data
        for i in students:
            for j in i.data.keys():
                gen_data[j].append(i.data[j])
            gen_data[APROVACAO].append(i.get_approved_subejcts())
            gen_data[ESPERA].append(i.get_waiting_list())

        # dataframe and to excel
        gen_data = pd.DataFrame(gen_data)
        gen_data.to_excel(
            self.exwriter,
            sheet_name=sheet_name,
            index=False
        )
        self.__adjust_width__(sheet_name, gen_data)

    def __emptydict__(self):
        ret = {}
        for i in self.all_students[0].data.keys():
            ret[i] = []

        ret[APROVACAO] = []
        ret[ESPERA] = []

        return ret

    def __adjust_width__(self, sheet, df):
        writer = self.exwriter
        worksheet = writer.sheets[sheet]  # pull worksheet object
        for idx, col in enumerate(df):  # loop through all columns
            series = df[col]
            max_len = max((
                series.astype(str).map(len).max(),  # len of largest item
                len(str(series.name))  # len of column name/header
            )) + 1  # adding a little extra space
            max_len = min(60, max_len)
            worksheet.set_column(idx, idx, max_len)  # set column width
