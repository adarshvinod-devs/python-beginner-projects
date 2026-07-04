students_marks = {}
temp_student_marks = {}
subjects = ["Maths","Science","English"]
choices = {1:"Add Student",2:"Add Marks of a student",3:"Find the average marks of a student",4:"View existing students",5:"Exit"}

def add_student():
  name = input("Enter the student's name to save: ")
  students_marks[name] = {}
  print("Name is saved")

def add_marks():
   global students_marks
   try:
      name = input("Enter the students name to add marks: ")
      if name in students_marks:
         temp_student_marks = students_marks[name].copy()
         for i in subjects:
            marks = int(input(f"Enter the marks of {i}: "))
            temp_student_marks[i]=marks
         if len(temp_student_marks) == len(subjects):
            students_marks[name] = temp_student_marks
            print("Marks are saved")
      else:
         print("This student does not exist")
   except ValueError:
      print("Please enter a digit")

def average_marks():
   name = input("Enter the students name to check average marks: ")
   if name in students_marks and students_marks[name]:
      avg = sum(students_marks[name].values())/ len(students_marks[name])
      print(f"Average marks = {avg}")
   elif name in students_marks:
      print("Marks are not uploaded yet")
   else:
      print("This student does not exist")

def view_students():
   for key in students_marks.keys():
      print(f"{key} :")
      for key1,value1 in students_marks[key].items():
         print(f"   {key1} : {value1}")
         

while True:
   try:
      for key,value in choices.items():
         print(f"{key} -> {value}") 
      choice = int(input("Enter your choice: "))
      match choice:
         case 1:
            add_student()
         case 2:
            add_marks()
         case 3:
            average_marks()
         case 4:
            view_students()
         case 5:
            break
         case _:
            print("Enter a valid choice")
         
   except ValueError:
      print("Enter the corresponding number to your choice")