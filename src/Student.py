class Student():
    def __init__(self, data):
        self.data = data

        self.approved_subj = []


    def approve(self, subject):
        if not(subject in self.approved_subj):
            self.approved_subj.append(subject)

    def get_approved_subejcts(self):
        if self.approved_subj == []:
            return "Nenhuma"

        st = ""
        for i, sub in enumerate(self.approved_subj):
            if i != len(self.approved_subj) - 1:
                st += sub + ", "
                continue
            st += sub

        return st

    def is_approved(self):
        if self.approved_subj == []:
            return False
        return True

    def __str__(self):
        cont = ""

        for i in self.data.keys():
            cont += i + ': ' + str(self.data[i]) + '\n'
        
        cont += "Aprovações: " + str(self.approved_subj) + '\n'

        return cont