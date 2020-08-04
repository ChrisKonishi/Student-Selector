class Student_prioritizer():

'''
Receives a list of students of a single subejct and sort them, starting with those with more priority to be enrolled.

init(list: criteria)
criteria: list of tuples containing student attributes to be considered and if it is reversed or not. e.g. [("age", True), ("public school", False)]

call( list: students)
students: list os Students to be sorted
returns: the same list, ordered according to the described behavior.
'''
    
    def __init__(self, criteria):
        self.criteria = criteria

    def __call__(self, students)
        for i in reversed(self.criteria):
            students.sort(key=lambda x: x.data[i[0]], reverse=i[1])

        return students