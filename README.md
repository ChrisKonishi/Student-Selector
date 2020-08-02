# Student Selector
Project for student selection for Projeto Ales

# Required libraries
Pandas

# Classes

## Student

Wraps all relevant data relateng to a single student

#### init(dict: data)
- data: a dictionary containing all relevant data (keys: search for attributes)

#### method: is_approved()
- returns: True if they are approved to enroll in any class, else otherwise

#### method: get_approved_subejcts()
- returns: list containing all approved subejcts

#### method: approve(str: subject)
- subject: name of a subject which the student is allowed to enroll



## Student_reader

Processes raw student data collecting relevant information

#### init(str: file, list: subjects, list: attributes, dict: ignore)
- file: csv file directory with students data
- subjects: list of subjects, as they will be written
- attributes: which attributes should be collected, written as dictionry keys
- ignore: dictionary with subject names as keys and contains lists of students to be ignored

#### method: get_all_students()
- returns: list of Students containing all students

#### method: get_students_subject()
- returns: dictionary with subject names as keys and contains list of Students


## Student_priority

Receives a List of students of a single subejct and sort them starting with those with more priority to be enrolled.

#### init(list: criteria, list: students)
- criteria: list of student attributes to be considered, starting with the more relevant. Higher values come first.
- students: list os Students to be sorted

#### call()
- returns: the same list, ordered according to the described behavior.


## Approver

Decides if a student is allowed to enroll in a subject

#### init(dict: students, dict: limit)
- students: dictionary containing all students sorted, divided by subject
- limit: dictionary containing the limit number of students, divided by subject

#### call()
- returns: dictionary containing the limit number of students, divided by subject. But the students are updated, knowing which subjects they are allowed to enroll



## Writer

Writes a .xlxs file with all approved students and by subject

#### init(Student_reader: students, str: path)
- students: contains all students approved and not approved
- path: directory to save the file



