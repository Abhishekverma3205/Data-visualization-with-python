import numpy as np
import matplotlib.pyplot as plt

student_grades = {"Alice": 90, "Bob": 85, "Charlie": 78}

student_names = list(student_grades.keys())
grades = np.array(list(student_grades.values()))


plt.bar(student_names, grades)

plt.xlabel('Student Names')
plt.ylabel('Grade')
plt.title('Student Grades')


plt.show()