def calc_Average(name, math_Grade, english_Grade, science_Grade):
    calculated_Average = (math_Grade + english_Grade + science_Grade) / 3
    print(f"\nMath = {math_Grade} English = {english_Grade} Science = {science_Grade}")
    print(f"{name}'s average grade is: {calculated_Average:.2f}")
    """
    The line 3 prints out based on sample out and the initialize value of calc_average
    The line 4 prints out the name its average with .2f for 2 decimal format 
    This line 10 uses noOfStudents to calculate average based on usersinput wanted
    """

noOfStudents = int(input("How many students do you want to calculate the average?"))

for i in range(noOfStudents):
    name = input("\nEnter the student's name: ")
    math_Grade = float(input("Enter the math grade: "))
    english_Grade = float(input("Enter the English grade: "))
    science_Grade = float(input("Enter the Science grade: "))

    calc_Average(name, math_Grade, english_Grade, science_Grade)

"""I used for loop to the userinputs based on the noOfstudents then get the userinput for name and grade of 3 subjects
    Then call the calc_average to prints out the needed information such us name, its grade for 3 subjects and then its average
    
    Copyrights © https://github.com/Dramos02
"""

