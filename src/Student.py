class Student():
    def __init__(self, data):
        self.data = data

        self.approved_subj = []


    def approve(self, subject):
        if not(subject in self.approved_subj):
            self.approved_subj.append(subject)

    def get_approved_subejcts(self):
        return self.approved_subj

    def is_approved(self):
        if self.approved_subj == []:
            return False
        return True

    def __str__(self):
        cont = ""

        for i in self.data.keys():
            cont += i + ': ' + str(self.data[i]) + '\n'

        return cont