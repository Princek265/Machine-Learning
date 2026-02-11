import matplotlib.pyplot as plt

# Meaningful data
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8]
exam_score   = [35, 40, 50, 55, 65, 70, 80, 85]

plt.scatter(hours_studied, exam_score)

plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Relationship Between Study Time and Exam Score")
plt.grid(True)
plt.show()
