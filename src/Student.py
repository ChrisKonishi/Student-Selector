class Student():
    def __init__(self, data):
        self.data = data

        self.approved_subj = []
        self.waiting_list = []

    def approve(self, subject):
        if not(subject in self.approved_subj):
            self.approved_subj.append(subject)

    def wait(self, subject):
        if not(subject in self.waiting_list):
            self.waiting_list.append(subject)

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

    def get_waiting_list(self):
        st = ""
        for i, sub in enumerate(self.waiting_list):
            if i != len(self.waiting_list) - 1:
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
