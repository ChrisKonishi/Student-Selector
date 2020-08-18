import pandas as pd

from Student import Student

class Student_reader():
    def __init__(self, file, subjects, attributes):
        self.file = file
        self.subjects = subjects
        self.attributes = attributes

        self.all_student, self.subejct_student = self.process_data()


    def process_data(self):

        #isso aqui eh gambiarra, mas preguiça de deixar elegante
        try:
            data = pd.read_csv(self.file)
        except:
            data = pd.read_excel(self.file)
        

        sub_student = {}
        for i in self.subjects:
            sub_student[i] = []

        all_student = []

        for row in range(len(data)):
            stt_dic = {}
            materias = []

            #aqui eh a atribuicao de dados

            for att in self.attributes.keys():
                aux = None

                if att == "Era Ales":
                    aux = data[self.attributes[att]][row] == "Sim"

                elif att == "É Particular":
                    aux = data[self.attributes[att]][row] == "Privada"

                elif att == "É bolsista":
                    aux = data[self.attributes[att]][row] == "Sim"

                elif att == "É de Campinas":
                    aux = data[self.attributes[att]][row] == "Sim"

                elif att in self.subjects:
                    if data[self.attributes[att]][row] == "Sim":
                        materias.append(att)
                    continue

                else:
                    aux = data[self.attributes[att]][row]

                stt_dic[att] = aux

            stt_dic["Ordem chegada"] = row + 1
            stt_dic["Matérias"] = materias
            #fim da coleta de dados

            student = Student(stt_dic)

            all_student.append(student)

            #decidir materia(s)
            for i in self.subjects:
                if i in stt_dic["Matérias"]:
                    sub_student[i].append(student)


        return all_student, sub_student


    def get_all_students(self):
        return self.all_student

    def get_student_subject(self):
        return self.subejct_student



        

        
