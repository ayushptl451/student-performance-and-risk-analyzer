import matplotlib.pyplot as plt
import pandas as pd

# ---------------------------
# 1. DATA
# ---------------------------

# Risk category data (for Pie Chart)
risk_labels = ['Low Risk', 'Medium Risk', 'High Risk']
risk_values = [55, 30, 15]

# Subject-wise performance (for Bar Chart)
subjects = ['Maths', 'Physics', 'Chemistry', 'Programming']
marks = [72, 65, 70, 85]

# Semester-wise performance (for Line Graph)
semesters = ['Sem 1', 'Sem 2', 'Sem 3', 'Sem 4']
avg_scores = [65, 70, 75, 82]

# ---------------------------
# 2. PIE CHART – Risk Category
# ---------------------------
plt.figure()
plt.pie(risk_values, labels=risk_labels, autopct='%1.0f%%', startangle=90)
plt.title("Student Risk Category Distribution")
plt.show()

# ---------------------------
# 3. BAR CHART – Subject Performance
# ---------------------------
plt.figure()
plt.bar(subjects, marks)
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.title("Subject-wise Performance")
plt.show()

# ---------------------------
# 4. LINE GRAPH – Performance Trend
# ---------------------------
plt.figure()
plt.plot(semesters, avg_scores, marker='o')
plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.title("Student Performance Trend")
plt.show()
