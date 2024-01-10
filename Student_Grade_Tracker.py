class StudentGradeTracker:
    def __init__(self, student_name):
        self.student_name = student_name
        self.subjects = {}
    
    def add_grade(self, subject, grade):
        if subject in self.subjects:
            self.subjects[subject].append(grade)
        else:
            self.subjects[subject] = [grade]
    
    def calculate_average_grade(self):
        total_grades = 0
        total_subjects = 0
        
        for subject, grades in self.subjects.items():
            total_grades += sum(grades)
            total_subjects += len(grades)
        
        if total_subjects == 0:
            return 0
        else:
            return total_grades / total_subjects

# Example usage:
student_name = input("Enter student's name: ")
tracker = StudentGradeTracker(student_name)

while True:
    print("\nOptions:")
    print("1. Add Grade")
    print("2. Calculate Average Grade")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        subject = input("Enter subject: ")
        grade = float(input("Enter grade: "))
        tracker.add_grade(subject, grade)
    elif choice == '2':
        average_grade = tracker.calculate_average_grade()
        print(f"\nAverage grade for {student_name}: {average_grade:.2f}")
    elif choice == '3':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
