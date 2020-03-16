'''
Question 3 - Midterm
Author:Yewande Ogunedina
ITMD 513
Title: Load dataset and determine descriptive statistics, and create pie chart for student grades. 
'''

import numpy as np
import matplotlib as plt
import csv
import pandas as pd
import scipy
import matplotlib.pyplot as plt
import turtle
from scipy import stats

#display all data on screen
student = np.loadtxt('/Users/WendyAdedoyin/Documents/student_grades.csv', delimiter = ',', skiprows=1)
student = np.array(student[0:])
print(student)

# Display the number of rows and columns of numpy array
total_rows = np.shape(student)[0]
total_cols = np.shape(student)[1]
print ("Number of rows and columns", (total_rows, total_cols))

#display how many students in the dataset
print ("There are", total_rows, "students")

#display the array data types
file_type = student.dtype
print("Data type is", file_type)

#display descriptive statistics score
min_score = student[:,31].min()
max_score = student[:,31].max()
std_score = student[:,31].std()
mean_score = student[:,31].mean()
percentile_25 = np.percentile(student[:,31],25)
percentile_75 = np.percentile(student[:,31],75)
median_score = np.median(student[:,31])
mode_score = stats.mode(student[:,31])

#print descriptive statistics score
print ("Minimum overall score :", min_score)
print ("Maxium overall score :", max_score)
print ("Mean :", mean_score)
print ("Median:" , median_score)
print ("Mode:", mode_score)
print ("Percentile (25%, 75%):", [percentile_25, percentile_75])
print ("Std. Dev :", std_score)



#determine how many students achieved A,B,C,D,F grades
grade_a = np.sum((student[:,31] > 90) & (student[:,31] < 100))
print("Number of students with grade A:")
print(grade_a)

#grade b
grade_b = np.sum((student[:,31] > 80) & (student[:,31] < 90))
print("Number of students with grade B: ")
print(grade_b)

#grade c
grade_c = np.sum((student[:,31] > 70) & (student[:,31] < 80))
print("Number of students with grade C: ")
print(grade_c)

#grade d 
grade_d = np.sum((student[:,31] > 60) & (student[:,31] < 70))
print("Number of students with grade D: ")
print(grade_d)

#grade f
grade_f = student[:,31]<= 59
print("Number of students with grade F: ")
print(student[grade_f,:].shape[0])


#create pie chart
Grades = [21, 8, 1, 1, 2]
slice_labels = ['Grade is A', ' Grade is B', 'Grade is C', 'Grade is D', 'Grade is F']
explode = (0.1, 0, 0 , 0, 0) #only explode A grade 
plt.pie(Grades, labels=slice_labels, explode=explode)
plt.title ('Student Grades')
plt.show()
