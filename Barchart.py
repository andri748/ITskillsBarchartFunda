import numpy as np
import matplotlib.pyplot as plt

python = (85, 67, 23, 98)
java = (50, 67, 89, 14)
networking = (60, 20, 56, 22)
machine_learning = (88, 23, 40, 87)

people = ['Bob', 'Anna', 'Jhon', 'Mark']

index = np.arange(4)

plt.bar(index, python, width=0.2, label="Python")
plt.bar(index + 0.2, java, width=0.2, label="Java") # index + 0.2 is shifted the bar
plt.bar(index + 0.4, networking, width=0.2, label="Networking") # index + 0.2 is shifted the bar
plt.bar(index + 0.6, machine_learning, width=0.2, label="Machine Learning") # index + 0.2 is shifted the bar

plt.title("IT Skill Levels")
plt.xlabel("Person")
plt.ylabel("Skill Levels")
plt.xticks(index + 0.2, people)
plt.legend(loc='upper right')
plt.ylim(0, 135)

plt.show()
