# Dictionary to store student details
students = {}

def add_student(name, student_id, s_class):

    if student_id in students:
        print(f"Student ID {student_id} already exists")
        else:
            students[student_id] = {
                "name": name,
                "class": s_class,
                "grades":[]
                }
            print(f"Student {name} added.")

def update_grades(student_id, grades):

    if student_id in students:
        students[student_id]['grades'].extend(grades)
        print(f"Grades updated for student {students[student_id]['name']}.")
        else:
            print(f"Student Id {student_id} does not exist.")

def calculate_average(student_id):
    
    if student_id in students:
        grades = students[student_id]['grades']
        if grades:
            return sum(grades) /len(grades)
        else:
            return 0.0

     else:
        print(f"Student ID {student_id} does not exist.")
        return NONE

def generate_top_students_report():
    class_top_students = {}
    
    for student_id, details in students.items():
        s_class = details['class']
        average_grade = calculate_average(student_id)
    


        
             
            
     













































        
             
            
     












































