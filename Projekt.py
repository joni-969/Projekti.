def main():
    total_students = int(input("Shkruani numrin total të nxënësve në klasë: "))
    
    students = {}
    
    for _ in range(total_students):
        name = input(f"Shkruani emrin e nxënësit {_ + 1}: ")
        grade = float(input(f"Shkruani notën për {name}: "))
        students[name] = grade
        
    average_grade = calculate_average(students)
    
    min_grade, max_grade = find_min_max(students)
    
    passed_students, failed_students = categorize_students(students)
    
    print(f"\nMesatarja e notave është: {average_grade}")
    print(f"Nota minimale është: {min_grade}")
    print(f"Nota maksimale është: {max_grade}")
    print("\nNxënësit që kanë kaluar:")
    print_students(passed_students)
    print("\nNxënësit që nuk kanë kaluar:")
    print_students(failed_students)
    
def calculate_average(students):
    total_grade = sum(students.values())
    average_grade = total_grade / len(students)
    return average_grade

def find_min_max(students):
    min_grade = min(students.values())
    max_grade = max(students.values())
    return min_grade, max_grade

def categorize_students(students):
    passed_students = {}
    failed_students = {}
    for name, grade in students.items():
        if grade >= 60:
            passed_students[name] = grade
        else:
            failed_students[name] = grade
    return passed_students, failed_students
def print_students(students):
    for name, grade in students.items():
        print(f"{name}: {grade}")
if __name__ == "__main__":
    main()