'''
Decides if a student is allowed to enroll in a subject

init(dict: limit)
limit: dictionary containing the limit number of students, divided by subject

call(dict: students)
students: dictionary containing all students sorted, divided by subject
returns: dictionary containing the students, divided by subject. The students are updated, marking in which subjects they are allowed to enroll
'''
class Approver():
    def __init__(self, limit):
        self.limit = limit

    def __call__(self, students):
        for i in self.limit.keys():
            for j in range(len(students[i])):

                try:
                    if students[i][j].data["Ignorar"]:
                        continue

                except:
                    pass

                if j < self.limit[i]:
                    students[i][j].approve(i)

                else:
                    students[i][j].wait(i)

        return students

