from SchoolManagement import SchoolManagement

def menu():
    sm = SchoolManagement('localhost','root','','SchoolManagement')
    while True:
        print('1. add student')
        print('2. add teacher')
        print('3. add course')
        print('4. add teacher course')
        print('5. add grade')
#..............................................................................................................................
        print('6. show students')
        print('7. show teachers')
        print('8. show courses')
        print('9. show teacher courses')
        print('10. show grades')
#..............................................................................................................................
        print('11. delete student')
        print('12. delete teacher')
        print('13. delete courses')
        print('14. delete teacher course')
        print('15. delete grade')
#..............................................................................................................................
        print('16. update student')
        print('17. update teacher')
        print('18. update course')
        print('19. update teacher course')
        print('20. update grade')
#..............................................................................................................................
        print('21. exit')
        option = input('Enter 1,2,3,...,21: ')

        if option == '1': #add student
            name = input('Enter student name: ').strip()
            family = input('Enter student family: ').strip()
            if not name or family:
                print('Name and family are required and can not be empty!')
            else:
                sm.add_student(name,family)
                print('Student saved successfully.')

        elif option == '2': #add teacher
            name = input('Enter teacher name: ').strip()
            family = input('Enter teacher family: ').strip()
            if not name or family:
                print('Name and family are required and can not be empty!')
            else:    
                sm.add_teacher(name,family)
                print('Teacher saved successfully.')

        elif option == '3': #add course
            name = input('Enter course: ').strip()
            if not name:
                print('Course is required and can not be empty!')
            else:
                sm.add_course(name)
                print('ourse saved successfully.')

        elif option == '4': #add teacher course
            teacher_id = input('Enter teacher id: ')
            course_id = input('course_id: ')
            if not teacher_id or not course_id or not teacher_id.isnumeric() or not course_id.isnumeric():
                print('Invalid data!')
            else:
                sm.add_teacher_course(teacher_id,course_id)

        elif option == '5': #add grade
            student_id = input('Enter student id: ')
            course_id = input('Enter course id: ')
            score = input('Enter score: ')
            is_float_grade = True if score.replace('.','',1).isdigit() else False
            if not student_id or not course_id or not score or not student_id.isnumeric() or not course_id.isnumeric() or not is_float_grade:
                print('Invalid data!')
            else:
                sm.add_grade(student_id,course_id,score)

        elif option == '6': #show students
            students = sm.show_students()
            if not students:
                print('No students found!')
            else:
                for student in students:
                    print(student)

        elif option == '7': #show teachers
            teachers = sm.show_teachers()
            if not teachers:
                print('No teachers found!')
            else:
                for teacher in teachers:
                    print(teacher)

        elif option == '8': #show courses
            courses = sm.show_courses()
            if not courses:
                print('No courses found!')
            else:
                for course in courses:
                    print(course)

        elif option == '9': #show teacher courses
            courses = sm.show_courses()
            if not courses:
                print('No courses found!')
            else:
                for course in courses:
                    print(course)

        elif option == '10': #show grades
            grades = sm.show_grades()
            if not grades:
                print('No grades found!')
            else:
                for grade in grades:
                    print(grade)

        elif option == '11': # delete student
            student_id = input('Enter student id: ')
            if not student_id:
                print('Invalid data!')
            else:
                sm.delete_student(student_id)
                print('Student deleted successfully')

        elif option == '12': # delete teacher
            teacher_id = input('Enter teacher id: ')
            if not teacher_id:
                print('Invalid data!')
            else:
                sm.delete_teacher(teacher_id)
                print('Teacher deleted successfully')

        elif option == '13': # delete course
            course_id = input('Enter course id: ')
            if not course_id:
                print('Invalid data!')
            else:
                sm.delete_course(course_id)
                print('Course deleted successfully')

        elif option == '14': # delete teacher course
            teacher_id = input('Enter teacher id: ')
            if not teacher_id:
                print('Invalid data!')
            else:
                sm.delete_teacher_course(teacher_id)
                print('Teacher course deleted successfully')

        elif option == '15': # delete grade
            grade_id = input('Enter grade id: ')
            if not grade_id:
                print('Invalid data!')
            else:
                sm.delete_grade(grade_id)
                print('Grade deleted successfully')

        elif option == '16': # update student
            student_id = input('Enter student id: ')
            new_name = input('Enter new name: ').strip()
            new_family = input('Enter new family: ').strip()
            sm.update_student(int(student_id),new_name,new_family)

        elif option == '17': # update teacher
            teacher_id = input('Enter teacher id: ')
            new_name = input('Enter new name: ').strip()
            new_family = input('Enter new family: ').strip()
            sm.update_teacher(int(teacher_id),new_name,new_family)

        elif option == '18': # update course
            course_id = input('Enter course id: ')
            new_course = input('Enter new course: ').strip()
            sm.update_course(int(course_id),new_course)

        elif option == '19': # update teacher course
            teacher_id = input('Enter teacher id: ')
            new_teacher_id = input('Enter new teacher id: ').strip()
            new_course_id = input('Enter new course id: ').strip()
            sm.update_teacher_course(int(teacher_id),new_teacher_id,new_course_id)

        elif option == '20': # update grade
            grade_id = input('Enter grade id: ')
            new_score = input('Enter new score: ').strip()
            sm.update_grade(int(grade_id),new_score)

        elif option == '21':
            break

        else:
            print('ERROR!')

if __name__ == '__main__':
    menu()