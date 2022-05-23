from student_cl import Student

students = [['a', 'b', [1, 2, 3, 4, 5]], ['c', 'd', [1, 2, 2, 2, 2]], ['e', 'f', [3, 3, 3, 3, 3]],
            ['g', 'h', [5, 5, 5, 5, 5]], ['j', 'k', [0, 0, 0, 0, 0]]]

students = [Student(*students[i]) for i in range(len(students))]
# for i in range(len(students)):
# print(students[i].average_grade)
students = sorted(students, key=lambda st: st.average_grade, reverse=True)
for student in students:
    print([student.full_name, student.group, student.average_grade])
