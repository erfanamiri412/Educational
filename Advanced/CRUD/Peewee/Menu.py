from SchoolManagement import Student, Teacher, Grade

def main():
    while True:
        print('1. Add Student')
        print('2. Add teacher')
        print('3. Add grade')
#..............................................................................................................................
        print('4. Show students')
        print('5. Show teachers')
        print('6. Show grades')
#..............................................................................................................................
        print('7. Update student')
        print('8. Update teacher')
        print('9. Update grade')
#..............................................................................................................................
        print('10. Delete student')
        print('11. Delete teacher')
        print('12. Delete grade')
#..............................................................................................................................
        print('13 exit')

        choice = input('Enter 1,2,3,...,13: ')

        if choice == '1': # add student
            name = input('Enter name: ').strip()
            family = input('Enter family: ').strip()
            age = int(input('Enter age: '))
            Student.create(name = name, family = family, age = age)
            print('Student created successfully')
            break

        elif choice == '2': # add teacher
            name = input('Enter name: ').strip()
            family = input('Enter family: ').strip()
            subject = input('Enter subject: ').strip()
            Teacher.create(name = name, family = family, subject = subject)
            print('Teacher created successfully')
            break

        elif choice == '3': # add grade
            try:
                student_id = int(input('Enter student id: '))
                teacher_id = int(input('Enter teacher id: '))
                st = Student.get(Student.id == student_id)
                te = Teacher.get(Teacher.id == teacher_id)
                grade = float(input('Enter grade: '))
                if st and te:
                    Grade.create(student = student_id, teacher = teacher_id, score = grade)
                print('Grade created successfully')
                break
            except Student.DoesNotExist:
                print('Student not found!')
            except Teacher.DoesNotExist:
                print('Teacher not found!')
#..............................................................................................................................
        elif choice == '4': # show students
            students = Student.select()
            for student in students:
                print(f'{student.id}, {student.name}, {student.family}, {student.age}')
            break

        elif choice == '5': # show teachers
            teachers = Teacher.select()
            for teacher in teachers:
                print(f'{teacher.id}, {teacher.name}, {teacher.family}, {teacher.subject}')
            break

        elif choice == '6': # show grades
            grades = Grade.select()
            for grade in grades:
                print(f'{grade.id}, {grade.student_id}, {grade.teacher_id}, {grade.score}')
            break
#..............................................................................................................................
        elif choice == '7': # update student
            try:
                student_id = int(input('Enter student id: '))
                # st = Student.get(student.id == student_id)
                # if not st:
                #     print('Student not found!')
                #     continue
                name = input('Enter new name: ')
                family = input('Enter new family: ')
                age = int(input('Enter new age: '))
                st = Student.update({Student.name : name, Student.family : family, Student.age : age})
                st.execute()
                print('Student updated successfully.')
                break
            except Student.DoesNotExist:
                print('Student not found!')

            
        elif choice == '8': # update teacher
            try:
                teacher_id = int(input('Enter teacher id: '))
                name = input('Enter new name: ')
                family = input('Enter new family: ')
                subject = int(input('Enter new subject: '))
                te = Teacher.update({Teacher.name : name, Teacher.family : family, Teacher.subject : subject})
                te.execute()
                print('Teacher updated successfully.')
                break
            except Teacher.DoesNotExist:
                print('Teacher not found!')

        elif choice == '9': # update grade
            try:
                grade_id = int(input('Enter grade id: '))
                score = int(input('Enter new score: '))
                gr = Grade.update({Grade.score : score})
                gr.execute()
                print('grade updated successfully.')
                break
            except Grade.DoesNotExist:
                print('grade not found!')
#..............................................................................................................................
        elif choice == '10': #delete student
            # try:
            #     student_id = int(input('Enter student id: '))
            #     st = Student.get(student.id == student_id)
            #     st.delete_instance()
            # except Student.DoesNotExist:
            #     print('Student not found!')
            student_id = int(input('Enter student id: '))
            st = Student.get_or_none(Student.id == student_id)
            if not st:
                print('Student not found!')
                continue
            st.delete_instance()
            print('Student deleted successfully')
            break

        elif choice == '11': #delete teacher
            teacher_id = int(input('Enter teacher id: '))
            te = Teacher.get_or_none(Teacher.id == teacher_id)
            if not te:
                print('Teacher not found!')
                continue
            te.delete_instance()
            print('Teacher deleted successfully')
            break

        elif choice == '12': #delete grade
            grade_id = int(input('Enter teacher id: '))
            gr = Grade.get_or_none(Grade.id == grade_id)
            if not gr:
                print('Grade not found!')
                continue
            gr.delete_instance()
            print('Grade deleted successfully')
            break
#..............................................................................................................................
        elif choice == '13': #exit
            break

if __name__ == '__main__':
    main()