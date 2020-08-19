# Student Selector
Student selection project for Projeto Ales

---

# Required libraries
Pandas

---

# Running
- Download the code
- Keep the same folder structure
- Get the candidates data (.csv or .xlsx)
- Use the Jupyter Notebook "Executar.ipynb" to set up your parameters and run the code

---

# Classes

## Student

Wraps all relevant data related to a single student

#### init(dict: data)
- data: a dictionary containing all relevant data (keys: attributes)

#### method: is_approved()
- returns: True if they are approved to enroll in any class, False otherwise

#### method: get_approved_subejcts()
- returns: list containing all approved subjects

#### method: approve(str: subject)
- subject: name of a subject in which the student is allowed to enroll

---

## Student_reader

Processes raw student data, collecting relevant information

#### init(str: file, list: subjects, list: attributes, dict: ignore)
- file: .csv or .xlsx file directory with students data
- subjects: list of subjects, as they will be written
- attributes: which attributes should be collected, written as dictionary keys to the excel coluumn
- ignore: dictionary with subject names as keys, containing lists of students to be ignored

#### method: get_all_students()
- returns: list of Students containing all students

#### method: get_students_subject()
- returns: dictionary with subject names as keys, containing lists of Students

---

## Student_sorter

Receives a list of students of a single subejct and sorts them, starting with those with more priority to be enrolled.

#### init(list: criteria)
- criteria: list of tuples containing student attributes to be considered and if it is reversed or not. e.g. [("age", True), ("public school", False)]

#### call( list: students)
- students: list os Students to be sorted
- returns: the same list, ordered according to the described behavior.

---

## Approver

Decides if a student is allowed to enroll in a subject

#### init(dict: limit)
- limit: dictionary containing the limit number of students, divided by subject

#### call(dict: students)
- students: dictionary containing all students sorted, divided by subject
- returns: dictionary containing the students, divided by subject. The students are updated, marking in which subjects they are allowed to enroll

---

## Writer

Writes a .xlxs file with all approved students and subject classes

#### init(Student_reader: students, str: path, list:subjects)
- students: contains all students approved and not approved
- path: directory to save the file (containing filename)
- subjects: list with the subject names

#### call()
writes an excel file (directory + name in path) with all students sorted, approved (or not) and divided by subject


