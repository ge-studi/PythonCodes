# Consider a CSV file made through Excel, containing student data such as roll no, name, gender and marks obtained, such as:
# R010,Anurag,M,78
# R012,Disha,F,67
# R013,Gurvinder,M,72

# Load this information into appropriate data structure so that you can query on a roll no and retrieve the name, gender or marks.

# Further, write a function to get a list of names who have obtained higher than certain marks.
# L = getHigherThan(60)


import csv 

# Load data
def load_student_data(filename):
    student_data = {}
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            roll_no, name, gender, marks = row
            student_data[roll_no] = {
                'name': name,
                'gender': gender,
                'marks': int(marks)
            }
    return student_data

# Query
def get_student_info(student_data, roll_no):
    return student_data.get(roll_no, "Roll number not found.")

# Get list of names who scored higher than certain marks
def getHigherThan(student_data, threshold):
    return[info['name'] for info in student_data.values() if info['marks']> threshold]


filename = 'students.csv'
students = load_student_data(filename)

print(get_student_info(students, 'R012'))

L=getHigherThan(students, 60)
print("Students with marks > 60:", L)