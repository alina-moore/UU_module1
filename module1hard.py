grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# первый вариант. с использованием непройденных функций
sorted_students = sorted(students)
# print(sorted_students)

sum_each = [sum(i) for i in grades]
# print(sum_each)
len_each = [len(i) for i in grades]
# print(len_each)

average_grade = [summa / kolichestvo for summa, kolichestvo in zip(sum_each, len_each)]
# print(average_grade)

journal = dict(zip(sorted_students, average_grade))
print(journal)
print()

# второй вариант. без использования непройденных функций
students = list(students)
# print(min(students), max(students))
# students.remove("Aaron"), students.remove("Steve")
# print(students)
# print(min(students), max(students))
# print(len(students)

students[0] = "Aaron"
students[1] = "Bilbo"
students[2] = "Johnny"
students[3] = "Khendrik"
students[4] = "Steve"

# print(students)
# print(len(grades)

# print(sum(grades[0]))
# print(sum(grades[1]))
# print(sum(grades[2]))
# print(sum(grades[3]))
# print(sum(grades[4]))

# print(len(grades[0]))
# print(len(grades[1]))
# print(len(grades[2]))
# print(len(grades[3]))
# print(len(grades[4]))

# print(sum(grades[0])/len(grades[0]))
# print(sum(grades[1])/len(grades[1]))
# print(sum(grades[2])/len(grades[2]))
# print(sum(grades[3])/len(grades[3]))
# print(sum(grades[4])/len(grades[4]))

journal_2 = {students[0]: sum(grades[0]) / len(grades[0]), students[1]: sum(grades[1]) / len(grades[1]),
             students[2]: sum(grades[2]) / len(grades[2]), students[3]: sum(grades[3]) / len(grades[3]),
             students[4]: sum(grades[4]) / len(grades[4])}
print(journal_2)
